from ssis_synctree.model.bases import \
    BaseStudents, BaseStaff, \
    BaseParents, BaseParentsChildLink, \
    BaseCourses, BaseSchedule, \
    BaseGroup, BaseCohort, BaseEnrollments

import re


class MoodleStudents(BaseStudents):
    __slots__ = ['firstname', 'lastname', 'auth', 'username', 'homeroom', 'parents', 'email', '_deleted']

    @property
    def _grade(self):
        # FIXME: This has to be in settings.ini file
        return {'PKB': '-1'}.get(self.homeroom, re.sub('[^0-9]+$', '', self.homeroom))

    @property
    def lastfirst(self):
        return f"{self.lastname}, {self.firstname}"


class MoodleParents(BaseParents):
    """
    """
    __slots__ = ['firstname', 'lastname', 'email', 'username', 'auth', 'homeroom', '_family_id']

    @property
    def lastfirst(self):
        return f"{self.lastname}, {self.firstname}"


class MoodleStaff(BaseStaff):
    __slots__ = ['firstname', 'lastname', 'username', 'email', 'auth']

    @property
    def lastfirst(self):
        return f"{self.lastname}, {self.firstname}"


class MoodleParentsChildLink(BaseParentsChildLink):
    __slots__ = ['links']


class MoodleCourses(BaseCourses):
    __slots__ = ['name', 'moodle_shortcode', '_dbid']


class MoodleSchedule(BaseSchedule):
    __slots__ = ['user_idnumber', 'course', 'group', 'role']
    """
    """
    pass


class MoodleGroups(BaseGroup):
    __slots__ = ['grade', 'name', 'section', 'course', 'members', '_short_code', '_id']


class MoodleCohorts(BaseCohort):
    __slots__ = ['members']


class MoodleEnrollments(BaseEnrollments):
    __slots__ = ['courses', 'groups', 'roles']
