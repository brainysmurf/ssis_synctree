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
        #raise NotImplemented("How to determine it is staff?")
        return '@ssis-suzhou.net' in self.email

    @property
    def _family_id(self):
        return self.idnumber[:4]

    @property
    def name(self):
        return self.firstname + ' ' + self.lastname

    @property
    def _description(self):
        return f"{self.name} ({self.idnumber}): {self.username} {self.auth.upper()}"


class BaseStudents(BaseUsers):
    __slots__ = []

    @property
    def _description(self):
        return f"{self.name} ({self.idnumber}) Grade {self._grade}: {self.username} {self.auth.upper()}"


class BaseParents(BaseUsers):
    __slots__ = []


class BaseStaff(BaseUsers):
    __slots__ = []


class BaseParentsChildLink(Base):
    __slots__ = []

    @property
    def _description(self):
        return f"PARENTS: {', '.join(sorted(self.links))}"


class BaseCourses(Base):
    __slots__ = []

    @property
    def _description(self):
        return f"{self.idnumber}: {self.name}"

class BaseSchedule(Base):
    """
    Schedule is a placeholder only
    """
    __slots__ = []

    @property
    def _description(self):
        """ Don't output """
        return None

class BaseGroup(Base):
    __slots__ = []


class BaseCohort(Base):
    __slots__ = []

    @property
    def _description(self):
        return ", ".join(self.members)


class BaseEnrollments(Base):
    __slots__ = []

    @property
    def _description(self):
        assert len(self.courses) == len(self.groups)
        num = len(self.courses)
        arranged = [self.courses.index(c) for c in sorted(self.courses)]
        enrollment_string = '\n\t'.join([self.courses[a] + ' -> ' + self.groups[a] for a in arranged])
        return f"{num} ENROLLMENTS:\n\t{enrollment_string}"


