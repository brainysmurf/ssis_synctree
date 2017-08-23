"""
Interface with postgres moodle database
Some of the lower-level functions might be useful in a more abstract class
"""
from sqlalchemy import and_, not_, or_
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from sqlalchemy import desc, asc
from sqlalchemy import func, case, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import aliased
from collections import defaultdict
from sqlalchemy.sql.expression import cast, delete
import logging
import re

# moodle stuff:
from ssis_synctree.moodle import MoodleDBSchema    # yes, import the module itself, used for getattr statements
from ssis_synctree.moodle.MoodleDBSchema import *  # and, yes, import all the terms we need to refer to the tables as classes

# app stuff:
from ssis_synctree.utils import Namespace, time_now
import ssis_synctree_settings

from synctree.results import successful_result, unsuccessful_result, exception_during_call

from ssis_synctree.utils import DynamicMockIf


class MoodleInter:
    """
    Mixin that implements lower-level conveniene methods that handles sessions, transactions, queries
    Errors are not trapped, should be handled at higher level
    Does not implement self.db_session, that is left for the subclass
    """

    def table_string_to_class(self, table):
        """
        This provides the whole class with an API whereby
        table_name can be a string that equals the equiv in the actual database
        so that places outside of me don't have to do a bunch of imports
        TODO: Find the native sqlalchemy way of doing this conversion
        @table should be a string
        @returns Database class that can be used in queries
        """
        if table.lower().endswith('data'):
            table = table[:-4] + 'datum'
        if table.endswith('s'):
            table = table[:-1]
        ret = getattr(MoodleDBSchema, table.replace('_', ' ').title().replace(' ', ''))
        return ret

    def wrap_no_result(self, f, *args, **kwargs):
        """
        For simple work, returns None if NoResultFound is encountered
        Most useful when calling an sqlalchemy function like one() and you want
        a simple way to handle an error
        """
        try:
            return f(*args, **kwargs)
        except NoResultFound:
            return None

    def insert_table(self, table, **kwargs):
        with self.db_session() as session:
            table_class = self.table_string_to_class(table)
            instance = table_class()
            for key in kwargs.keys():
                setattr(instance, key, kwargs[key])
            session.add(instance)

    def delete_table(self, table, **kwargs):
        with self.db_session() as session:
            table_class = self.table_string_to_class(table)
            table_class.delete(**kwargs)

    def get_rows_in_table(self, table, **kwargs):
        """
        @table string of the table name (without the prefix)
        @param kwargs is the where statement
        """
        table_class = self.table_string_to_class(table)
        with self.db_session() as session:
            statement = session.query(table_class).filter_by(**kwargs)
        return statement.all()

    def update_table(self, table, where={}, **kwargs):
        """
        Can only update one row...
        """
        if len(where) != 1:
            return exception_during_call(info=f"db.update_table passed 'where' dict with more than one key")
        table_class = self.table_string_to_class(table)
        ret = []
        with self.db_session() as session:
            try:
                instance = session.query(table_class).filter_by(**where).one()
            except NoResultFound:
                return [unsuccessful_result(method="db.update_date", info=f"Cannot update {table_class} with this query: {where} because NOT found")]
            except MultipleResultsFound:
                return [unsuccessful_result(method="db.update_table", info=f"Cannot update {table_class} with this idnumber: {where['idnumber']} because multiple results found")]
            except sqlalchemy.exc.IntegrityError:
                return [unsuccessful_result(method="db.update_table", info=f"Cannot update {table_class} with this idnumber: {where['idnumber']} because of an integrity error (it has to be unique but there is already someone in there)")]
            for key in kwargs:
                setattr(instance, key, kwargs[key])
                where_key = list(where.keys())[0]
                ret.append(
                    successful_result(method="db.update_table", 
                        info="update {0.__tablename__} set {1} = {2} where {3} = {4}".format(
                            table_class, key, kwargs[key], where_key, where[where_key]
                        )
                    )
                )
            session.add(instance)
        return ret

    def set_username_from_idnumber(self, idnumber, username):
        self.update_table('user', where={'idnumber':idnumber}, username=username)

    def get_user_from_idnumber(self, idnumber):
        with self.db_session() as session:
            try:
                ret = session.query(User).filter(User.idnumber == idnumber).one()
            except MultipleResultsFound:
                self.logger.critical("More than one user with this idnumber: {}".format(idnumber))
                ret = None
            except NoResultFound:
                ret = None
        return ret

    def get_course_from_idnumber(self, idnumber):
        with self.db_session() as session:
            try:
                ret = session.query(Course).filter(Course.shortname == idnumber).one()
            except MultipleResultsFound:
                self.logger.critical("More than one course with this idnumber: {}".format(idnumber))
                ret = None
            except NoResultFound:
                ret = None
        return ret

    def get_user_from_username(self, username):
        """
        Return None if not present
        """
        with self.db_session() as session:
            try:
                ret = session.query(User).filter(User.username == username).one()
            except NoResultFound:
                return None
            except MultipleResultsFound:
                raise    # not possible, because username has to be unique
        return ret

    def set_user_idnumber_from_username(self, username, idnumber):
        with self.db_session() as session:
            ret = session.query(User).filter(User.username == username).one()
            ret.idnumber = idnumber

    def change_user_username(self, old_username, new_username):
        with self.db_session() as session:
            ret = session.query(User).filter(User.username == old_username).one()
            ret.username = new_username

    def get_column_from_row(self, table, column, **kwargs):
        table_class = self.table_string_to_class(table)
        with self.db_session() as session:
            try:
                result = session.query(table_class).filter_by(**kwargs).one()
            except NoResultFound:
                result = None
        if not result:
            return None
        return getattr(result, column)

    def get_list_of_attributes(self, table, attr):
        """
        """
        table_class = self.table_string_to_class(table)
        with self.db_session() as session:
            instance = session.query(table_class)
        return [getattr(obj, attr) for obj in instance.all()]

    def parse_user(self, user):
        if isinstance(user, str):
            # passed an idnumber, so let's get the object
            return self.get_user_from_idnumber(user)
        return user

    def get_online_portfolios(self):
        with self.db_session() as session:
            statement = session.query(Course).filter(Course.idnumber.startswith('OLP:'))

        for row in statement.all():
            yield re.sub(r'^OLP:', '', row.idnumber)

    def get_user_custom_profile_field(self, user, field_name):
        """
        @param user can be an object or just the idnumber
        @return the value of the custom profile object
        """
        user = self.parse_user(user)
        with self.db_session() as session:
            statement = session.query(UserInfoDatum).\
                join(UserInfoField, UserInfoField.id == UserInfoDatum.fieldid).\
                    filter(and_(
                        UserInfoField.shortname == field_name,
                        UserInfoDatum.userid == user.id
                        )
                    )
            try:
                ret = statement.one()
            except MultipleResultsFound:
                self.logger.warning("Multiple fields for {0.username} and {1}; using first() ".format(user, field_name))
                ret = statement.first()
        return ret

class MoodleInterface(MoodleInter):
    """
    Higher-level convenience routines that handles sessions, transactions, queries
    The difference between high-level and low-level may be up to this programmer's imagination :)
    But basically, anything obviously 'dragonnet-y' is here
    """
    SYSTEM_CONTEXT = 1
    MRBS_EDITOR_ROLE = 10
    CONTEXT_USER = 30   #  user-level context
    TEACHING_LEARNING_CATEGORY_ID = ssis_synctree_settings['SSIS_DB']['db_tl_cat_id']

    def __init__(self, *args, **kwargs):
        """
        Ensure that certain cohorts are already established in the database
        """
        super().__init__(*args, **kwargs)

        with self.db_session() as session:
            needed_cohorts = ['teachersALL', 'parentsALL', 'studentsALL', 'supportstaffALL']
            for cohort in needed_cohorts:
                exists = session.query(Cohort).filter_by(idnumber=cohort).all()
                if not exists:
                    self.add_cohort(cohort, cohort)

    def users_enrolled_in_this_cohort(self, cohort):
        """
        Returns users in this cohort
        @param cohort should be the cohort idnumber
        """
        with self.db_session() as session:
            all_users = session.query(User).\
                select_from(CohortMember).\
                    join(Cohort, Cohort.id == CohortMember.cohortid).\
                    join(User, User.id == CohortMember.userid).\
                        filter(
                            and_(
                                    Cohort.idnumber == cohort, 
                                    User.deleted == 0, 
                                    User.idnumber != ''
                                )
                        )
            yield from all_users.all()

    def import_parents_with_links(self, cohort='parentsALL'):
        """
        Imports users in 'cohort' and return any links, if present
        FIXME: Ensure that returns even if no link?
        """
        with self.db_session() as session:
            Student = aliased(User)
            imported_ = session.query(User, Student).\
                select_from(CohortMember).\
                    outerjoin(Cohort, Cohort.id == CohortMember.cohortid).\
                    outerjoin(User, User.id == CohortMember.userid).\
                    outerjoin(RoleAssignment, RoleAssignment.userid == User.id).\
                    outerjoin(Role, Role.id == RoleAssignment.roleid).\
                    outerjoin(Context,
                        and_(
                            Context.id == RoleAssignment.contextid,
                            Context.contextlevel == self.CONTEXT_USER
                        )).\
                    outerjoin(Student, Student.id == Context.instanceid).\
                    filter(
                        and_(
                            Cohort.idnumber == cohort,
                            Role.shortname == 'parent',
                            User.deleted==0,
                            User.idnumber!= '',
                            Student.idnumber!='',
                            Student.deleted==0)
                    )
        yield from imported_.all()

    def import_students_with_links(self, cohort='studentsALL'):
        """
        Imports users in 'cohort' and return any links, if present
        FIXME: Ensure that returns even if no link?
        """
        with self.db_session() as session:
            Student = aliased(User)
            imported_ = session.query(Student, User).\
                select_from(User).\
                    join(RoleAssignment, RoleAssignment.userid == User.id).\
                    join(Role, Role.id == RoleAssignment.roleid).\
                    join(Context,
                        and_(
                            Context.id == RoleAssignment.contextid,
                            Context.contextlevel == self.CONTEXT_USER
                        )).\
                    join(Student, Student.id == Context.instanceid).\
                    filter(
                        and_(
                            Cohort.idnumber == cohort,
                            Role.shortname == 'parent',
                            Student.deleted==0,
                            Student.idnumber!='',
                            User.idnumber!='',
                            User.deleted==0)
                    )
        yield from imported_.all()

    def get_cohorts_for_user(self, idnumber):
        with self.db_session() as session:
            statement = session.query(Cohort.idnumber).\
                select_from(User).\
                    join(CohortMember, CohortMember.userid == User.id).\
                    join(Cohort, Cohort.id == CohortMember.cohortid).\
                filter(User.idnumber == idnumber)
        yield from [s[0] for s in statement.all()]

    def get_parent_student_links(self):
        with self.db_session() as session:
            Child = aliased(User)
            statement = session.\
                query(User.idnumber, Child.idnumber).\
                select_from(User).\
                join(RoleAssignment, RoleAssignment.userid == User.id).\
                join(Role, Role.id == RoleAssignment.roleid).\
                join(Context,
                    and_(
                        Context.id == RoleAssignment.contextid,
                        Context.contextlevel == 30
                    )).\
                join(Child, Child.id == Context.instanceid).\
                filter(and_(
                        Role.shortname == 'parent',
                        User.deleted==0),
                        User.idnumber!='',
                        Child.idnumber!='',
                    ).\
                order_by(User.idnumber)
        for item in statement.all():
            yield item

    def users_enrolled_in_these_cohorts(self, cohort):
        """
        Returns users
        @param cohort must be an iterator
        TODO: Do I need to process for repeats?
        """
        or_portion = [Cohort.idnumber == c for c in cohort]
        with self.db_session() as session:
            all_users = session.query(User)\
                .select_from(CohortMember).\
                    join(Cohort, Cohort.id == CohortMember.cohortid).\
                    join(User, User.id == CohortMember.userid).\
                        filter(
                            or_(
                                *or_portion
                            ),
                        )
            for item in all_users.all():
                yield item

    def add_cohort(self, idnumber, name):
        exists = self.get_rows_in_table('cohort', idnumber=idnumber)
        if exists:
            self.default_logger('Did NOT create cohort {} as it already exists!'.format(idnumber))
            return
        now = time_now()

        with self.db_session() as session:
            cohort = Cohort()
            cohort.idnumber = idnumber
            cohort.name = name
            cohort.descriptionformat = 0
            cohort.description = ''
            cohort.contextid = self.SYSTEM_CONTEXT
            cohort.source="psmdlsyncer"
            cohort.timecreated = time_now()
            cohort.timemodified = time_now()
            session.add(cohort)

    def get_user_enrollments(self):

        with self.db_session() as session:
            enrollments = session.query(
                User.idnumber,
                Enrol.enrol,
                Course.idnumber
            ).select_from(UserEnrolment).\
                join(User, User.id == UserEnrolment.userid).\
                join(Enrol, Enrol.id == UserEnrolment.enrolid).\
                join(Course, Course.id == Enrol.courseid).\
            filter(
                and_(
                    Enrol.enrol == 'manual',
                )
            )

        yield from enrollments.all()


    def bell_schedule(self):
        """
        Query that represents the schedule, using Moodle's terms
        Sorted using order by Role.name ASC because
        we need the order to be in Teacher, Parent, Student
        because teacher info needed to complete the group
        TODO: Figure out how to get specific ordering from SQL
              and then incorporate Manager status too
        """

        with self.db_session() as session:

            # FIXME What to do about cases where they are not in a group but also don't want duplicates?
            schedule = session.query(Course.idnumber.label("courseID"), 
                        User.idnumber.label("userID"), 
                        User.username.label('username'), 
                        Role.shortname.label('rolename'), 
                        Group.idnumber.label('groupIdNumber'), 
                        Group.name.label('groupName')
                    ).select_from(Course).\
                        join(CourseCategory, CourseCategory.id == Course.category).\
                        join(Context, Course.id == Context.instanceid).\
                        join(RoleAssignment, RoleAssignment.contextid == Context.id).\
                        join(User, User.id == RoleAssignment.userid).\
                        join(Role, Role.id == RoleAssignment.roleid).\
                        outerjoin(GroupsMember, GroupsMember.userid == User.id).\
                        outerjoin(Group, and_(
                            Group.id == GroupsMember.groupid,
                            Group.courseid == Course.id
                            )).\
                        filter(
                            and_(
                                #CourseCategory.path == ('/{}'.format(self.TEACHING_LEARNING_CATEGORY_ID)),   # TODO: get roleid on __init__
                                CourseCategory.path.like('/{}/%'.format(self.TEACHING_LEARNING_CATEGORY_ID)),   # TODO: get roleid on __init__
                                Course.idnumber != '',
                                User.idnumber != '',
                                User.deleted == 0
                            )).\
                        order_by(asc(Role.id))   # sort by role.id because it's in the natural order expected (teachers first, then students, then parents)

            for item in schedule.all():
                yield item

    def get_bell_schedule(self):
        """
        Makes a generator that outputs basically outputs SSIS' bell schedule
        First does an SQL statement to get the raw data, and then processes it in python
        to get the expected output.
        (Getting it done in pure sql with nested selects was just a bit too tedius)
        """
        results = defaultdict(lambda : defaultdict(list))
        for row in self.bell_schedule():
            _period = ''
            courseID, userID, username, roleName, groupId, groupName = row
            if not groupId:
                continue

            # Do different things based on the role
            # For teachers, we have to see if they are the owner of the group

            if roleName == "editingteacher":
                # TODO: Can be deleted, right?
                # if not groupId:
                #     groupId = username + courseID
                results[groupId]['course'] = courseID

                # Most probably, there will only be one teacher in this group
                # But hard-coding it as one object seems wrong, so use a list
                # FIXME: If teachers were to be manaully put into a group
                #        that isn't their own group, we have some trouble
                #        There isn't any reason for them to do that
                #        But we should probably close that off
                #        (Maybe look at the username before adding here?)
                results[groupId]['teachers'].append(userID)

            elif roleName == "manager":
                # what do we do in this case?
                continue

            elif roleName == "student":
                if userID.endswith('P'):
                    # Ensure there are no parents mistakenly being put
                    # TODO: Unenrol them?
                    continue

                if not groupId:
                    #TODO: Figure out why the SQL query returns so many blank groups
                    continue

                if not userID in results[groupId]['students']:
                    results[groupId]['students'].append(userID)

            elif roleName == "parent":
                # The below will work okay because we sorted the query by name
                # and Teacher comes before Parent
                # a bit of a workaround, but it should work okay
                if not groupId:
                    #TODO: Figure out why the SQL query returns so many blank groups
                    continue

                if '-' in groupId:
                    section = groupId.split('-')[1]
                else:
                    section = ''
                    #self.logger.warning("Found when processing parent, moodle group {} does not have a section number attached, so much be illigitmate".format(groupId))
                    # TODO: we should indicate the enrollment by yielding what we can
                    #continue

                teachers = results[groupId]['teachers']
                course = results[groupId]['course']
                if teachers and course:

                    for teacher in teachers:
                        yield {
                            'shortcode':course, 
                            'period': _period,
                            'section': section,
                            'student_idnumber': userID, 
                            'staff_idnumber': teacher, 
                            'group': groupId
                        }

            else:
                # non-editing teachers...
                pass

        for group in results.keys():
            if '-' in group:
                section = group.split('-')[1]
            else:
                section = ''
                # self.logger.warning("Moodle group {} does not have a section number attached, so much be illigitmate".format(group))
                # continue
            teachers = results[group]['teachers']
            course = results[group]['course']
            if course and not teachers:
                #self.logger.warning("Group with no teacher info: {}!".format(group))
                continue
            elif not course:
                #self.logger.warning("No course {} in group?: {}!".format(str(course), group))
                continue

            for student in results[group]['students']:
                for teacher in teachers:  # note: there will only be one teacher...
                    yield {
                        'shortcode': course, 
                        'period': _period, 
                        'section': section, 
                        'student_idnumber':student,
                        'staff_idnumber': teacher,
                        'group': group
                    }

    def get_mrbs_editors(self):
        with self.db_session() as session:
            statement = session.query(User).\
                select_from(RoleAssignment).\
                    join(User, RoleAssignment.userid == User.id).\
                        filter(
                            and_(
                                RoleAssignment.contextid == self.SYSTEM_CONTEXT,
                                RoleAssignment.roleid == self.MRBS_EDITOR_ROLE,
                                not_(User.idnumber.like(''))
                            )
                        )
        for item in statement.all():
            yield item

    def add_mrbs_editor(self, user_idnumber):
        user = self.wrap_no_result(self.get_user_from_idnumber, user_idnumber)
        if not user:
            # no such user, don't do it!
            return

        now = time_now()
        self.insert_table(
            'role_assignments',
            contextid=self.SYSTEM_CONTEXT,
            roleid=self.MRBS_EDITOR_ROLE,
            userid=user.id,
            modifierid=2, # TODO: Admin ID, right?
            component='psmdlsyncer',  # Might as well use it for something?
            itemid=0,
            sortorder=0,
            timemodified=now)

    def get_user_schoolid(self, user):
        obj = self.get_user_custom_profile_field(user, 'schoolid')
        if not obj:
            return None
        return obj.data

    def get_timetable_table(self):
        with self.db_session() as session:
            statement = session.query(SsisTimetableInfo, User.idnumber).\
                join(User, User.id == SsisTimetableInfo.studentuserid)
        for item in statement.all():
            yield item

    def get_course_metadata(self):
        with self.db_session() as session:
            statement = session.query(
                Course.idnumber.label('course_idnumber'),
                CourseSsisMetadatum.value.label('course_grade')).\
            select_from(CourseSsisMetadatum).\
            join(Course, Course.id == CourseSsisMetadatum.courseid).\
            filter(CourseSsisMetadatum.field.like('grade%')).\
            order_by(Course.idnumber, CourseSsisMetadatum.value)

        for item in statement.all():
            yield item

    def add_course_metadata(self, course_metadata):
        with self.db_session() as session:
            try:
                course = session.query(Course).filter_by(idnumber=course_metadata.course_idnumber).one()
            except NoResultFound:
                self.default_logger("No course by idnumber when adding metadata {}".format(course_metadata.course_idnumber))
                return
            except MultipleResultsFound:
                self.logger.warning("Multiple courses with idnumber {}".format(course_metadata.course_idnumber))
                return

            for i in range(len(course_metadata.course_grade)):
                grade = course_metadata.course_grade[i]
                grade_str = "grade{}".format(i+1)
                new = CourseSsisMetadatum()
                new.courseid = course.id
                setattr(new, 'field', grade_str)
                setattr(new, 'value', grade)

                exists = session.query(CourseSsisMetadatum).filter_by(
                    courseid=course.id,
                    field=grade_str,
                    value=grade
                    ).all()
                if exists:
                    self.logger.default_logger('Course Metadata already exists')
                    continue
                session.add(new)

    def get_teaching_learning_courses(self):
        """
        Returns course information for any course that is within the Teaching & Learning menu
        """

        with self.db_session() as session:
            statement = session.query(Course.idnumber, Course.fullname, Course.id.label('database_id')).\
                join(CourseCategory, CourseCategory.id == Course.category).\
                    filter(
                        and_(
                            Course.idnumber!='',
                            # CourseCategory.path.like('/{}/%'.format(self.TEACHING_LEARNING_CATEGORY_ID)),
                            # Remove this limitation, since there really is no point to it anymore
                            # FIXME: This query can be restructured
                        )).\
                order_by(Course.id)

        for item in statement.all():
            yield item

    def get_teaching_learning_courses_with_grades_subquery(self):
        """
        Returns course information for any course that is within the Teaching & Learning menu
        Including the grade info stored in course_ssis_metadata
        Grade info is a string, if there are more than two then is in 11,12 format
        TODO: Sometimes it formats as 12/11, make it sort (but if you sort you have to put in group_by)
              Workaround: the model just sorts it for us

        Left in for posperity, because it illustrates a concrete example of a subquery
        """

        with self.db_session() as session:
            sub = session.query(
                Course.id.label('course_id'),
                func.string_agg(CourseSsisMetadatum.value, ',').label('grade')).\
                select_from(Course).\
                    join(CourseCategory, CourseCategory.id == Course.category).\
                    filter(and_(
                        not_(Course.idnumber == ''),
                        #CourseCategory.path == '/{}'.format(self.TEACHING_LEARNING_CATEGORY_ID)
                        CourseCategory.path.like('/{}/%'.format(self.TEACHING_LEARNING_CATEGORY_ID))
                        )).\
                    group_by(Course.id).\
                    subquery()

            statement = session.query(Course.idnumber, Course.fullname, sub.c.grade, Course.id.label('database_id')).\
                join(sub, Course.id == sub.c.course_id).\
                    order_by(Course.id)

        for item in statement.all():
            yield item

    def report_teaching_learning_courses(self):
        """
        Returns course information for any course that is within the Teaching & Learning menu
        Including the grade info stored in course_ssis_metadata
        Grade info is a string, if there are more than two then is in 11,12 format
        TODO: Sometimes it formats as 12/11, make it sort (but if you sort you have to put in group_by)
              Workaround: the model just sorts it for us
        """

        with self.db_session() as session:
            sub = session.query(
                Course.id.label('course_id'),
                CourseCategory.id.label('cat_id'),
                CourseCategory.name.label('cat_name'),
                CourseCategory.path.label('cat_path')
                ).\
                select_from(Course).\
                    join(CourseCategory, CourseCategory.id == Course.category).\
                    filter(and_(
                        not_(Course.idnumber == ''),
                        #CourseCategory.path == '/{}'.format(self.TEACHING_LEARNING_CATEGORY_ID)
                        CourseCategory.path.like('/{}/%'.format(self.TEACHING_LEARNING_CATEGORY_ID))
                        )).\
                    group_by(Course.id, CourseCategory.id).\
                    subquery()

            statement = session.query(Course.idnumber, Course.fullname, sub.c.cat_name, sub.c.cat_path, Course.id.label('database_id')).\
                join(sub, Course.id == sub.c.course_id).\
                    order_by(Course.id)

        for item in statement.all():
            yield item

    def get_custom_profile_records(self):
        with self.db_session() as session:
            statement = session.\
                query(User.idnumber, User.username, UserInfoField.shortname, UserInfoDatum.data).\
                    select_from(UserInfoDatum).\
                join(UserInfoField, UserInfoField.id == UserInfoDatum.fieldid).\
                join(User, User.id == UserInfoDatum.userid)
        for item in statement.all():
            yield item

    def get_custom_profile_fields(self):
        """
        Returns just the data in user_info_fields
        """
        with self.db_session() as session:
            statement = session.\
                query(UserInfoField)
        for item in statement.all():
            yield item

    def set_user_custom_profile(self, user_idnumber, name, value):
        user = self.get_user_from_idnumber(user_idnumber)
        if not user:
            self.logger.warning("Custom profile field for a user was requested, but no such user:".format(user_idnumber))
            return  # some error, right?
        userid = user.id

        fieldid = self.get_column_from_row('user_info_field', 'id', shortname=name)

        if not fieldid:
            return

        self.update_table('user_info_data', where=dict(
            userid=userid,
            fieldid=fieldid
            ),
            data=value
            )

    def make_new_custom_profile_field(self, name):
        """
        Do database stuff to create the custom user profile field
        """
        with self.db_session() as session:
            exists = session.query(UserInfoField).filter(UserInfoField.name == name).all()
            if exists:
                return

            result = session.query(UserInfoField.sortorder).order_by(desc(UserInfoField.sortorder)).limit(1).first()
            if not result:
                lastsort = 0
            else:
                lastsort = int(result.sortorder)

            sort = lastsort + 1
            user_info_field = UserInfoField()
            user_info_field.shortname = name
            user_info_field.name = name.replace("_", " ").title()
            user_info_field.description = ""
            user_info_field.descriptionformat = 1
            user_info_field.categoryid = 1
            user_info_field.sortorder = sort
            user_info_field.required = 0
            user_info_field.locked = 1
            user_info_field.visible = 0
            user_info_field.forceunique = 0
            user_info_field.signup = 0
            user_info_field.defaultdata = 0
            user_info_field.defaultdataformat = 0
            user_info_field.param1 = "psmdlsyncer"  # for debugging...
            user_info_field.param2 = ""
            user_info_field.param3 = ""
            user_info_field.param4 = ""
            user_info_field.param5 = ""

            if name.startswith('is'):
                user_info_field.datatype = "checkbox"
            else:
                # for everything...?
                user_info_field.datatype = "text"

            session.add(user_info_field)

    def add_user_custom_profile(self, user_idnumber, name, value):
        """
        """
        user = self.wrap_no_result(self.get_user_from_idnumber, user_idnumber)
        if not user:
            return
        user_id = user.id  # needed later

        with self.db_session() as session:
            try:
                field = session.query(UserInfoField).filter_by(shortname=name).one()  # shortname == idnumber
            except NoResultFound:
                self.logger.info("User has a custom profile field {} but it doesn't exist yet".format(name))
                return
            except MultipleResultsFound:
                self.logger.info("Multiple, using first (again)")
                field = session.query(UserInfoField).filter_by(shortname=name).first()

            exists = session.query(UserInfoDatum).filter_by(fieldid=field.id, userid=user_id).all()
            if exists:
                self.default_logger("Not creating entry for field {} for user {} because it already exists!".format(name, user_idnumber))
                return
            # check for multiples?
            user_info = UserInfoDatum()
            user_info.userid = user_id
            user_info.fieldid = field.id
            if field.datatype == 'checkbox':
                user_info.data = int(value)
            else:
                user_info.data = value
            user_info.dateformat = 0
            session.add(user_info)

    def get_cohorts(self):
        """
        First return cohorts without member info, then with user info
        """
        with self.db_session() as session:
            statement = session.query(Cohort).filter(Cohort.idnumber != '')
            for cohort in statement.all():
                yield (None, cohort.idnumber)

        with self.db_session() as session:
            statement = session.query(User.idnumber, Cohort.idnumber).\
                select_from(CohortMember).\
                    join(Cohort, Cohort.id == CohortMember.cohortid).\
                    join(User, User.id == CohortMember.userid).\
                filter(
                    and_(
                            User.deleted == 0, 
                            User.idnumber != '',
                            Cohort.idnumber != '',
                        )
                )
            yield from statement.all()

    def get_groups(self):
        with self.db_session() as session:
            statement = session.query(Group.id, Group.idnumber, Group.name, Course.idnumber, User.idnumber).\
                select_from(GroupsMember).\
                    join(Group, GroupsMember.groupid == Group.id).\
                    join(Course, Course.id == Group.courseid).\
                    outerjoin(User, GroupsMember.userid == User.id)
        return statement.all()

    def get_all_groups(self):
        """
        Get all groups
        """
        with self.db_session() as session:
            statement = session.query(Group, Course).\
                select_from(Group).\
                    join(Course, Course.id == Group.courseid)
        return statement.all()

    def clear_active_timetable_data(self):
        with self.db_session() as session:
            statement = session.query(SsisTimetableInfo)
            for row in statement.all():
                row.active = 0

    def get_timetable_data(self, active_only=True):
        with self.db_session() as session:
            Teacher = aliased(User)
            Student = aliased(User)
            statement = session.query(
                SsisTimetableInfo.id,
                Course.idnumber.label('course_idnumber'),
                Teacher.idnumber.label('teacher_idnumber'),
                Student.idnumber.label('student_idnumber'),
                SsisTimetableInfo.name,
                SsisTimetableInfo.period,
                SsisTimetableInfo.comment,
                SsisTimetableInfo.active
                ).\
            select_from(SsisTimetableInfo).\
                join(Course, Course.id == SsisTimetableInfo.courseid).\
                join(Teacher, Teacher.id == SsisTimetableInfo.teacheruserid).\
                join(Student, Student.id == SsisTimetableInfo.studentuserid)
            if active_only:
                statement = statement.filter(SsisTimetableInfo.active == 1)
        return statement.all()

    def set_timetable_data_inactive(self, timetable):
        with self.db_session() as session:
            ns = Namespace()
            try:
                ns.courseid = session.query(Course).filter_by(shortname=timetable.course.idnumber).one().id
                ns.studentuserid = session.query(User).filter_by(idnumber=timetable.student.idnumber).one().id
                ns.teacheruserid = session.query(User).filter_by(idnumber=timetable.teacher.idnumber).one().id
            except NoResultFound:
                self.logger.warning('No results found for timetable object when setting to inactive {}'.format(timetable))
            except MultipleResultsFound:
                self.logger.warning('Multiple results found for timetable object {}'.format(timetable))
                return
            ns.name = timetable.group.idnumber
            exist = session.query(SsisTimetableInfo).\
                filter_by(
                    **ns.kwargs
                    ).all()

            for row in exist:
                row.active = 0


    def add_timetable_data(self, timetable):
        with self.db_session() as session:
            ns = Namespace()
            ns.courseid, ns.studentuserid, ns.teacheruserid = (None, None, None)
            try:
                ns.courseid = session.query(Course).filter_by(shortname=timetable.course.idnumber).one().id
                ns.studentuserid = session.query(User).filter_by(idnumber=timetable.student.idnumber).one().id
                ns.teacheruserid = session.query(User).filter_by(idnumber=timetable.teacher.idnumber).one().id
            except NoResultFound:
                if ns.courseid:
                    self.logger.debug('No results found for timetable object when adding {}'.format(timetable))
                return
            except MultipleResultsFound:
                self.logger.warning('Multiple results found for timetable object {}'.format(timetable))
                return
            ns.name = timetable.group.idnumber
            ns.period = timetable.period_info
            ns.grade = timetable.course.convert_grade()

            exist = False
            try:
                exist = session.query(SsisTimetableInfo).filter_by(**ns.kwargs).one()
            except NoResultFound:
                pass

            if exist:                
                if not exist.active:
                    self.logger.warning('Timetable {} was inactive, setting to active'.format(timetable))
                    exist.active = 1
                else:
                    self.logger.warning("Timetable {} already exists!".format(timetable))

            else:
                new = SsisTimetableInfo()
                for key in ns.kwargs:
                    setattr(new, key, getattr(ns, key))
                new.comment = timetable.group.section
                new.active = 1

                session.add(new)

    def set_timetable_data_active(self, timetable):
        # TODO: Figure this out so that I'm not repeating code...
        with self.db_session() as session:
            ns = Namespace()
            try:
                ns.courseid = session.query(Course).filter_by(shortname=timetable.course).one().id
                ns.studentuserid = session.query(User).filter_by(idnumber=timetable.student).one().id
                ns.teacheruserid = session.query(User).filter_by(idnumber=timetable.teacher).one().id
            except NoResultFound:
                self.logger.warning('No results found for timetable object when setting to active {}'.format(timetable))
                return
            except MultipleResultsFound:
                self.logger.warning('Multiple results found for timetable object {}'.format(timetable))
                return
            ns.name = timetable.group.idnumber
            ns.period = timetable.period_info

            this = session.query(SsisTimetableInfo).\
                filter_by(
                    **ns.kwargs
                    ).one()
            this.active = 1

    def undelete_user(self, user):
        with self.db_session() as session:
            this_user = session.query(User).filter_by(idnumber=user.idnumber).one()
            this_user.deleted = 0

