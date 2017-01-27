import os

from synctree.importers.default_importer import DefaultImporter
from synctree.importers.csv_importer import CSVImporter, TranslatedCSVImporter
from synctree.importers.db_importer import PostgresDBImporter
from synctree.importers.default_importer import DefaultImporter
from contextlib import contextmanager

from ssis_synctree.converter import convert_short_long

import ssis_synctree_settings

verbose = False

class AutosendImporter(CSVImporter):
    """
    Don't read in the username
    """
    _settings = ssis_synctree_settings['SSIS_AUTOSEND']

    def get_path(self):
        """
        Add version capabilities
        """
        path = self.get_setting('path')
        parent_dir, file_name = os.path.split(path)
        if hasattr(self, 'file_hook'):
            file_name = self.file_hook(file_name)
        starting_name = file_name.format(subbranch_name=self._subbranch.subbranchname)
        files = []
        for file_ in os.listdir(parent_dir):
            if file_.startswith(starting_name):
                version = float(file_[len(starting_name):])
                obj = {'file_':file_, 'version':version}
                files.append(obj)
        files.sort(key=lambda o: o['version'])
        if len(files) == 0:
            print("No candidates found for {}".format(starting_name))
            #exit()
        winner = files[-1]
        verbose and print("-> Using {}".format(winner))
        ret = os.path.join(parent_dir, winner['file_'])
        return ret

class AutosendStudentsImporter(AutosendImporter):
    pass
    
class AutosendStaffImporter(AutosendImporter):
    def resolve_duplicate(self, obj, **kwargs):
        """
        Update the status ensuring we indicate secondary
        TODO: status should be a list
        """
        obj._sections.add(obj._section)
        obj._sections.add(kwargs.get('_section'))
        return None

    def kwargs_preprocessor(self, kwargs):
        kwargs['_active'] = kwargs['_active'] == '1'

        if not kwargs['_active'] or kwargs['email'] == "" or not kwargs['idnumber'].isdigit():
            return None
        return kwargs

class AutosendParentsImporter(DefaultImporter):
    """
    Just go through the students branch and derive the parents as necessary
    """

    def resolve_duplicate(self, obj, **kwargs):
        if obj._kwargs != kwargs:
            if obj._kwargs.get('email') != kwargs.get('email'):
                print("Inconsistent parent emails for {0}: {0.email} != {1[email]}".format(obj, kwargs))
            else:
                print("Duplicate parent with different details {}".format(obj))

    def reader(self):
        subbranch = self._branch.students
        for student in subbranch:
            parent1 = student._family_id + '0'
            parent1_email = student._parent1_email
            parent2 = student._family_id + '1'
            parent2_email = student._parent2_email
            yield {
                'idnumber': parent1,
                'email': parent1_email,
                'lastfirst': parent1_email + ', Parent',
                'homeroom': set([student.homeroom])
            }
            yield {
                'idnumber': parent2,
                'email': parent2_email,
                'lastfirst': parent2_email + ', Parent',
                'homeroom': set([student.homeroom])
            }

    def on_import_complete(self):
        """
        Rework the homeroom to be a string (from a list), and        
        make changes to ensure that the accounts are equivalent.
        This means having the parent account use the staff email addy
        TODO: Is some operation needed when they are not the same?
        """
        for parent in self._branch.parents:
            parent.homeroom = ','.join(sorted(parent.homeroom))

            if parent.idnumber in self._branch.staff.idnumbers:
                # Make changes to ensure that the accounts are equivalent
                # This means having the parent account use the staff email addy
                # FIXME: What happens if they are not the same?
                staff = self._branch.staff.get(parent.idnumber)
                if parent.email != staff.email:
                    # Note that we have the model defined so that Parent.username
                    # will return the email handle when the email is ssis-suzhou.net domain
                    parent.email = staff.email

class AutosendParentsChildLinkImporter(DefaultImporter):
    def resolve_duplicate(self, obj, **kwargs):
        if obj._kwargs != kwargs:
            print("AutosendParentsChildLink duplicate with different info: {}".format(obj))
        return kwargs

    def reader(self):
        branch = self._branch.students
        for student in branch:
            for parent in student.parents:
                yield {
                    'idnumber': student.idnumber,
                    'links': set([parent])
                }
                yield {
                    'idnumber': parent,
                    'links': set([student.idnumber])
                }

class AutosendCohortsImporter(DefaultImporter):

    def resolve_duplicate(self, obj, **kwargs):
        if obj._kwargs != kwargs:
            print("AutosendCohorts duplicate with different info: {}".format(obj))

    def reader(self):
        for b in ['students', 'parents', 'staff']:
            subbranch = getattr(self._branch, b)
            for user in subbranch:
                user_idnumber = user.idnumber
                if b == 'students':
                    cohorts = user._cohorts
                elif b == 'parents':
                    cohorts = set()
                    parent = self._branch.parents.get(user_idnumber)
                    parentlink = self._branch.parents_child_link.get(parent.idnumber)
                    for c in parentlink.links:
                        child = self._branch.students.get(c)
                        cohorts.update({c.replace('students', 'parents') for c in child._cohorts})
                elif b == 'staff':
                    cohorts = user._cohorts

                for cohort in cohorts:
                    yield {
                        'idnumber': cohort,
                        'members': [user_idnumber]
                    }

class ScheduleImporter(AutosendImporter):
    pass

class CourseImporter(AutosendImporter):
    pass

class AutosendCoursesImporter(TranslatedCSVImporter):
    klass = CourseImporter
    translate = {'ssis_dist': ['ssis_elem', 'ssis_sec']}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Read in course mapping info and use as a dict below
        # Even though it is stored in lowercase, uppercase keys return identical results
        self.course_mappings = ssis_synctree_settings['COURSE_MAPPINGS']

    def resolve_duplicate(self, obj, **kwargs):
        """
        There are various small insignificant differences, so we just seperate with ' / '
        Reminder: resolve duplicate is not expecting you to return anything, just set it directly
        """
        created_list = getattr(obj, '_shortcodes')
        new_value = kwargs['_shortcode']
        if not new_value in created_list:
            created_list.append( new_value )

    def kwargs_preprocessor(self, kwargs_in):
        if kwargs_in['idnumber'].startswith('X'):
            return None
        orig_shortcode = kwargs_in['idnumber']

        # It woud be best to output some kind of error or reporting
        # device to indicate if there is no mapping present... 
        converted_short = self.course_mappings.get(orig_shortcode, orig_shortcode)
        #

        kwargs_in['_shortcode'] = orig_shortcode
        kwargs_in['moodle_shortcode'] = converted_short
        kwargs_in['idnumber'] = converted_short
        kwargs_in['_shortcodes'] = [orig_shortcode]
        return kwargs_in

    # def on_import_complete(self):        

class AutosendScheduleImporter(TranslatedCSVImporter):
    """
    This class is for reference only, for other branches to read in information from
    """

    klass = ScheduleImporter
    translate = {'ssis_dist': ['ssis_elem', 'ssis_sec']}

    def kwargs_preprocessor(self, kwargs_in):
        """
        Translate the course shortcode
        """
        student = self._branch.students.get(kwargs_in['student_idnumber'])
        if student is None or kwargs_in.get('course').startswith('X'):
            # TODO: Do I need to filter out if no student?
            return None
        short, _ = convert_short_long(kwargs_in['course'], "")
        kwargs_in['course'] = short

        staff = self._branch.staff.get(kwargs_in['staff_idnumber'])
        student = self._branch.students.get(kwargs_in['student_idnumber'])
        if not staff or not student:
            return None
        grade = student._grade
        kwargs_in['grade'] = grade
        kwargs_in['_old_group'] = "{}-{}-{}".format(staff.lastname.lower(), short.lower(), kwargs_in['section'].lower())
        kwargs_in['group'] = "{}-{}-{}-{}".format(staff.lastname.lower(), short.lower(), grade, kwargs_in['section'].lower())
        return kwargs_in

class AutosendGroupsImporter(DefaultImporter):
    def resolve_duplicate(self, obj, **kwargs):
        if obj._kwargs != kwargs:
            raise Exception('Unequal values')

    def reader(self):
        subbranch = self._branch.schedule
        for item in subbranch:
            id_ = item.idnumber
            student_idnumber = item.student_idnumber
            teacher_idnumber = item.staff_idnumber
            course = item.course
            group = item.group
            grade = item.grade
            section = item.section

            sobj = self._branch.get_from_subbranches(student_idnumber, ['students'])
            tobj = self._branch.get_from_subbranches(teacher_idnumber, ['staff'])
            if not sobj:
                # TODO: raiseerror instead?
                # This can happen when student is in the schedule but not in info
                continue
            members = [student_idnumber, teacher_idnumber]
            members.extend(sobj.parents)

            name = f"{tobj.lastname.title()} course{course.upper()} sec{section}"

            yield {
                'idnumber': group,
                'name': name,
                'course': course,
                'grade': grade,
                'section': section,
                'members': set(members),
            }

class AutosendEnrollmentsImporter(DefaultImporter):

    def reader(self):
        branch = self._branch.schedule
        for item in branch:
            id_ = item.idnumber
            student = item.student_idnumber
            teacher = item.staff_idnumber
            course = item.course
            group = item.group

            yield {
                'idnumber': student,
                'courses': [course],
                'groups': [group],
                'roles': ['student']
            }

            sobj = self._branch.get_from_subbranches(student, ['students'])
            if not sobj:
                print('Student in schedule but not in district info: {}'.format(student))
                continue

            for parent in sobj.parents:
                yield {
                    'idnumber': parent,
                    'courses': [course],
                    'groups': [group],
                    'roles': ['parent']
                }

            yield {
                'idnumber': teacher,
                'courses': [course],
                'groups': [group],
                'roles': ['editingteacher']
            }

