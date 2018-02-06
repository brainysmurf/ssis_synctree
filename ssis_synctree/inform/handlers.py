
from psmdlsyncer.html_email import Email, read_in_templates
from psmdlsyncer.utils.Namespace import NS
from psmdlsyncer.settings import config_get_section_attribute
from psmdlsyncer.utils.Utilities import get_head_of_grade


def inform_admin(admin_email):
    pass


def reinform_new_parent(family):
    pass


def inform_new_student(student):
    path_to_templates = config_get_section_attribute('DIRECTORIES', 'path_to_templates')
    student_email_templates = read_in_templates(path_to_templates + '/student_new_account')
    sender = '"DragonNet Admin" <lcssisadmin@student.ssis-suzhou.net>'
    email = Email(config_get_section_attribute('EMAIL', 'domain'))
    email.define_sender('lcssisadmin@student.ssis-suzhou.net', "DragonNet Admin")
    email.use_templates(student_email_templates)
    email.make_subject(f"New Student in Homeroom {student.homeroom}, {student.lastfirst}")
    homeroom_teacher = student.homeroom_teacher
    if homeroom_teacher:
          email.add_to(homeroom_teacher.email)
    # ssis does not want this feature
    #for guardian_email in student.guardian_emails:
    #      email.add_to(guardian_email)
    # for class_teacher in student.get_teachers_as_list():
    #       email.add_to(class_teacher + '@ssis-suzhou.net')
    # if student.grade in [11, 12]:
    #       email.add_cc('santinagambrill@ssis-suzhou.net')
    #       email.add_cc('matthewmarshall@ssis-suzhou.net')
    # elif student.grade in [6, 7, 8, 9, 10]:
    #       email.add_cc('aubreycurran@ssis-suzhou.net')
    email.add_bcc('lcssisadmin@student.ssis-suzhou.net')
    email.add_bcc('jacobusgubbels@ssis-suzhou.net')
    email.define_fields(sf)
    email.send()


def inform_new_parent(parent):
    """
    parent is object
    """
    path_to_templates = config_get_section_attribute('DIRECTORIES', 'path_to_templates')
    parent_email_templates = read_in_templates(path_to_templates + '/parent_new_account')
    email = Email(config_get_section_attribute('EMAIL', 'domain'))
    email.define_sender('lcssisadmin@student.ssis-suzhou.net', "DragonNet Admin")
    email.use_templates(parent_email_templates)
    email.make_subject("Your SSIS DragonNet Parent Account")
    for parent_email in parent.emails:
        email.add_to(parent_email)
    for student in parent.children:
        if student.is_korean:
            email.add_language('kor')
        if student.is_chinese:
            email.add_language('chi')
    email.add_bcc('lcssisadmin@student.ssis-suzhou.net')
    email.add_bcc('jacobusgubbels@ssis-suzhou.net')
    email.define_field('username', parent.email)
    email.define_field('salutation', 'Dear Parent')

    email.send()


def inform_parent_username_changed(parent, password):
    """
    parent is object
    """
    path_to_templates = config_get_section_attribute('DIRECTORIES', 'path_to_templates')
    parent_email_templates = read_in_templates(path_to_templates + '/parent_username_changed')
    email = Email(config_get_section_attribute('EMAIL', 'domain'))
    email.define_sender('lcssisadmin@student.ssis-suzhou.net', "DragonNet Admin")
    email.use_templates(parent_email_templates)
    email.make_subject("Notification of updated SSIS DragonNet username")
    email.add_to(parent.email)
    for student in parent.children:
        if student.is_korean:
            email.add_language('kor')
        if student.is_chinese:
            email.add_language('chi')
    email.add_bcc('lcssisadmin@student.ssis-suzhou.net')
    email.add_bcc('jacobusgubbels@ssis-suzhou.net')
    email.define_field('username', parent.email)
    email.define_field('salutation', 'Dear SSIS Parent')
    email.define_field('password', password)

    email.send()

