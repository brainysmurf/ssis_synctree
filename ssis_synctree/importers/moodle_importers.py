from synctree.importers.db_importer import PostgresDBImporter
from ssis_synctree.moodle.MoodleInterface import MoodleInterface
import ssis_synctree_settings
from collections import defaultdict


class MoodleImporter(PostgresDBImporter, MoodleInterface):
    _settings = ssis_synctree_settings['SSIS_DB']

    def reader(self):
        """
        """
        return []


class MoodleStudentsImporter(MoodleImporter):

    def reader(self):
        """
        Link to parents is because autosend has it too
        """

        # First get the basic details
        # Not doing this first can result in inter-dependency
        students = self.users_enrolled_in_this_cohort('studentsALL')
        for student in students:
            yield {
                'idnumber': student.idnumber, 
                'firstname': student.firstname, 
                'lastname': student.lastname,
                'email': student.email,
                'auth': student.auth,
                'username': student.username,
                'homeroom': student.department,
                'parents': [],
                '_deleted': student.deleted
            }

        # Create the links to parents
        users = self.import_students_with_links('studentsALL')
        for student, parent in users:
            if student.idnumber.endswith('P'):
                # TODO: Change this to filter in MoodleInterface.import_students_with_links
                continue
            yield {
                'idnumber':student.idnumber, 
                'parents': [parent.idnumber],
            }


class MoodleParentsImporter(MoodleImporter):

    def reader(self):
        # Build cohort information to be used below

        parents = self.users_enrolled_in_this_cohort('parentsALL')
        for parent in parents:
            yield {
                'idnumber': parent.idnumber, 
                'firstname': parent.firstname, 
                'lastname': parent.lastname,
                'auth': parent.auth,
                'username': parent.username,
                'email': parent.email,
                'homeroom': parent.department,
            }


class MoodleStaffImporter(MoodleImporter):
    def reader(self):

        mrbs_editors = [u.idnumber for u in self.get_mrbs_editors()]

        for cohort in ['teachersALL', 'supportstaffALL']:
            for user in self.users_enrolled_in_this_cohort(cohort):
                yield {
                    'idnumber': user.idnumber,
                    'firstname': user.firstname,
                    'lastname':user.lastname,
                    'username':user.username,
                    'email': user.email,
                    'auth': user.auth,
                    'mrbs_editor': user.idnumber in mrbs_editors
                }


class MoodleParentsChildLinkImporter(MoodleImporter):
    def resolve_duplicate(self, obj, **kwargs):
        if obj._kwargs != kwargs:
            print("MoodleParentsChildLinkImporter Duplicate with different info: {}".format(obj))
        return kwargs

    def reader(self):
        users = self.import_parents_with_links('parentsALL')
        for parent, student in users:
            yield {
                'idnumber': student.idnumber,
                'links': set([parent.idnumber])
            }
            yield {
                'idnumber': parent.idnumber,
                'links': set([student.idnumber])
            }


class MoodleCohortsImporter(MoodleImporter):

    def reader(self):
        for user_idnumber, cohort_idnumber in self.get_cohorts():
            if user_idnumber is None:
                # yield an empty membership, working around issue  FIXME: Or have get_cohorts() return despite no user
                yield {
                    'idnumber': cohort_idnumber,
                    'members': []
                }
            else:
                user = self._branch.get_from_subbranches(user_idnumber, ['students', 'staff', 'parents'])
                if not user:
                    continue
                yield {
                    'idnumber': cohort_idnumber,
                    'members': [user_idnumber],
                }


class MoodleScheduleImporter(MoodleImporter):
    """
    This is just a placeholder. We read the enrollments below using this information
    """ 
    def reader(self):
        for schedule in self.bell_schedule():
            course, idnumber, username, role, group, group_name = schedule
            user = self._branch.get_from_subbranches(
                idnumber,
                ['students', 'staff', 'parents']
            )

            yield {
                'user_idnumber': idnumber,
                'course': course,
                'group': group,
                'role': role
            }


class MoodleCoursesImporter(MoodleImporter):
    def reader(self):   
        for item in self.get_teaching_learning_courses():
            yield {
                'idnumber': item.idnumber,
                'moodle_shortcode': item.idnumber,
                'name': item.fullname,
                '_dbid': item.database_id
            }


class MoodleGroupsImporter(MoodleImporter):

    def kwargs_preprocessor(self, kwargs_in):
        # Pattern must match expected group
        if len(kwargs_in['idnumber'].split('-')) == 4:
            return kwargs_in
        return None

    def reader(self):
        for group_id, group_idnumber, group_name, course_idnumber, user_idnumber in self.get_groups():
            if '-' in group_idnumber:
                split = group_idnumber.split('-')
                if len(split) == 4:
                    grade = split[-2]
                elif len(split) == 3:
                    # may not have been migrated yet
                    grade = ''
                else:
                    grade = ''
                teacher = split[0]
                section = split[-1]
            else:
                section = ''
                grade = ''
                teacher = ''

            if not group_idnumber:
                # Manual groups can be created without idnumber, in which case we should just move on
                continue

            yield {
                'idnumber': group_idnumber,
                'name': group_name,
                'grade': grade,
                'section': section,
                '_short_code': '',
                '_id': group_id,
                'course': course_idnumber,
                'members': set([user_idnumber])
            }

        # This will get groups that do not have a member, but what about those that already do?
        for group, course in self.get_all_groups():
            if not group.idnumber:
                continue

            if '-' in group.idnumber:
                split = group.idnumber.split('-') 
                section = group.idnumber.split('-')[-1]
                if len(split) == 4:
                    grade = split[-2]
                else:
                    grade = ''
            else:
                section = ''

            yield {
                'idnumber': group.idnumber,
                'grade': grade,
                'section': section,
                'course': course.idnumber,
                '_id': group.id,
                'members': set()
            }


class MoodleEnrollmentsImporter(MoodleImporter):

    def reader(self):
        """

        TODO: This is wrong, maybe just do another SQL 

        """
        for schedule in self._branch.schedule.get_objects():
            user_idnumber = schedule.user_idnumber
            course = schedule.course
            group = schedule.group
            role = schedule.role

            # And ignore any enrollment that doesn't have predefined roles

            if not role in ['student', 'parent', 'editingteacher']:
                continue

            yield {
                'idnumber': user_idnumber,
                'courses': [course],
                'groups': ['' if group is None else group],
                'roles': [role]
            }


