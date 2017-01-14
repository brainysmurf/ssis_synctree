from synctree.base import Base

class BaseUsers(Base):
    """

    """
    def _family_id(self):
        return self.idnumber[:4]

    def name(self):
        return self.firstname + ' ' + self.lastname

class BaseStudents(BaseUsers):

    def email(self):
        return '{}@{}'.format(self.username, 'student.ssis-suzhou.net')   # todo make this a setting instead

class BaseParents(BaseUsers):

    def _family_id(self):
        return self.idnumber[:4]

class BaseStaff(BaseUsers):
    pass

class BaseParentsChildLink(Base):
    pass

class BaseCourses(Base):
    pass

class BaseSchedule(Base):
    """
    Schedule is a placeholder only
    """
    pass

class BaseGroup(Base):
    pass

class BaseCohort(Base):
    pass

class BaseEnrollments(Base):
    pass