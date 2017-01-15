<?php
define('CLI_SCRIPT', 1);

require(dirname(dirname(dirname(__FILE__))) . '/config.php');
global $CFG;
require_once($CFG->dirroot . '/cohort/lib.php');
require_once($CFG->dirroot . '/enrol/locallib.php');
require_once($CFG->dirroot . '/group/lib.php');
require_once($CFG->libdir . '/grouplib.php');
require_once($CFG->dirroot . '/course/lib.php');
#require dirname(__DIR__) . '/vendor/autoload.php';

class moodlephp
{
    private $ADMIN_USER_ID = 2;
    private $DEFAULT_PASSWORD = "changeme";

    public function __construct()
    {
        global $DB;

        $s = $DB->get_record_select('role', 'archetype = ?', array("student"));
        $this->STUDENT_ROLE_ID = $s->id;
        $s = $DB->get_record_select('role', 'shortname = ?', array('parent'));
        $this->PARENT_ROLE_ID = $s->id;
        $s = $DB->get_record_select('role', 'archetype = ?', array('editingteacher'));
        $this->TEACHER_ROLE_ID = $s->id;
    }

    public function call($args)
    {
        $which_function = $args[0];
        array_shift($args);
        if (method_exists($this, $which_function)) {
            return $this->$which_function($args);
        } else {
            return "-1 We don't have this command: " . $which_function;
        }
    }

    private function debug($data)
    {
        file_put_contents('/tmp/phpoutput.txt', $data, FILE_APPEND);
    }

    private function add_user_to_cohort($args)
    {
        $idnumber = $args[0];
        $cohortidnumber = $args[1];

        global $DB;
        if (!$user = $this->getUserByIDNumber($idnumber)) {
            return "-100 Could not find user $idnumber while adding cohort $cohortidnumber";
        }

        if (!($cohort = $DB->get_record_select('cohort', "idnumber = ?", array($cohortidnumber)))) {
            return "-101 Cohort $cohortidnumber does not exist";
        }

        $cohortID = $cohort->id;
        $userID = $user->id;
        // workaround, instead of using cohort_existing_selector, due to bug
        $cohort_membership = $DB->get_record_select(
            'cohort_members',
            'cohortid = ? and userid = ?',
            array('cohortid' => $cohortID, 'userid' => $userID)
        );
        if ($cohort_membership) {
            return "+100 $idnumber is already a member of this cohort $cohortidnumber !";
        }

        cohort_add_member($cohortID, $userID);
        return "+";
    }

    private function remove_user_from_cohort($args) {
      $idnumber = $args[0];
      $cohortidnumber = $args[1];

      global $DB;
      if( !$user = $this->getUserByIDNumber($idnumber) ) {
       return "-102 Could not find user $idnumber while removing cohort $cohortidnumber";
      }

      if ( $cohort = $DB->get_record_select( 'cohort', 'idnumber = ?', array($cohortidnumber) )) {
        $cohortID= $cohort->id;
        $userID = $user->id;
        // workaround, instead of using cohort_existing_selector, due to bug
        $cohort_membership = $DB->get_record_select('cohort_members', 'cohortid = ? and userid = ?', array('cohortid'=>$cohortID,'userid'=>$userID));
        if ( !($cohort_membership) ) {
          return "+101 $idnumber  is not a member of the cohort $cohortidnumber";
        }
      } else {
        return "-103 Could not find cohort $cohortidnumber";
    }

      $r = cohort_remove_member($cohortID, $userID);
      return "+";
    }

    private function create_online_portfolio($args)
    {
        global $DB;
        $idnumber = $args[0];

        $user = $DB->get_record('user', array('idnumber' => $idnumber));

        $olpManager = new \SSIS\Portfolios\Manager();

        // Capture output to only display if there's an error
        ob_start();
        $result = $olpManager->createAndFixCourseForUser($user);
        $output = ob_get_clean();

        if ($result) {
            return "+";
        } else{
            return "-999 Portfolio creation failed " . $output;
        }
    }

    private function create_new_course($args)
    {
        global $DB;

        $coursedata = new \stdClass();
        $coursedata->idnumber = $args[0];
        $coursedata->shortname = $args[0];
        $coursedata->fullname = $args[1];
        $teachlearning = $DB->get_field('course_categories', 'id', array('name' => 'Teaching & Learning'));
        $coursedata->category = $teachlearning;
        $coursedata->format = 'onetopic';

        $course_idnumber = $coursedata->idnumber;

        try {
            $course = create_course($coursedata);
        } catch (Exception $e) {
            return "-101 Did not create course $course_idnumber: " . $e->getMessage();
        }

        if (!$course) {
            return "-1 Could not create course. Not sure why though...";
        } else {
            return "+";
        }

    }

    private function create_cohort($args)
    {
        $cohortidnumber = $args[0];
        $cohortname = $args[1];

        $cohort = new stdClass;
        $cohort->idnumber = $cohortidnumber;
        $cohort->name = $cohortname;
        $cohort->contextid = context_system::instance()->id;
        $cohort->description = 'psmdlsyncer';

        // moodle takes care of the rest
        if (!cohort_add_cohort($cohort)) {
            return "-9 Could not create cohort $cohortidnumber (for some reason?)";
        } else {
            return "+";
        }
    }

    private function create_account($args)
    {
        $username = $args[0];
        $email = $args[1];
        $firstname = $args[2];
        $lastname = $args[3];
        $idnumber = $args[4];

        // if ( $this->user_does_exist(array($username)) ) {
        //   return "-1000 This username is already taken: $username";
        // }

        global $DB, $CFG;

        try {
            $user = create_user_record($username, "changeme");  // changeme forces password reset
        } catch (Exception $e) {
            // Probably what happened is that there is a record already with the given username.
            $user = $DB->get_record_select('user', 'username = ?', array($username));
            if (!$user) {
                return "-104 Could not create account for $username because " . $e->getMessage(
                ) . " Tried to recover deleted record, nothing";
            }
            if (substr($user->idnumber, 0, 4) != substr($idnumber, 0, 4)) {
                return "-105 Could not create account for $username because there is a deleted account that already has that username. Needs to be fixed manually";
            }
        }

        $user->deleted = 0;
        $user->email = trim($email);
        $user->firstname = trim($firstname);
        $user->lastname = trim($lastname);
        $user->idnumber = trim($idnumber);
        $user->username = trim($username);
        $user->maildigest = 1;  // All my users should use digest, for the love of god
        $user->city = 'Suzhou';
        $user->country = 'CN';

        $DB->update_record('user', $user);

        return "+";
    }

    private function user_does_exist($args)
    {
        $username = $args[0];

        global $DB, $CFG;
        $s = $DB->get_record_select('user', 'username = ?', array($username));
        return $s;
    }

    private function associate_child_to_parent($args)
    {
        $parent_idnumber = $args[0];
        $child_idnumber = $args[1];

        try {
            if ($parent = $this->getUserByIDNumber($parent_idnumber) and $child = $this->getUserByIDNumber(
                    $child_idnumber
                )
            ) {
                $context = context_user::instance($child->id);
                role_assign($this->PARENT_ROLE_ID, $parent->id, $context->id);
            } else {
                return "-105 Either could not find parent $parent_idnumber or couldn't find child $child_idnumber";
            }
        } catch (Exception $e) {
            return "-106 Could not associate child $child_idnumber to parent $parent_idnumber because " . $e->getMessage(
            );
        }

        return "+";
    }

    private function get_group_from_id($group_id) {
      // this only works properly because in draognnet group names are guaranteed to be unique
      // ( teacher username + course idnumber )
      global $DB;
      return $DB->get_record('groups', array('idnumber'=>$group_id), '*');
    }

    private function add_user_to_group($args)
    {
        $user_idnum = $args[0];
        $group_id = $args[1];

        $user = $this->getUserByIDNumber($user_idnum);
        $group = $this->get_group_from_id($group_id);

        if (!$group) {
            return "-107 Group $group_id does not exist! Cannot add user $user_idnum";
        }

        if (!$user) {
            return "-108 User $user_idnum does not exist! Cannot add him to group $group_id";
        }

        groups_add_member($group, $user);
        return "+";
    }

    private function remove_user_from_group($args)
    {
        $user_idnum = $args[0];
        $group_id = $args[1];

        global $DB;

        $user = $this->getUserByIDNumber($user_idnum);
        $group = $this->get_group_from_id($group_id);

        if (!$group) {
            return "-109 Group $group_id does not exist! Cannot remove user $user_idnum";
        }

        if (!$user) {
            return "-110 User $user_idnum does not exist! Cannot remove him to group $group_id";
        }

        groups_remove_member($group, $user);
        return "+";
    }

    private function delete_group_for_course($args)
    {
        $group_id = $args[1];

        if (!$group = $this->get_group_from_id($group_id)) {
            return "-1 Cannot get group, maybe because course does not exist?... ";
        }

        if (groups_delete_group($group)) {
            return "+";
        } else {
            return "-111 Cannot delete group... ";
        }
    }

    private function create_group_for_course($args)
    {
        $course_idnumber = $args[0];
        $group_id = $args[1];
        $group_name = $args[2];
        global $DB;

        if (!$course = $DB->get_record('course', array('idnumber' => $course_idnumber), '*')) {
            return "-112 Course does not exist $course_idnumber";
        }

        // check to see if there's one already there
        if ($group = $this->get_group_from_id($group_id)) {
            return "-113 Group ".$group_id." already exists";
        }

        $group_data = new stdClass;
        $group_data->courseid = $course->id;
        $group_data->description = 'psmdlsyncer';
        $group_data->idnumber = $group_id;
        $group_data->name = $group_name;

        try {
            $group = groups_create_group($group_data);
        } catch (Exception $e) {
            return "-113 Group ".$group_id." probably already exists ".$e->getMessage();
        }
        if ($group) {
            return "+ $group_id";
        } else {
            return "-114 Cannot create group $group_id";
        }
        return "+ $group_id";
    }

    private function enrol_user_in_course($args)
    {
        $useridnumber = $args[0];
        $course_idnumber = $args[1];
        $group_id = $args[2];
        $group_name = $args[3];
        $role = $args[4];

        switch (strtolower($role)) {
            case "student":
                $roleid = $this->STUDENT_ROLE_ID;
                break;
            case "parent":
                $roleid = $this->PARENT_ROLE_ID;
                break;
            case "editingteacher":
                $roleid = $this->TEACHER_ROLE_ID;
                break;
            default:
                return "-115 No viable role ID was passed " . $role;
        }

        global $DB, $PAGE;

        if (!$user = $this->getUserByIDnumber($useridnumber)) {
            return "-116 Could not find user $useridnumber when enrolling in course $course_idnumber";
        }

        if (!$course = $DB->get_record('course', array('idnumber' => $course_idnumber), '*')) {
            return "-117 Course does not exist!... $course_idnumber";
        }

        if (!$context = context_course::instance($course->id)) {
            return "-118 Could not get context for course $course_idnumber with ID $course->id";
        }

        $manager = new course_enrolment_manager($PAGE, $course);

        if (!is_enrolled($context, $user->id)) {
            try {
                $enrolMethod = $DB->get_record(
                    'enrol',
                    array('enrol' => 'manual', 'courseid' => $course->id),
                    '*',
                    MUST_EXIST
                );
            } catch (Exception $e) {
                return "-300 Could not find manual enrol method for course?: " . $e->getMessage();
            }
            $enrolid = $enrolMethod->id;

            $instances = $manager->get_enrolment_instances();
            $plugins = $manager->get_enrolment_plugins();

            if (!array_key_exists($enrolid, $instances)) {
                return "-119 Invalid enrol instance";
            }

            $instance = $instances[$enrolid];
            /** @var enrol_plugin $plugin */
            $plugin = $plugins[$instance->enrol];

            if (!$plugin) {
                return "-200 Cannot find plugin, used enrolid $enrolid";
            }

            $timestart = time();
            $timeend = 0;
            $plugin->enrol_user($instance, $user->id, $roleid, $timestart, $timeend);
        }

        $group = $this->get_group_from_id($group_id);
        if (!$group) {
            return "-151 Group does not exist " . $group_id;
        }

        if (groups_add_member($group, $user)) {
            return "+";
        } else {
            return "-121 Couldn't add user $useridnumber to group $group_name";
        }
    }

    private function deenrol_user_from_course($args) {
      $useridnumber = $args[0];
      $course_idnumber = $args[1];

      global $DB, $PAGE;

      if( !$user = $this->getUserByIDnumber($useridnumber) ) {
        return "-122 Could not find user $useridnumber when deenrolling from course $course_idnumber";
      }

      if( !$course = $DB->get_record('course', array('idnumber'=>$course_idnumber), '*') ) {
        return "-123 Course does not exist!... $course_idnumber";
      }

      if( !$context = context_course::instance($course->id) ) {   # get_context_instance(CONTEXT_COURSE, $course->id) ) { 
        return "-124 Could not get context for course $course_idnumber with ID $course->id";
      }

      $manager = new course_enrolment_manager($PAGE, $course);

      if( !is_enrolled($context, $user->id) ) {
       return "-125 Already not enrolled";
     }

      $enrolMethod = $DB->get_record('enrol', array('enrol'=>'manual', 'courseid'=>$course->id), '*', MUST_EXIST);
      $enrolid = $enrolMethod->id;

      $instances = $manager->get_enrolment_instances();
      $plugins = $manager->get_enrolment_plugins();

      if (!array_key_exists($enrolid, $instances)) {
       return "-119 Invalid enrol instance";
      }

      $instance = $instances[$enrolid];
      $plugin = $plugins[$instance->enrol];

      $plugin->unenrol_user($instance, $user->id);  # does not return anything

      return "+";
    }

    private function change_username($args)
    {
        $idnumber = $args[0];
        $new_username = $args[1];
        global $DB;

        $user = $this->getUserByIDNumber($idnumber);
        $user->username = $new_username;

        $DB->update_record('user', $user);
        return "+";
    }

    private function change_parent_username($args)
    {
        $idnumber = $args[0];
        $new_username = $args[1];
        $password = $args[2];
        global $DB;

        $user = $this->getUserByIDNumber($idnumber);
        $user->username = $new_username;
        $user->email = $new_username;
        if ($user->firstname == 'Parent') {
            $user->lastname = $new_username;
        }

        set_user_preference('auth_forcepasswordchange', 1, $user);
        update_internal_user_password($user, $password);

        $DB->update_record('user', $user);
        return "+";
    }

    private function getUserByIDNumber($idnumber)
    {
        global $DB;
        $s = $DB->get_record_select('user', 'idnumber = ?', array($idnumber));
        return $s;
    }

    private function getUserByUsername($username)
    {
        global $DB;
        $s = $DB->get_record_select('user', 'username = ?', array($username));
        return $s;
    }

    // private function delete_account($idnumber)
    // {

    // }
}

#str_getcsv('foo bar "so what"', $delimiter=" ");

$klass = new moodlephp();
$handle = fopen("php://stdin", "r");

$command = "";

while (trim($command) != "QUIT") {
    echo "?: ";
    $command = trim(fgets($handle));
    if ($command != 'QUIT') {
        $arguments = str_getcsv($command, $delimiter = " ", $enclosure = "'");
        try {
            $result = $klass->call($arguments);
        } catch (Exception $e) {
            $result = '-99999 ' . $e->getMessage() . $command . '(' . $arguments . ')';
        } finally {
            echo $result . "\n";
        }
    }
}

fclose($handle);
