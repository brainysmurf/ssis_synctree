from ssis_synctree.model.bases import \
    BaseStudents, BaseStaff, \
    BaseParents, BaseParentsChildLink, \
    BaseCourses, BaseSchedule, \
    BaseGroup, BaseCohort, BaseEnrollments
from synctree.interface import property_interface

import re


@property_interface(
    'firstname lastname auth username homeroom parents lastfirst email '
    '_deleted',
    firstname='', lastname='', auth='nologin', username='', email='', homeroom='', parents=[], _deleted='0',
)
class MoodleStudents(BaseStudents):
    def _grade(self):
        # FIXME: This has to be in settings.ini file
        return {'PKB': '-1'}.get(self.homeroom, re.sub('[^0-9]+$', '', self.homeroom))

    def lastfirst(self):
        return f"{self.lastname}, {self.firstname}"


@property_interface(
    'firstname lastname lastfirst email username auth homeroom '
    '_family_id',
    firstname='', lastname='', auth='nologin', username='', email='', homeroom=''
)
class MoodleParents(BaseParents):
    """
    """
    def lastfirst(self):
        return f"{self.lastname}, {self.firstname}"


@property_interface(
    'firstname lastname username email auth lastfirst '
    '',
    firstname='', lastname='', username='', email='', auth=""
)
class MoodleStaff(BaseStaff):
    def lastfirst(self):
        return f"{self.lastname}, {self.firstname}"


@property_interface(
    'links'
    '',
    links=[],
)
class MoodleParentsChildLink(BaseParentsChildLink):
    pass


@property_interface(
    'name moodle_shortcode '
    '_dbid',
    name='', moodle_shortcode='', _dbid=None
)
class MoodleCourses(BaseCourses):
    pass


@property_interface(
    'user_idnumber course group role'
    '',
    user_idnumber='', course='', group='', role=''
)
class MoodleSchedule(BaseSchedule):
    """
    """
    pass


@property_interface(
    'grade name section course members '
    '_short_code _id',
    grade='', name='', section='', course='', members='', _id='', _short_code=''
)
class MoodleGroups(BaseGroup):
    pass


@property_interface(
    'members'
    '',
    members='',
)
class MoodleCohorts(BaseCohort):
    pass


@property_interface(
    'courses groups roles ',
    courses=[], groups=[], roles=[]
)
class MoodleEnrollments(BaseEnrollments):
    pass
