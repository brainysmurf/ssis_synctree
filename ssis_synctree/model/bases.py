from synctree.base import Base


class BaseUsers(Base):
    """

    """
    __slots__ = []

    @property
    def _email_handle(self):
        try:
            return self.email.split('@')[0]
        except IndexError:
            return self.email

    @property
    def _is_staff(self):
        return '@ssis-suzhou.net' in self.email

    @property
    def _family_id(self):
        return self.idnumber[:4]

    @property
    def name(self):
        return self.firstname + ' ' + self.lastname


class BaseStudents(BaseUsers):
    __slots__ = []


class BaseParents(BaseUsers):
    __slots__ = []

    @property
    def _family_id(self):
        return self.idnumber[:4]


class BaseStaff(BaseUsers):
    __slots__ = []


class BaseParentsChildLink(Base):
    __slots__ = []


class BaseCourses(Base):
    __slots__ = []


class BaseSchedule(Base):
    """
    Schedule is a placeholder only
    """
    __slots__ = []


class BaseGroup(Base):
    __slots__ = []


class BaseCohort(Base):
    __slots__ = []


class BaseEnrollments(Base):
    __slots__ = []