from synctree.importers.db_importer import PostgresDBImporter
from ssis_synctree.moodle.MoodleInterface import MoodleInterface

from synctree.templates import DefaultTemplate, LoggerTemplate, LoggerReporter

from ssis_synctree.moodle.php import PHP

from synctree.results import \
    dropped_action, \
    unsuccessful_result, \
    successful_result

import ssis_synctree_settings

try:
    import hues
except ImportError:
    pass  # May not be needed, used for tests

from synctree.utils import extend_template_exceptions
from ssis_synctree.utils import is_attached_terminal
from ssis_synctree.utils import DynamicMockIf


class MoodleDB(PostgresDBImporter, MoodleInterface):
    _settings = ssis_synctree_settings['SSIS_DB']

    def __init__(self):
        """
        We don't need branch and/or tree, so override this to compensate.
        (Also doesn't do check for cohorts)
        FIXME: Refactor to make more sense!
        """
        self.init()


def mocked_return(*args, **kwargs):
    return successful_result(method="Mocked: " + str(args), info=str(kwargs))


class MoodleTemplate(DefaultTemplate):

    user_column_map = {'homeroom': 'department'}  # User column mapping
    _exceptions = extend_template_exceptions('user_column_map php moodledb courses users')
    _mock = False

    def __init__(self):
        """
        Sets up state so that we guarantee that things won't be re-created once we have them
        """
        super().__init__()
        self.moodledb = DynamicMockIf(self._mock, mocked_return, methods=['update_table'])(MoodleDB)()
        self.php = DynamicMockIf(self._mock, mocked_return, methods=['command'])(PHP)()
        self.courses = []
        self.groups = []
        self.users = {}
        for course in [c for c in self.moodledb.get_rows_in_table('courses') if c.idnumber]:
            self.courses.append(course.idnumber)
        for group in [c for c in self.moodledb.get_rows_in_table('groups') if c.idnumber]:
            self.groups.append(group.idnumber)
        for user in [c for c in self.moodledb.get_rows_in_table('users') if c.idnumber]:
            self.users[user.idnumber] = bool(user.deleted)


class MoodleFirstRunTemplate(MoodleTemplate):
    """
    Implements initial account creations and creates groups as needed
    Seperated out this way so that in the consecutive run we can ensure that we everything is already set up properly for enrollments
    """
    def new_users(self, action):
        if not action.idnumber.strip():
            return unsuccessful_result(info='No idnumber?')
        else:
            user = action.source
            ret = []
            if user.idnumber not in self.users:
                # only actually call this if we are sure it's not already there
                ret.append(self.php.create_account(user.username, user.email, user.firstname, user.lastname, user.idnumber))
            else:
                if self.users[user.idnumber]:
                    # It's been deleted, so just change it back
                    ret.append(successful_result(method='new_users', info=f"Found an old, deleted user: {user.idnumber}"))
                    ret.extend(self.moodledb.update_table('users', where={'idnumber':user.idnumber}, deleted=0))
                else:
                    ret.append(dropped_action(method=f"Already exists: {user.name} ({user.idnumber})"))
            for cohort in user._cohorts:
                ret.append(self.php.add_user_to_cohort(user.idnumber, cohort))
            return ret

    def new_parents(self, action):
        ret = []
        pees = {'0': 'P', '1': 'PP'}.get(action.idnumber[-1], None)
        deprecated_idnumber = f"{action.source._family_id}{pees}"
        if pees and deprecated_idnumber in self.users:
            if self.users[deprecated_idnumber]:
                # It has been deleted, undelete it before migrating
                ret.extend(self.moodledb.update_table('users', where={'idnumber': deprecated_idnumber}, deleted=0))

            if action.idnumber in self.users:
                # We already have the normal ID in here, so compensate
                if self.users[action.idnumber]:
                    ret.extend(self.moodledb.update_table('users', where={'idnumber': action.idnumber}, deleted=0))
                # It's already there, but we didn't find it in parentsALL, so add it
                ret.append(self.php.add_user_to_cohort(action.idnumber, 'parentsALL'))
            else:
                # Doesn't already exist, so migrate
                ret.extend(self.moodledb.update_table('users', where={'idnumber': deprecated_idnumber}, idnumber=action.idnumber))

        else:
            ret.extend(self.new_users(action))
        return ret

    def new_staff(self, action):
        """ Convoluted logical structure to reflect a migration """

        existing_username = self.moodledb.get_user_from_username(action.source.username)
        existing_idnumber = self.moodledb.get_user_from_idnumber(action.source.idnumber)

        if existing_username and not existing_idnumber:
            # There is only one account which we can just update directly
            self.moodledb.set_user_idnumber_from_username(
                action.source.username, action.source.idnumber
            )
            return dropped_action(method=f"Updated staff idnumber with id: {existing_username.id}")

        if existing_username:
            # We have to proceed carefully

            if existing_username.idnumber == action.source.username:
                # We have staff account with their email address in the idnumber field
                if existing_idnumber:
                    # There is an account with with the right idnumber
                    if existing_idnumber.id == existing_username.id:
                        # They are the same account, and this is correct, BUT WHY new_staff??
                        return dropped_action(method=f"Why new: {action.source.idnumber}?")
                    else:
                        # Two different accounts that need to be merged
                        return dropped_action(method=f"Merge these: {existing_idnumber.id} and {existing_username.id}")
                else:
                    # There is only one account which we can just update directly
                    self.moodledb.set_user_idnumber_from_username(
                        action.source.username, action.source.idnumber
                    )
                    return dropped_action(method=f"Updated staff idnumber with id: {existing_username.id}")
            else:
                if existing_username.idnumber == action.source.email:
                    return dropped_action(method=f"This looks like the parent account: {action.source.idnumber}")
                else:
                    return dropped_action(method=f"No code path for {action.source.idnumber}")
        else:
            # Nothing with previous username
            if existing_idnumber:
                return dropped_action(f"Why new already one: {action.source.idnumber}!")
            else:
                # 
                # Nothing there yet, proceed as normal
                return self.new_users(action)
                #
        
        return dropped_action(method=f"Huh. No code path for {action.source.idnumber}")

    def new_students(self, action):
        """
        Cascading results
        """
        # prepare = (
        #         (self.new_users, action),  # FIXME: Why do I need self here?
        #         (self.add_members_to_cohorts, action._replace(idnumber='studentsALL', value=action.idnumber)),
        #     )
        # return cascading_result(prepare)
        return self.new_users(action)

    def new_courses(self, action):
        course = action.source
        return self.php.create_new_course(course.idnumber, course.name)

    def new_groups(self, action):
        group_idnumber = action.source.idnumber
        group_name = action.source.name
        course_idnumber = action.source.course
        if course_idnumber not in self.courses:
            return dropped_action(method=f"No course {course_idnumber} in moodle")
        if group_idnumber in self.groups:
            return dropped_action(method=f"Group {group_idnumber} already exists")
        else:
            return self.php.create_group_for_course(course_idnumber, group_idnumber, group_name)

    def new_cohorts(self, action):
        cohort = action.source
        return self.php.new_cohort(cohort.idnumber, cohort.idnumber)

    def new_parents_child_link(self, action):
        ret = []
        parent_idnumber = action.source.idnumber
        for child_idnumber in action.source.links:
            ret.append(self.php.associate_child_to_parent(parent_idnumber, child_idnumber))
        return ret

    def add_cohorts_members_to_moodle(self, action):
        cohort_idnumber = action.idnumber
        user_idnumber = action.value
        return self.php.add_user_to_cohort(user_idnumber, cohort_idnumber)

    def remove_cohorts_members_from_moodle(self, action):
        cohort_idnumber = action.idnumber
        user_idnumber = action.value
        return self.php.remove_user_from_cohort(user_idnumber, cohort_idnumber)


class FullReporter(LoggerReporter):

    def __init__(self):
        self._success = hues.huestr(' S ').white.bg_green.bold.colorized
        self._fail = hues.huestr(' W ').black.bg_yellow.bold.colorized
        self._exception = hues.huestr(' E ').white.bg_red.bold.colorized

    def _reverse(self, x):
        return hues.huestr(f" {x}: ").black.bold.colorized

    def will_start(self):
        super().will_start()
        self.unimplemented = set()

    def finished(self):
        print(sorted(self.unimplemented))

    def success(self, action, result):
        build_str = f"{self._success}{self._reverse(action.method)}{result.method} -> {result.info}"
        self.append_this(action, (build_str, action, result))
        print(build_str)

    def fail(self, action, result):
        build_str = f"{self._fail}{self._reverse(action.method)}{result.method} -> {result.info}"
        self.append_this(action, (build_str, action, result))
        print(build_str)

    def exception(self, action, result):
        build_str = f"{self._exception}{self._reverse(action.method)}{result.method} -> {result.info}"
        self.append_this(action, (build_str, action, result))
        print(build_str)

    def not_implemented(self, action, result):
        super().not_implemented(action, result)
        if result.method is not None:
            self.unimplemented.add(result.method)
        else:
            # No need to add is message is None, indication that don't need, for example EOF
            pass


class MoodleFullTemplate(MoodleFirstRunTemplate):

    _reporter = FullReporter

    def old_students(self, action):
        return dropped_action(method=action.method)

    def old_staff(self, action):
        return dropped_action(method=action.method)

    def old_parents(self, action):
        return dropped_action(method=action.method)

    def update_user_profile(self, action, column):
        who = action.dest
        to_ = getattr(action.source, column)
        kwargs = {}
        mapped_column = self.user_column_map.get(column) or column
        kwargs[mapped_column] = to_
        return self.moodledb.update_table('users', where={'idnumber': who.idnumber}, **kwargs)

    def update_staff_auth(self, action):
        return self.update_user_profile(action, 'auth')

    def update_students_auth(self, action):
        return self.update_user_profile(action, 'auth')

    def update_parents_auth(self, action):
        return self.update_user_profile(action, 'auth')

    def update_staff_firstname(self, action):
        return self.update_user_profile(action, 'firstname')

    def update_students_firstname(self, action):
        return self.update_user_profile(action, 'firstname')

    def update_parents_firstname(self, action):
        return self.update_user_profile(action, 'firstname')

    def update_staff_lastname(self, action):
        return self.update_user_profile(action, 'lastname')

    def update_students_lastname(self, action):
        return self.update_user_profile(action, 'lastname')

    def update_parents_lastname(self, action):
        return self.update_user_profile(action, 'lastname')

    def update_staff_email(self, action):
        return self.update_user_profile(action, 'email')

    def update_students_email(self, action):
        return self.update_user_profile(action, 'email')

    def update_parents_email(self, action):
        return self.update_user_profile(action, 'email')

    def update_staff_username(self, action):
        return self.update_user_profile(action, 'username')

    def update_students_username(self, action):
        return self.update_user_profile(action, 'username')

    def update_parents_username(self, action):
        return self.update_user_profile(action, 'username')

    def update_staff_homeroom(self, action):
        return self.update_user_profile(action, 'homeroom')

    def update_students_homeroom(self, action):
        return self.update_user_profile(action, 'homeroom')

    def update_parents_homeroom(self, action):
        return self.update_user_profile(action, 'homeroom')

    def update_staff_name(self, action):
        return dropped_action("Users don't have 'name' in profile")

    def update_students_name(self, action):
        return dropped_action("Users don't have 'name' in profile")

    def update_parents_name(self, action):
        return dropped_action("Users don't have 'name' in profile")

    # def update_parents_lastfirst(self, action):
    #     """ This doesn't do anything """
    #     return

    def update_username(self, action):
        # First check to see to ensure that there is no one else with that username
        user = self.moodledb.get_user_from_username(action.source.username)
        if user:
            return unsuccessful_result(info=f'There is already a user with the username of {action.source.username}')
        return self.update_user_profile(action, 'username')

    def update_firstname(self, action):
        return self.update_user_profile(action, 'firstname')

    def update_lastname(self, action):
        return self.update_user_profile(action, 'lastname')

    def update_email(self, action):
        return self.update_user_profile(action, 'email')

    def new_enrollments(self, action):
        """
        This is received when a new user has enrollments not previously enrolled in anything
        Should loop through all the available enrollments
        """
        user_idnumber = action.source.idnumber
        enrollments = action.source
        ret = []
        for i, course in enumerate(enrollments.courses):
            if course not in self.courses:
                ret.append( dropped_action(method=f"No course {course} in moodle") )
                continue
            group = enrollments.groups[i]
            role = enrollments.roles[i]
            if not group:
                ret.append(return_unimplemented_result(info=f"Unknown group, not enrolling {user_idnumber} from {course}"))
                continue
            ret.append(self.php.enrol_user_into_course(user_idnumber, course, group, group, role))
        return ret

    def old_enrollments(self, action):
        """
        This is received when a new user has enrollments not previously enrolled in anything
        Should loop through all the available enrollments
        """
        user_idnumber = action.dest.idnumber
        enrollments = action.dest
        ret = []
        for i, course in enumerate(enrollments.courses):
            group = enrollments.groups[i]
            role = enrollments.roles[i]
            if not group:
                ret.append(return_unimplemented_result(info=f"Blank group, not de-enrolling {user_idnumber} from {course}"))
                continue
            ret.append(self.php.unenrol_user_from_course(user_idnumber, course))
        return ret

    def add_enrollments_courses_to_moodle(self, action):
        """
        This adds enrollments when detected a change
        action.value is the course name, which we can derive the intended group and role
        """
        user_idnumber = action.source.idnumber
        enrollments = action.source
        course = action.value
        if course not in self.courses:
            return dropped_action(method=f"No course {course} in moodle")
        index = enrollments.courses.index(course)
        group = enrollments.groups[index]
        role = enrollments.roles[index]
        return self.php.enrol_user_into_course(user_idnumber, course, group, group, role)

    def remove_enrollments_courses_from_moodle(self, action):
        user_idnumber = action.dest.idnumber
        course = action.value
        return self.php.unenrol_user_from_course(user_idnumber, course)

    def add_enrollments_groups_to_moodle(self, action):
        return []

    def add_enrollments_roles_to_moodle(self, action):
        return []

    def add_groups_members_to_moodle(self, action):
        # TODO: For this to work, we need to know the role, perhaps in source?
        return []


class HuesReporter:

    def will_start(self):
        self.unimplemented = set()

    def finished(self):
        print(sorted(self.unimplemented))

    def success(self, action, result):
        hues.success(f"{result.method} ({result.info})")

    def fail(self, action, result):
        hues.error(f"{result.method} : {result.info}")

    def exception(self, action, result):
        hues.error(f'EXCEPTION: {result.method}: {result.info}')

    def not_implemented(self, action, result):
        if result.method is not None:
            self.unimplemented.add(result.method)
        else:
            # No need to add is message is None, indication that don't need, for example EOF
            pass


class MoodleTestTemplate(MoodleFullTemplate):
    _reporter = HuesReporter






