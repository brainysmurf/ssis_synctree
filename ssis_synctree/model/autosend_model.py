from ssis_synctree.model.bases import \
    BaseStudents, BaseStaff, \
    BaseParents, BaseParentsChildLink, \
    BaseCourses, BaseSchedule, \
    BaseGroup, BaseCohort, BaseEnrollments
import re
import ssis_synctree_settings

STUDENT_PSIDUSERNAME_MAPPINGS = 'STUDENT_PSIDUSERNAME_MAPPINGS'


class AutosendStudents(BaseStudents):
    """
    lastfirst
    """
    __slots__ = ['homeroom', 'lastfirst', '_dbid', '_dob', '_districtentrydate', '_department', '_passport', '_grade', '_guardianemails']

    @property
    def auth(self):
        """ Previous version had nologin in place, but not sure what to do """
        # boundary = int(ssis_synctree_settings.get('SSIS_AUTOSEND', 'auth_boundary'))
        # ldap_auth = ssis_synctree_settings.get('SSIS_AUTOSEND', 'auth_above_equal')
        # manual_auth = ssis_synctree_settings.get('SSIS_AUTOSEND', 'auth_less_than')
        # return ldap_auth if int(self._grade) >= boundary else manual_auth
        if self._grade in ['6']:
            return 'ldapsync_plus'
        return 'manual'

    @property
    def email(self):
        """ This has been updated to reflect Microsft 365 """
        # mapping = ssis_synctree_settings[STUDENT_PSIDUSERNAME_MAPPINGS].get(self.idnumber)
        # handle = (self.name + self._year_of_graduation).lower().replace(' ', '') if not mapping else mapping
        return self.idnumber + '@mail.ssis-suzhou.net'

    @property
    def firstname(self):
        return self.lastfirst.split(',')[1].strip()

    @property
    def lastname(self):
        return self.lastfirst.split(',')[0].strip()

    @property
    def _cohorts(self):
        ret = {'studentsALL', 'students{}'.format(self._grade), 'students{}'.format(self.homeroom)}
        ret.add( 'students{}'.format('SEC' if int(self._grade) >=6 else 'ELEM' ) )
        if int(self._grade) in range(6,11):
            ret.add('studentsMS')
        elif int(self._grade) in range(10,13):
            ret.add('studentsHS')
        return ret

    @property
    def username(self):
        """
        Username is the PSID
        """
        #return self.idnumber
        if self._grade in ['6']:
            return self.idnumber
        mapping = ssis_synctree_settings[STUDENT_PSIDUSERNAME_MAPPINGS].get(self.idnumber)
        return (self.name + self._year_of_graduation).lower().replace(' ', '').replace('-', '') if not mapping else mapping

    @property
    def parents(self):
        return [self._family_id + 'P', self._family_id + 'PP']

    @property
    def _guardian_email_list(self):
        return self._guardianemails.split(',')

    @property
    def _parent1_email(self):
        l = self._guardian_email_list
        return l[0]

    @property
    def _parent2_email(self):
        l = self._guardian_email_list
        return l[1] if len(l) > 1 else 'noemaillisted' + self._family_id + '@example.com'

    @property
    def _year_of_graduation(self):
        """
        Do the math, and then remove the '20' from the year
        Underscore, because this is not information we are tracking
        """
        return str((12 - int(self._grade)) + self._this_year)[2:]

    @property
    def _this_year(self):
        return 2018

    # TODO: Fix this to be a calculation
    # def _this_year(self):
    #     # Very rudimentary, better to use calendar to check the current year
    #     # But reminds us that an underscore is needed here because this isn't information we are tracking
    #     return 2016


class AutosendParents(BaseParents):
    """
    """
    __slots__ = ['lastfirst', 'email', 'homeroom']

    @property
    def username(self):
        """ FIXME: makes sure this works should be the idnumber """
        return self._family_id + str(len([0 for i in self.idnumber if i == 'P']) - 1)

    @property
    def firstname(self):
        return self.lastfirst.split(',')[1].strip()

    @property
    def lastname(self):
        return self.lastfirst.split(',')[0].strip()

    @property
    def auth(self):
        return 'ldap_syncplus'

    @property
    def _cohorts(self):
        """ Ensures they are placed into here """
        return ['parentsALL']


class AutosendStaff(BaseStaff):
    # For those that might have children associated to their teacher account
    #children = []
    __slots__ = ['_dbid', 'lastfirst', 'email', '_active', '_section', '_dunno', '_title', '_sections']

    @property
    def username(self):
        """ FIXME: email handle """
        return self._email_handle

    @property
    def auth(self):
        return 'ldap_syncplus'  #  if self.idnumber != '48250' else 'manual'  # jac's account

    @property
    def firstname(self): 
        return self.lastfirst.split(',')[1].strip()

    @property
    def lastname(self):
        return self.lastfirst.split(',')[0].strip()

    @property
    def _cohorts(self):
        if self._section == '0':
            ret = ['supportstaffALL']
            if self._title == 'Substitute':
                ret.append('teachersALL')
            return ret
        else:
            if hasattr(self, '_sections'):
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

    def post_init(self):
        self.email = self.email.replace('@ssis-suzhou.net', '@mail.ssis-suzhou.net')


class AutosendParentsChildLink(BaseParentsChildLink):
    __slots__ = ['links']


class AutosendCourses(BaseCourses):
    """
    """
    __slots__ = ['name', 'moodle_shortcode', '_shortcode', '_names', '_shortcodes']


class AutosendSchedule(BaseSchedule):
    """
    Not synced over, as moodle doesn't need or have a schedule
    """
    __slots__ = ['course', 'period', 'section', 'staff_idnumber', 'student_idnumber', '_old_group', 'group', 'grade']


class AutosendGroups(BaseGroup):
    """
    """
    __slots__ = ['course', 'grade', 'section', 'members', 'name', '_old_group']


class AutosendCohorts(BaseCohort):
    """
    """
    __slots__ = ['members']


class AutosendEnrollments(BaseEnrollments):
    __slots__ = ['courses', 'groups', 'roles']
