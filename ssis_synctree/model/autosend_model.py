from ssis_synctree.model.bases import \
    BaseStudents, BaseStaff, \
    BaseParents, BaseParentsChildLink, \
    BaseCourses, BaseSchedule, \
    BaseGroup, BaseCohort, BaseEnrollments
import re
from synctree.interface import property_interface
import ssis_synctree_settings

STUDENT_PSIDUSERNAME_MAPPINGS = 'STUDENT_PSIDUSERNAME_MAPPINGS'

@property_interface(
    'lastfirst name email firstname lastname auth username homeroom parents '
    '_dbid _dob _districtentrydate _department _passport _family_id _grade _guardianemails _guardian_email_list _parent1_email _parent2_email _year_of_graduation _this_year _cohorts',
    _dbid='0', _grade=0, homeroom=None, lastfirst='', _dob='0/0/0', _guardianemails='', _districtentrydate='', _department='', _passport=''
)
class AutosendStudents(BaseStudents):
    """
    lastfirst
    """

    def auth(self):
        boundary = int(ssis_synctree_settings.get('SSIS_AUTOSEND', 'auth_boundary'))
        ldap_auth = ssis_synctree_settings.get('SSIS_AUTOSEND', 'auth_above_equal')
        manual_auth = ssis_synctree_settings.get('SSIS_AUTOSEND', 'auth_less_than')
        return ldap_auth if int(self._grade) >= boundary else manual_auth

    def email(self):
        """ FIXME: In future, this will not be synced """
        mapping = ssis_synctree_settings[STUDENT_PSIDUSERNAME_MAPPINGS].get(self.idnumber)
        handle = (self.name + self._year_of_graduation).lower().replace(' ', '') if not mapping else mapping
        return handle + '@student.ssis-suzhou.net'

    def firstname(self):
        return self.lastfirst.split(',')[1].strip()

    def lastname(self):
        return self.lastfirst.split(',')[0].strip()

    def _cohorts(self):
        ret = {'studentsALL', 'students{}'.format(self._grade), 'students{}'.format(self.homeroom)}
        ret.add( 'students{}'.format('SEC' if int(self._grade) >=6 else 'ELEM' ) )
        if int(self._grade) in range(6,11):
            ret.add('studentsMS')
        elif int(self._grade) in range(10,13):
            ret.add('studentsHS')
        return ret

    def username(self):
        """
        Username is the PSID
        """
        return self.idnumber
        # mapping = ssis_synctree_settings[STUDENT_PSIDUSERNAME_MAPPINGS].get(self.idnumber)
        # return (self.name + self._year_of_graduation).lower().replace(' ', '') if not mapping else mapping

    def parents(self):
        return [self._family_id + '0', self._family_id + '1']

    def _guardian_email_list(self):
        return self._guardianemails.split(',')

    def _parent1_email(self):
        l = self._guardian_email_list
        return l[0]

    def _parent2_email(self):
        l = self._guardian_email_list
        return l[1] if len(l) > 1 else None

    def _year_of_graduation(self):
        """
        Do the math, and then remove the '20' from the year
        Underscore, because this is not information we are tracking
        """
        return str((12 - int(self._grade)) + self._this_year)[2:]

    def _this_year(self):
        return 2017

    # TODO: Fix this to be a calculation
    # def _this_year(self):
    #     # Very rudimentary, better to use calendar to check the current year
    #     # But reminds us that an underscore is needed here because this isn't information we are tracking
    #     return 2016

@property_interface(
    'firstname lastname lastfirst email username auth homeroom '
    '_family_id',
    email='', lastfirst='', homeroom=set()
)
class AutosendParents(BaseParents):
    """
    """
    def username(self):
        """ FIXME: makes sure this works should be the idnumber """
        return self.idnumber

    def firstname(self):
        return self.lastfirst.split(',')[1].strip()

    def lastname(self):
        return self.lastfirst.split(',')[0].strip()

    def auth(self):
        return 'manual'

    def _cohorts(self):
        """ Ensures they are placed into here """
        return ['parentsALL']

@property_interface(
    'lastfirst username email lastname firstname '  
    '_active _section _cohorts _dunno _sections',
    lastfirst='', _dbid='', email='', _dunno='', _active='', _title='', _section='', _sections=set()
)
class AutosendStaff(BaseStaff):
    # For those that might have children associated to their teacher account
    #children = []

    def username(self):
        """ FIXME: email handle """
        return self.idnumber

    def auth(self):
        return 'ldap_sync'

    def firstname(self): 
        return self.lastfirst.split(',')[1].strip()

    def lastname(self):
        return self.lastfirst.split(',')[0].strip()

    def _cohorts(self):
        if self._section == '0':
            return ['supportstaffALL']
        else:
            if self._sections:
                coh = ['teachersALL']
                if '111' in self._sections:
                    coh.append('teachersELEM')
                if '112' in self._sections:
                    coh.append('teachersSEC')
                return coh
            else:
                if self._section == '111':
                    return ['teachersALL', 'teachersELEM']
                elif self._section == '112':
                    return ['teachersALL', 'teachersSEC']
                else:
                    return ['teachersALL']

@property_interface(
    'links'
    '',
    links=[],
)
class AutosendParentsChildLink(BaseParentsChildLink):
    pass

@property_interface(
    'name moodle_shortcode '
    '_shortcode _names _shortcodes',
    name='', moodle_shortcode='', _shortcode='', _names=[], _shortcodes = []
)
class AutosendCourses(BaseCourses):
    """
    """
    pass
    
@property_interface(
    'course period section staff_idnumber student_idnumber'
    '',
    course='', period='', section='', staff_idnumber='', student_idnumber='', _old_group='', group='', grade='',
)    
class AutosendSchedule(BaseSchedule):
    """
    Not synced over, as moodle doesn't need or have a schedule
    """
    pass

@property_interface(
    'course grade section members name '
    '_old_group',
    course='', grade='', section='', members='', _old_group='', name=''
)
class AutosendGroups(BaseGroup):
    """
    """
    pass

@property_interface(
    'members'
    '',
    members=''
)
class AutosendCohorts(BaseCohort):
    """
    """
    pass

@property_interface(
    'courses groups roles ',
    courses=[], groups=[], roles=[]
)
class AutosendEnrollments(BaseEnrollments):
    pass
