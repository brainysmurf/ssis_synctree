"""
Exposes native Moodle functions to python
Uses pexpect utility
"""
import logging
import pexpect, sys, os
import ssis_synctree_settings
from synctree.results import \
    successful_result, \
    unsuccessful_result, \
    dropped_action, \
    exception_during_call
from ssis_synctree.utils import DynamicMockIf


class PHP:
    """
    Interfaces with php file phpclimoodle.php
    """
    # putting it here allows us to test pexpect
    _settings = ssis_synctree_settings['PHP']
    _end_of_line = '\r\n'  # terminals use this DOS-like line ending

    def __init__(self):
        #TODO: Get this info from standard settings and config
        # TODO: Depreciate this stupid dry run thingie, make it a logging feature instead
        self.path_to_cli = self._settings.get('path_to_cli')
        self.path_to_php = self._settings.get('path_to_php')
        if not self.path_to_php:
            self.path_to_php = '/usr/bin/php'

        # Moodle requires any php files to be run from the admin/cli directory
        os.chdir(self.path_to_cli)

        # And now, spawn it
        cmd = " ".join([self.path_to_php, self.path_to_cli]) + '/phpclimoodle.php'
        self.process = pexpect.spawn(cmd)
        self.process.delaybeforesend = 0  # speed things up a bit, eh?
        self.process.setecho(False)
        self.process.timeout = 3600
        self.process.expect_exact('?: ') # not sure why this works the first time

    def command(self, *args):
        """
        Interfaces with pexpect
        """
        sentline = args[0] + " '" + "' '".join(args[1:]) + "'"
        try:
            self.process.sendline(sentline)
        except OSError:
            if routine == "QUIT":
                return dropped_action()
            if self.process.isalive():
                raise Exception("Huh. Error but it's still alive!")
            else:
                raise Exception("The other side just up and died")

        # We know that the phpclimoodle file returns a plus if it's all good
        # and a negative if not, handle accordingly
        # End with \r\n... I wonder why we are getting that??
        success_string = '\+.*\r\n'
        error_string = '-\d+ .*\r\n'

        # Look for a success string or an error string
        # Wrapped in a try statement, in case something else goes wrong

        try:
            which = self.process.expect([success_string, error_string])
        except pexpect.exceptions.EOF:
            # This is actually expected
            return dropped_action()
        except Exception as e:   
            raise Exception(f'-999999 exception was raised for command {sentline}: {e}')
        the_string = "<>"
        if which == 0:
            the_string = self.process.after.decode('utf-8').strip('\r\n')
            if '++ Error' in the_string:
                which = 2  # Mimick an error
        elif which == 1:
            the_string = self.process.after.decode('utf-8').strip('\r\n')
        else:
            the_string = self.process.after.decode('utf-8').strip('\r\n') + ' -> pexpect returned non-understood result: {}'.format(which)


        # cleanup the string
        the_string.replace('\r\n', '').replace('?: ', '')  # Sometimes this "leaks" for unknown reason

        if which == 0:
            return successful_result(method=sentline, info=the_string)
        elif which == 1:
            return unsuccessful_result(method=sentline, info=the_string)
        elif which == 2:
            return exception_during_call(method=sentline, info=the_string)
        else:
            return exception_during_call(method=sentline, info="Unknown pexpect error")

    def create_new_course(self, idnumber, fullname):
        """
        Places a blank course in the category called "Teaching & Learning"
        """
        return self.command('create_new_course', idnumber, fullname)

    def create_online_portfolio(self, idnumber):
        return self.command('create_online_portfolio', idnumber)

    def create_account(self, username, email, firstname, lastname, idnumber, auth='manual'):
        return self.command('create_account', username, email, firstname, lastname, idnumber, auth)

    def delete_account(self, useridnumber):
        return self.command('delete_account', useridnumber)

    def create_group_for_course(self, course_id, group_idnumber, group_name):
        return self.command('create_group_for_course', course_id, group_idnumber, group_name)

    def create_inactive_account(self, username, email, firstname, lastname, idnumber):
        """
        CREATE A 'SUSPENDED' ACCOUNT (MAKES MORE SENSE TO CALL IT INACTIVE WHEN CREATING IT)
        SIMPLY BY PASSING nologin TO THE FUNCTION
        OTHERWISE, SAME AS create_account
        """
        return self.command('create_account', username, email, firstname, lastname, idnumber)

    def enrol_user_into_course(self, idnumber, shortname, group_id, group_name, role):
        return self.command('enrol_user_in_course', idnumber, shortname, group_id, group_name, role)

    def unenrol_user_from_course(self, idnumber, course):
        return self.command('deenrol_user_from_course', idnumber, course)

    def add_user_to_cohort(self, useridnumber, cohortidnumber):
        return self.command('add_user_to_cohort', useridnumber, cohortidnumber)

    def remove_user_from_cohort(self, useridnumber, cohortidnumber):
        return self.command('remove_user_from_cohort', useridnumber, cohortidnumber)

    def new_cohort(self, cohortidnumber, cohortname):
        return self.command("create_cohort", cohortidnumber, cohortname)

    def add_user_to_group(self, userid, group_id):
        return self.command('add_user_to_group', userid, group_id)

    def remove_user_from_group(self, userid, group_id):
        return self.command('remove_user_from_group', userid, group_id)

    def add_group(self, group_id, group_name, course_id):
        return self.command('create_group_for_course', course_id, group_id, group_name)

    def delete_group(self, group, course):
        return self.command('delete_group_for_course', course, group)

    def change_username(self, idnumber, new_name):
        return self.command('change_username', idnumber, new_name)

    def change_parent_username(self, idnumber, new_username, password):
        return self.command('change_parent_username', idnumber, new_username, password)

    def associate_child_to_parent(self, parent_idnumber, child_idnumber):
        return self.command('associate_child_to_parent', parent_idnumber, child_idnumber)

    def enrol_student_into_course(self, student_idnumber, course_idnumber, group):
        return self.enrol_user_into_course( student_idnumber, course_idnumber, group.idnumber, group.name, "student" )

    def enrol_teacher_into_course(self, teacher_idnumber, course_idnumber, group):
        return self.enrol_user_into_course( teacher_idnumber, course_idnumber, group.idnumber, group.name, "teacher" )

    def enrol_parent_into_course(self, parent_idnumber, course_idnumber, group):
        return self.enrol_user_into_course( parent_idnumber, course_idnumber, group.idnumber, group.name, "parent" )

    def deenrol_student_from_course(self, student_idnumber, course_idnumber):
        return self.unenrol_user_from_course( student_idnumber, course_idnumber )

    def deenrol_teacher_from_course(self, teacher_idnumber, course_idnumber):
        return self.unenrol_user_from_course( teacher_idnumber, course_idnumber )

    def deenrol_parent_from_course(self, parent_idnumber, course_idnumber):
        return self.unenrol_user_from_course( parent_idnumber, course_idnumber )

    def new_student(self, student):
        ret = self.create_account( student.username, student.email, student.first, student.last, student.num, auth=auth )

        # TODO: If above didn't work, this won't do anything useful
        for cohort in student.cohorts:
            self.add_user_to_cohort(student.idnumber, cohort)
        for course, group in student.get_enrollments():
            self.enrol_student_into_course(student.ID, course, group)
        inform.inform_new_student(student)

        return ret

    def delete_user(self, user):
        self.delete_account(user.idnumber)

    def new_teacher(self, teacher):
        self.create_account( teacher.username, teacher.email, teacher.first, teacher.last, teacher.num, auth='manual' )

    def new_parent(self, parent):
        # parents' email is their username
        self.create_account( parent.username, parent.email, "Parent", parent.email, parent.idnumber, auth='manual' )
        for cohort in parent.cohorts:
            self.add_user_to_cohort(parent.ID, cohort)
        for course, group in parent.get_enrollments():
            self.enrol_parent_into_course(parent.ID, course, group)
        inform.inform_new_parent(parent)

    def add_cohort(self, name):
        pass

    # def new_group(self, group):
    #     self.logger.info('Creating account for {}'.format(parent))

    def no_email(self, student):
        sf = NS(student)
        sf.new_student_cmd = self.new_email_cmd

        self.shell( sf("/bin/bash {new_student_cmd} {num} {username} '{lastfirst}'") )

    def enroll_in_groups(self, student):
        get_groups = self.sql('select id, name from ssismdl_groups')()
        self._groups = {}
        for item in get_groups:
            groupid, groupname = item
        self._groups[groupid] = groupname

    def new_support_staff(self, staff):
        """
        Support staff have fairly simple accounts
        IStaff: username
              first_name
              last_name
              email
              num
        """
        self.create_account( staff.username, staff.email, staff.first_name, staff.last_name, staff.num )

        self.add_user_to_cohort( staff.num, 'adminALL' )
