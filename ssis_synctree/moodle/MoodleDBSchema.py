"""
Derived by using sqlalchemy tool
"""

from sqlalchemy import BigInteger, Column, Float, Index, Integer, Numeric, SmallInteger, String, Table, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class Assign(Base):
    __tablename__ = 'ssismdl_assign'

    id = Column(BigInteger, primary_key=True)
    course = Column(BigInteger, nullable=False, index=True, server_default='0')
    name = Column(String(255), nullable=False, server_default="''::character varying")
    intro = Column(Text, nullable=False)
    introformat = Column(SmallInteger, nullable=False, server_default='0')
    alwaysshowdescription = Column(SmallInteger, nullable=False, server_default='0')
    nosubmissions = Column(SmallInteger, nullable=False, server_default='0')
    submissiondrafts = Column(SmallInteger, nullable=False, server_default='0')
    sendnotifications = Column(SmallInteger, nullable=False, server_default='0')
    sendlatenotifications = Column(SmallInteger, nullable=False, server_default='0')
    duedate = Column(BigInteger, nullable=False, server_default='0')
    allowsubmissionsfromdate = Column(BigInteger, nullable=False, server_default='0')
    grade = Column(BigInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')
    requiresubmissionstatement = Column(SmallInteger, nullable=False, server_default='0')
    completionsubmit = Column(SmallInteger, nullable=False, server_default='0')
    cutoffdate = Column(BigInteger, nullable=False, server_default='0')
    teamsubmission = Column(SmallInteger, nullable=False, server_default='0')
    requireallteammemberssubmit = Column(SmallInteger, nullable=False, server_default='0')
    teamsubmissiongroupingid = Column(BigInteger, nullable=False, index=True, server_default='0')
    blindmarking = Column(SmallInteger, nullable=False, server_default='0')
    revealidentities = Column(SmallInteger, nullable=False, server_default='0')
    attemptreopenmethod = Column(String(10), nullable=False, server_default="'none'::character varying")
    maxattempts = Column(Integer, nullable=False, server_default='(-1)')


class AssignGrade(Base):
    __tablename__ = 'ssismdl_assign_grades'
    __table_args__ = (
        Index('ssismdl_assigrad_assuseatt_uix', 'assignment', 'userid', 'attemptnumber'),
    )

    id = Column(BigInteger, primary_key=True)
    assignment = Column(BigInteger, nullable=False, index=True, server_default='0')
    userid = Column(BigInteger, nullable=False, index=True, server_default='0')
    timecreated = Column(BigInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')
    grader = Column(BigInteger, nullable=False, server_default='0')
    grade = Column(Numeric(10, 5), server_default='0')
    attemptnumber = Column(BigInteger, nullable=False, index=True, server_default='0')


class AssignPluginConfig(Base):
    __tablename__ = 'ssismdl_assign_plugin_config'

    id = Column(BigInteger, primary_key=True)
    assignment = Column(BigInteger, nullable=False, index=True, server_default='0')
    plugin = Column(String(28), nullable=False, index=True, server_default="''::character varying")
    subtype = Column(String(28), nullable=False, index=True, server_default="''::character varying")
    name = Column(String(28), nullable=False, index=True, server_default="''::character varying")
    value = Column(Text)


class AssignSubmission(Base):
    __tablename__ = 'ssismdl_assign_submission'
    __table_args__ = (
        Index('ssismdl_assisubm_assusegro_uix', 'assignment', 'userid', 'groupid', 'attemptnumber'),
    )

    id = Column(BigInteger, primary_key=True)
    assignment = Column(BigInteger, nullable=False, index=True, server_default='0')
    userid = Column(BigInteger, nullable=False, index=True, server_default='0')
    timecreated = Column(BigInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')
    status = Column(String(10))
    groupid = Column(BigInteger, nullable=False, server_default='0')
    attemptnumber = Column(BigInteger, nullable=False, index=True, server_default='0')


class AssignUserFlag(Base):
    __tablename__ = 'ssismdl_assign_user_flags'

    id = Column(BigInteger, primary_key=True)
    userid = Column(BigInteger, nullable=False, index=True, server_default='0')
    assignment = Column(BigInteger, nullable=False, index=True, server_default='0')
    locked = Column(BigInteger, nullable=False, server_default='0')
    mailed = Column(SmallInteger, nullable=False, index=True, server_default='0')
    extensionduedate = Column(BigInteger, nullable=False, server_default='0')


class AssignUserMapping(Base):
    __tablename__ = 'ssismdl_assign_user_mapping'

    id = Column(BigInteger, primary_key=True)
    assignment = Column(BigInteger, nullable=False, index=True, server_default='0')
    userid = Column(BigInteger, nullable=False, index=True, server_default='0')


class AssignfeedbackComment(Base):
    __tablename__ = 'ssismdl_assignfeedback_comments'

    id = Column(BigInteger, primary_key=True)
    assignment = Column(BigInteger, nullable=False, index=True, server_default='0')
    grade = Column(BigInteger, nullable=False, index=True, server_default='0')
    commenttext = Column(Text)
    commentformat = Column(SmallInteger, nullable=False, server_default='0')


class AssignfeedbackFile(Base):
    __tablename__ = 'ssismdl_assignfeedback_file'

    id = Column(BigInteger, primary_key=True)
    assignment = Column(BigInteger, nullable=False, index=True, server_default='0')
    grade = Column(BigInteger, nullable=False, index=True, server_default='0')
    numfiles = Column(BigInteger, nullable=False, server_default='0')


class Assignment(Base):
    __tablename__ = 'ssismdl_assignment'

    id = Column(BigInteger, primary_key=True)
    course = Column(BigInteger, nullable=False, index=True, server_default='0')
    name = Column(String(255), nullable=False, server_default="''::character varying")
    intro = Column(Text, nullable=False)
    introformat = Column(SmallInteger, nullable=False, server_default='0')
    assignmenttype = Column(String(50), nullable=False, server_default="''::character varying")
    resubmit = Column(SmallInteger, nullable=False, server_default='0')
    preventlate = Column(SmallInteger, nullable=False, server_default='0')
    emailteachers = Column(SmallInteger, nullable=False, server_default='0')
    var1 = Column(BigInteger, server_default='0')
    var2 = Column(BigInteger, server_default='0')
    var3 = Column(BigInteger, server_default='0')
    var4 = Column(BigInteger, server_default='0')
    var5 = Column(BigInteger, server_default='0')
    maxbytes = Column(BigInteger, nullable=False, server_default='100000')
    timedue = Column(BigInteger, nullable=False, server_default='0')
    timeavailable = Column(BigInteger, nullable=False, server_default='0')
    grade = Column(BigInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')


class AssignmentSubmission(Base):
    __tablename__ = 'ssismdl_assignment_submissions'

    id = Column(BigInteger, primary_key=True)
    assignment = Column(BigInteger, nullable=False, index=True, server_default='0')
    userid = Column(BigInteger, nullable=False, index=True, server_default='0')
    timecreated = Column(BigInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')
    numfiles = Column(BigInteger, nullable=False, server_default='0')
    data1 = Column(Text)
    data2 = Column(Text)
    grade = Column(BigInteger, nullable=False, server_default='0')
    submissioncomment = Column(Text, nullable=False)
    format = Column(SmallInteger, nullable=False, server_default='0')
    teacher = Column(BigInteger, nullable=False, server_default='0')
    timemarked = Column(BigInteger, nullable=False, index=True, server_default='0')
    mailed = Column(SmallInteger, nullable=False, index=True, server_default='0')


class AssignmentUploadpdf(Base):
    __tablename__ = 'ssismdl_assignment_uploadpdf'

    id = Column(BigInteger, primary_key=True)
    assignment = Column(BigInteger, nullable=False, unique=True, server_default='0')
    coversheet = Column(Text)
    template = Column(BigInteger, nullable=False, index=True, server_default='0')
    onlypdf = Column(SmallInteger, server_default='1')
    checklist = Column(BigInteger, server_default='0')
    checklist_percent = Column(BigInteger, server_default='0')


class AssignmentUploadpdfAnnot(Base):
    __tablename__ = 'ssismdl_assignment_uploadpdf_annot'
    __table_args__ = (
        Index('ssismdl_assiuploanno_asspag_ix', 'assignment_submission', 'pageno'),
    )

    id = Column(BigInteger, primary_key=True)
    assignment_submission = Column(BigInteger, nullable=False, index=True, server_default='0')
    startx = Column(BigInteger, server_default='0')
    starty = Column(BigInteger, nullable=False, server_default='0')
    endx = Column(BigInteger, nullable=False, server_default='0')
    endy = Column(BigInteger, nullable=False, server_default='0')
    path = Column(Text)
    pageno = Column(BigInteger, nullable=False, server_default='0')
    colour = Column(String(10), server_default="'red'::character varying")
    type = Column(String(10), server_default="'line'::character varying")


class AssignmentUploadpdfComment(Base):
    __tablename__ = 'ssismdl_assignment_uploadpdf_comment'
    __table_args__ = (
        Index('ssismdl_assiuplocomm_asspag_ix', 'assignment_submission', 'pageno'),
    )

    id = Column(BigInteger, primary_key=True)
    assignment_submission = Column(BigInteger, nullable=False, index=True, server_default='0')
    posx = Column(BigInteger, server_default='0')
    posy = Column(BigInteger, nullable=False, server_default='0')
    width = Column(BigInteger, nullable=False, server_default='120')
    rawtext = Column(Text)
    pageno = Column(BigInteger, nullable=False, server_default='0')
    colour = Column(String(10), server_default="'yellow'::character varying")


class AssignmentUploadpdfQcklist(Base):
    __tablename__ = 'ssismdl_assignment_uploadpdf_qcklist'

    id = Column(BigInteger, primary_key=True)
    userid = Column(BigInteger, nullable=False, index=True)
    text = Column(Text)
    width = Column(BigInteger, nullable=False)
    colour = Column(String(10), nullable=False, server_default="'yellow'::character varying")


class AssignmentUploadpdfTmpl(Base):
    __tablename__ = 'ssismdl_assignment_uploadpdf_tmpl'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(255))
    course = Column(BigInteger, nullable=False, index=True)


class AssignmentUploadpdfTmplitm(Base):
    __tablename__ = 'ssismdl_assignment_uploadpdf_tmplitm'

    id = Column(BigInteger, primary_key=True)
    template = Column(BigInteger, nullable=False, index=True)
    type = Column(String(15), nullable=False, server_default="'shorttext'::character varying")
    xpos = Column(BigInteger, nullable=False, server_default='0')
    ypos = Column(BigInteger, nullable=False, server_default='0')
    width = Column(BigInteger, server_default='0')
    setting = Column(String(255))


class AssignsubmissionFile(Base):
    __tablename__ = 'ssismdl_assignsubmission_file'

    id = Column(BigInteger, primary_key=True)
    assignment = Column(BigInteger, nullable=False, index=True, server_default='0')
    submission = Column(BigInteger, nullable=False, index=True, server_default='0')
    numfiles = Column(BigInteger, nullable=False, server_default='0')


class AssignsubmissionOnlinetext(Base):
    __tablename__ = 'ssismdl_assignsubmission_onlinetext'

    id = Column(BigInteger, primary_key=True)
    assignment = Column(BigInteger, nullable=False, index=True, server_default='0')
    submission = Column(BigInteger, nullable=False, index=True, server_default='0')
    onlinetext = Column(Text)
    onlineformat = Column(SmallInteger, nullable=False, server_default='0')


class Attendance(Base):
    __tablename__ = 'ssismdl_attendance'

    id = Column(BigInteger, primary_key=True)
    course = Column(BigInteger, nullable=False, index=True, server_default='0')
    name = Column(String(255))
    grade = Column(BigInteger, nullable=False, server_default='100')


class AttendanceLog(Base):
    __tablename__ = 'ssismdl_attendance_log'

    id = Column(BigInteger, primary_key=True)
    sessionid = Column(BigInteger, nullable=False, index=True, server_default='0')
    studentid = Column(BigInteger, nullable=False, index=True, server_default='0')
    statusid = Column(BigInteger, nullable=False, index=True, server_default='0')
    statusset = Column(String(100))
    timetaken = Column(BigInteger, nullable=False, server_default='0')
    takenby = Column(BigInteger, nullable=False, server_default='0')
    remarks = Column(String(255))


class AttendanceSession(Base):
    __tablename__ = 'ssismdl_attendance_sessions'

    id = Column(BigInteger, primary_key=True)
    attendanceid = Column(BigInteger, nullable=False, index=True, server_default='0')
    groupid = Column(BigInteger, nullable=False, index=True, server_default='0')
    sessdate = Column(BigInteger, nullable=False, index=True, server_default='0')
    duration = Column(BigInteger, nullable=False, server_default='0')
    lasttaken = Column(BigInteger)
    lasttakenby = Column(BigInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger)
    description = Column(Text, nullable=False)
    descriptionformat = Column(SmallInteger, nullable=False, server_default='0')


class AttendanceStatus(Base):
    __tablename__ = 'ssismdl_attendance_statuses'

    id = Column(BigInteger, primary_key=True)
    attendanceid = Column(BigInteger, nullable=False, index=True, server_default='0')
    acronym = Column(String(2), nullable=False, server_default="''::character varying")
    description = Column(String(30), nullable=False, server_default="''::character varying")
    grade = Column(SmallInteger, nullable=False, server_default='0')
    visible = Column(SmallInteger, nullable=False, index=True, server_default='1')
    deleted = Column(SmallInteger, nullable=False, index=True, server_default='0')


class BackupController(Base):
    __tablename__ = 'ssismdl_backup_controllers'
    __table_args__ = (
        Index('ssismdl_backcont_typite_ix', 'type', 'itemid'),
    )

    id = Column(BigInteger, primary_key=True)
    backupid = Column(String(32), nullable=False, unique=True, server_default="''::character varying")
    operation = Column(String(20), nullable=False, server_default="'backup'::character varying")
    type = Column(String(10), nullable=False, server_default="''::character varying")
    itemid = Column(BigInteger, nullable=False)
    format = Column(String(20), nullable=False, server_default="''::character varying")
    interactive = Column(SmallInteger, nullable=False)
    purpose = Column(SmallInteger, nullable=False)
    userid = Column(BigInteger, nullable=False, index=True)
    status = Column(SmallInteger, nullable=False)
    execution = Column(SmallInteger, nullable=False)
    executiontime = Column(BigInteger, nullable=False)
    checksum = Column(String(32), nullable=False, server_default="''::character varying")
    timecreated = Column(BigInteger, nullable=False)
    timemodified = Column(BigInteger, nullable=False)
    controller = Column(Text, nullable=False)


class BackupCourse(Base):
    __tablename__ = 'ssismdl_backup_courses'

    id = Column(BigInteger, primary_key=True)
    courseid = Column(BigInteger, nullable=False, unique=True, server_default='0')
    laststarttime = Column(BigInteger, nullable=False, server_default='0')
    lastendtime = Column(BigInteger, nullable=False, server_default='0')
    laststatus = Column(String(1), nullable=False, server_default="'0'::character varying")
    nextstarttime = Column(BigInteger, nullable=False, server_default='0')


class BackupFilesTemplate(Base):
    __tablename__ = 'ssismdl_backup_files_template'
    __table_args__ = (
        Index('ssismdl_backfiletemp_baccon_ix', 'backupid', 'contextid', 'component', 'filearea', 'itemid'),
    )

    id = Column(BigInteger, primary_key=True)
    backupid = Column(String(32), nullable=False, server_default="''::character varying")
    contextid = Column(BigInteger, nullable=False)
    component = Column(String(100), nullable=False, server_default="''::character varying")
    filearea = Column(String(50), nullable=False, server_default="''::character varying")
    itemid = Column(BigInteger, nullable=False)
    info = Column(Text)
    newcontextid = Column(BigInteger)
    newitemid = Column(BigInteger)


class BackupIdsTemplate(Base):
    __tablename__ = 'ssismdl_backup_ids_template'
    __table_args__ = (
        Index('ssismdl_backidstemp_bacite_uix', 'backupid', 'itemname', 'itemid'),
        Index('ssismdl_backidstemp_baciten_ix', 'backupid', 'itemname', 'newitemid'),
        Index('ssismdl_backidstemp_bacitep_ix', 'backupid', 'itemname', 'parentitemid')
    )

    id = Column(BigInteger, primary_key=True)
    backupid = Column(String(32), nullable=False, server_default="''::character varying")
    itemname = Column(String(160), nullable=False, server_default="''::character varying")
    itemid = Column(BigInteger, nullable=False)
    newitemid = Column(BigInteger, nullable=False, server_default='0')
    parentitemid = Column(BigInteger)
    info = Column(Text)


class BackupLog(Base):
    __tablename__ = 'ssismdl_backup_logs'
    __table_args__ = (
        Index('ssismdl_backlogs_bacid_uix', 'backupid', 'id'),
    )

    id = Column(BigInteger, primary_key=True)
    backupid = Column(String(32), nullable=False, index=True, server_default="''::character varying")
    loglevel = Column(SmallInteger, nullable=False)
    message = Column(String(255), nullable=False, server_default="''::character varying")
    timecreated = Column(BigInteger, nullable=False)


class Badge(Base):
    __tablename__ = 'ssismdl_badge'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(255), nullable=False, server_default="''::character varying")
    description = Column(Text)
    image = Column(BigInteger, nullable=False)
    timecreated = Column(BigInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')
    usercreated = Column(BigInteger, nullable=False, index=True)
    usermodified = Column(BigInteger, nullable=False, index=True)
    issuername = Column(String(255), nullable=False, server_default="''::character varying")
    issuerurl = Column(String(255), nullable=False, server_default="''::character varying")
    issuercontact = Column(String(255))
    expiredate = Column(BigInteger)
    expireperiod = Column(BigInteger)
    type = Column(SmallInteger, nullable=False, index=True, server_default='1')
    courseid = Column(BigInteger, index=True)
    message = Column(Text, nullable=False)
    messagesubject = Column(Text, nullable=False)
    attachment = Column(SmallInteger, nullable=False, server_default='1')
    notification = Column(SmallInteger, nullable=False, server_default='1')
    status = Column(SmallInteger, nullable=False, server_default='0')
    nextcron = Column(BigInteger)


class BadgeBackpack(Base):
    __tablename__ = 'ssismdl_badge_backpack'

    id = Column(BigInteger, primary_key=True)
    userid = Column(BigInteger, nullable=False, index=True, server_default='0')
    email = Column(String(100), nullable=False, server_default="''::character varying")
    backpackurl = Column(String(255), nullable=False, server_default="''::character varying")
    backpackuid = Column(BigInteger, nullable=False)
    autosync = Column(SmallInteger, nullable=False, server_default='0')
    password = Column(String(50))


class BadgeCriterion(Base):
    __tablename__ = 'ssismdl_badge_criteria'
    __table_args__ = (
        Index('ssismdl_badgcrit_badcri_uix', 'badgeid', 'criteriatype'),
    )

    id = Column(BigInteger, primary_key=True)
    badgeid = Column(BigInteger, nullable=False, index=True, server_default='0')
    criteriatype = Column(BigInteger, index=True)
    method = Column(SmallInteger, nullable=False, server_default='1')


class BadgeCriteriaMet(Base):
    __tablename__ = 'ssismdl_badge_criteria_met'

    id = Column(BigInteger, primary_key=True)
    issuedid = Column(BigInteger, index=True)
    critid = Column(BigInteger, nullable=False, index=True)
    userid = Column(BigInteger, nullable=False, index=True)
    datemet = Column(BigInteger, nullable=False)


class BadgeCriteriaParam(Base):
    __tablename__ = 'ssismdl_badge_criteria_param'

    id = Column(BigInteger, primary_key=True)
    critid = Column(BigInteger, nullable=False, index=True)
    name = Column(String(255), nullable=False, server_default="''::character varying")
    value = Column(String(255))


class BadgeExternal(Base):
    __tablename__ = 'ssismdl_badge_external'

    id = Column(BigInteger, primary_key=True)
    backpackid = Column(BigInteger, nullable=False, index=True)
    collectionid = Column(BigInteger, nullable=False)


class BadgeIssued(Base):
    __tablename__ = 'ssismdl_badge_issued'
    __table_args__ = (
        Index('ssismdl_badgissu_baduse_uix', 'badgeid', 'userid'),
    )

    id = Column(BigInteger, primary_key=True)
    badgeid = Column(BigInteger, nullable=False, index=True, server_default='0')
    userid = Column(BigInteger, nullable=False, index=True, server_default='0')
    uniquehash = Column(Text, nullable=False)
    dateissued = Column(BigInteger, nullable=False, server_default='0')
    dateexpire = Column(BigInteger)
    visible = Column(SmallInteger, nullable=False, server_default='0')
    issuernotified = Column(BigInteger)


class BadgeManualAward(Base):
    __tablename__ = 'ssismdl_badge_manual_award'

    id = Column(BigInteger, primary_key=True)
    badgeid = Column(BigInteger, nullable=False, index=True)
    recipientid = Column(BigInteger, nullable=False, index=True)
    issuerid = Column(BigInteger, nullable=False, index=True)
    issuerrole = Column(BigInteger, nullable=False, index=True)
    datemet = Column(BigInteger, nullable=False)


class Block(Base):
    __tablename__ = 'ssismdl_block'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(40), nullable=False, unique=True, server_default="''::character varying")
    version = Column(BigInteger, nullable=False, server_default='0')
    cron = Column(BigInteger, nullable=False, server_default='0')
    lastcron = Column(BigInteger, nullable=False, server_default='0')
    visible = Column(SmallInteger, nullable=False, server_default='1')


class BlockCommunity(Base):
    __tablename__ = 'ssismdl_block_community'

    id = Column(BigInteger, primary_key=True)
    userid = Column(BigInteger, nullable=False)
    coursename = Column(String(255), nullable=False, server_default="''::character varying")
    coursedescription = Column(Text)
    courseurl = Column(String(255), nullable=False, server_default="''::character varying")
    imageurl = Column(String(255), nullable=False, server_default="''::character varying")


class BlockConfigurableReport(Base):
    __tablename__ = 'ssismdl_block_configurable_reports'

    id = Column(BigInteger, primary_key=True)
    courseid = Column(BigInteger, nullable=False)
    ownerid = Column(BigInteger, nullable=False)
    visible = Column(SmallInteger, nullable=False)
    name = Column(String(128), nullable=False, server_default="''::character varying")
    summary = Column(Text)
    type = Column(String(128), nullable=False, server_default="''::character varying")
    pagination = Column(SmallInteger)
    components = Column(Text)
    export = Column(String(255))
    jsordering = Column(SmallInteger)


class BlockInstance(Base):
    __tablename__ = 'ssismdl_block_instances'
    __table_args__ = (
        Index('ssismdl_blocinst_parshopags_ix', 'parentcontextid', 'showinsubcontexts', 'pagetypepattern', 'subpagepattern'),
    )

    id = Column(BigInteger, primary_key=True)
    blockname = Column(String(40), nullable=False, server_default="''::character varying")
    parentcontextid = Column(BigInteger, nullable=False, index=True)
    showinsubcontexts = Column(SmallInteger, nullable=False)
    pagetypepattern = Column(String(64), nullable=False, server_default="''::character varying")
    subpagepattern = Column(String(16))
    defaultregion = Column(String(16), nullable=False, server_default="''::character varying")
    defaultweight = Column(BigInteger, nullable=False)
    configdata = Column(Text)


class BlockMrbsArea(Base):
    __tablename__ = 'ssismdl_block_mrbs_area'

    id = Column(BigInteger, primary_key=True)
    area_name = Column(String(30))
    area_admin_email = Column(Text)


class BlockMrbsEntry(Base):
    __tablename__ = 'ssismdl_block_mrbs_entry'

    id = Column(BigInteger, primary_key=True)
    start_time = Column(BigInteger, nullable=False, server_default='0')
    end_time = Column(BigInteger, nullable=False, server_default='0')
    entry_type = Column(BigInteger, nullable=False, server_default='0')
    repeat_id = Column(BigInteger, nullable=False, server_default='0')
    room_id = Column(BigInteger, nullable=False, server_default='1')
    timestamp = Column(BigInteger, nullable=False, server_default='0')
    create_by = Column(String(80), nullable=False, server_default="''::character varying")
    name = Column(String(80), nullable=False, server_default="''::character varying")
    type = Column(String(1), nullable=False, server_default="'E'::character varying")
    description = Column(Text)
    roomchange = Column(SmallInteger, nullable=False, server_default='0')


class BlockMrbsRepeat(Base):
    __tablename__ = 'ssismdl_block_mrbs_repeat'

    id = Column(BigInteger, primary_key=True)
    start_time = Column(BigInteger, nullable=False, server_default='0')
    end_time = Column(BigInteger, nullable=False, server_default='0')
    rep_type = Column(BigInteger, nullable=False, server_default='0')
    end_date = Column(BigInteger, nullable=False, server_default='0')
    rep_opt = Column(String(32), nullable=False, server_default="''::character varying")
    room_id = Column(BigInteger, nullable=False, server_default='1')
    timestamp = Column(BigInteger, nullable=False, server_default='0')
    create_by = Column(String(80), nullable=False, server_default="''::character varying")
    name = Column(String(80), nullable=False, server_default="''::character varying")
    type = Column(String(1), nullable=False, server_default="'E'::character varying")
    description = Column(Text)
    rep_num_weeks = Column(Integer)


class BlockMrbsRoom(Base):
    __tablename__ = 'ssismdl_block_mrbs_room'

    id = Column(BigInteger, primary_key=True)
    area_id = Column(BigInteger, nullable=False, server_default='0')
    room_name = Column(String(25), nullable=False, server_default="''::character varying")
    description = Column(String(60))
    capacity = Column(BigInteger, nullable=False, server_default='0')
    room_admin_email = Column(Text)
    booking_users = Column(Text)


class BlockPosition(Base):
    __tablename__ = 'ssismdl_block_positions'
    __table_args__ = (
        Index('ssismdl_blocposi_bloconpag_uix', 'blockinstanceid', 'contextid', 'pagetype', 'subpage'),
    )

    id = Column(BigInteger, primary_key=True)
    blockinstanceid = Column(BigInteger, nullable=False, index=True)
    contextid = Column(BigInteger, nullable=False, index=True)
    pagetype = Column(String(64), nullable=False, server_default="''::character varying")
    subpage = Column(String(16), nullable=False, server_default="''::character varying")
    visible = Column(SmallInteger, nullable=False)
    region = Column(String(16), nullable=False, server_default="''::character varying")
    weight = Column(BigInteger, nullable=False)


class BlockRssClient(Base):
    __tablename__ = 'ssismdl_block_rss_client'

    id = Column(BigInteger, primary_key=True)
    userid = Column(BigInteger, nullable=False, server_default='0')
    title = Column(Text, nullable=False)
    preferredtitle = Column(String(64), nullable=False, server_default="''::character varying")
    description = Column(Text, nullable=False)
    shared = Column(SmallInteger, nullable=False, server_default='0')
    url = Column(String(255), nullable=False, server_default="''::character varying")


class BlogAssociation(Base):
    __tablename__ = 'ssismdl_blog_association'

    id = Column(BigInteger, primary_key=True)
    contextid = Column(BigInteger, nullable=False, index=True)
    blogid = Column(BigInteger, nullable=False, index=True)


class BlogExternal(Base):
    __tablename__ = 'ssismdl_blog_external'

    id = Column(BigInteger, primary_key=True)
    userid = Column(BigInteger, nullable=False, index=True)
    name = Column(String(255), nullable=False, server_default="''::character varying")
    description = Column(Text)
    url = Column(Text, nullable=False)
    filtertags = Column(String(255))
    failedlastsync = Column(SmallInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger)
    timefetched = Column(BigInteger, nullable=False, server_default='0')


class Book(Base):
    __tablename__ = 'ssismdl_book'

    id = Column(BigInteger, primary_key=True)
    course = Column(BigInteger, nullable=False, server_default='0')
    name = Column(String(255), nullable=False, server_default="''::character varying")
    intro = Column(Text)
    introformat = Column(SmallInteger, nullable=False, server_default='0')
    numbering = Column(SmallInteger, nullable=False, server_default='0')
    customtitles = Column(SmallInteger, nullable=False, server_default='0')
    revision = Column(BigInteger, nullable=False, server_default='0')
    timecreated = Column(BigInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')


class BookChapter(Base):
    __tablename__ = 'ssismdl_book_chapters'

    id = Column(BigInteger, primary_key=True)
    bookid = Column(BigInteger, nullable=False, server_default='0')
    pagenum = Column(BigInteger, nullable=False, server_default='0')
    subchapter = Column(BigInteger, nullable=False, server_default='0')
    title = Column(String(255), nullable=False, server_default="''::character varying")
    content = Column(Text, nullable=False)
    contentformat = Column(SmallInteger, nullable=False, server_default='0')
    hidden = Column(SmallInteger, nullable=False, server_default='0')
    timecreated = Column(BigInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')
    importsrc = Column(String(255), nullable=False, server_default="''::character varying")


class Brainpop(Base):
    __tablename__ = 'ssismdl_brainpop'

    id = Column(BigInteger, primary_key=True)
    course = Column(BigInteger, nullable=False, index=True, server_default='0')
    name = Column(String(255), nullable=False, server_default="''::character varying")
    intro = Column(Text)
    introformat = Column(SmallInteger, nullable=False, server_default='0')
    externalurl = Column(Text, nullable=False)
    display = Column(SmallInteger, nullable=False, server_default='0')
    displayoptions = Column(Text)
    parameters = Column(Text)
    timemodified = Column(BigInteger, nullable=False, server_default='0')


class CacheFilter(Base):
    __tablename__ = 'ssismdl_cache_filters'
    __table_args__ = (
        Index('ssismdl_cachfilt_filmd5_ix', 'filter', 'md5key'),
    )

    id = Column(BigInteger, primary_key=True)
    filter = Column(String(32), nullable=False, server_default="''::character varying")
    version = Column(BigInteger, nullable=False, server_default='0')
    md5key = Column(String(32), nullable=False, server_default="''::character varying")
    rawtext = Column(Text, nullable=False)
    timemodified = Column(BigInteger, nullable=False, server_default='0')


class CacheFlag(Base):
    __tablename__ = 'ssismdl_cache_flags'

    id = Column(BigInteger, primary_key=True)
    flagtype = Column(String(255), nullable=False, index=True, server_default="''::character varying")
    name = Column(String(255), nullable=False, index=True, server_default="''::character varying")
    timemodified = Column(BigInteger, nullable=False, server_default='0')
    value = Column(Text, nullable=False)
    expiry = Column(BigInteger, nullable=False)


class CacheText(Base):
    __tablename__ = 'ssismdl_cache_text'

    id = Column(BigInteger, primary_key=True)
    md5key = Column(String(32), nullable=False, index=True, server_default="''::character varying")
    formattedtext = Column(Text, nullable=False)
    timemodified = Column(BigInteger, nullable=False, index=True, server_default='0')


class Capability(Base):
    __tablename__ = 'ssismdl_capabilities'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(255), nullable=False, unique=True, server_default="''::character varying")
    captype = Column(String(50), nullable=False, server_default="''::character varying")
    contextlevel = Column(BigInteger, nullable=False, server_default='0')
    component = Column(String(100), nullable=False, server_default="''::character varying")
    riskbitmask = Column(BigInteger, nullable=False, server_default='0')

class BlockHomework(Base):
    __tablename__ = 'ssismdl_block_homework'

    id = Column(BigInteger, primary_key=True, server_default="nextval('ssismdl_block_homework_id_seq'::regclass)")
    approved = Column(SmallInteger, nullable=False, index=True, server_default="0")
    userid = Column(BigInteger, index=True)
    courseid = Column(BigInteger, index=True)
    groupid = Column(BigInteger, index=True)
    added = Column(BigInteger)
    description = Column(Text)
    startdate = Column(Text)
    duedate = Column(Text)
    duration = Column(Text)
    private = Column(SmallInteger, nullable=False, index=True, server_default="0")
    title = Column(Text)

class BlockHomeworkAssignDate(Base):
    __tablename__ = 'ssismdl_block_homework_assign_dates'

    id = Column(BigInteger, primary_key=True, server_default="nextval('ssismdl_block_homework_assign_dates_id_seq'::regclass)")
    homeworkid = Column(BigInteger, nullable=False, index=True, server_default="0")
    date = Column(Text, nullable=False)

class BlockHomeworkNote(Base):
    __tablename__ = 'ssismdl_block_homework_notes'
    __table_args__ = (
        Index('ssismdl_blochomenote_homu2_uix', 'homeworkid', 'userid', unique=True),
    )

    id = Column(BigInteger, primary_key=True, server_default="nextval('ssismdl_block_homework_notes_id_seq'::regclass)")
    homeworkid = Column(BigInteger, nullable=False, index=True)
    userid = Column(BigInteger, nullable=False, index=True)
    notes = Column(Text)

class Chat(Base):
    __tablename__ = 'ssismdl_chat'

    id = Column(BigInteger, primary_key=True)
    course = Column(BigInteger, nullable=False, index=True, server_default='0')
    name = Column(String(255), nullable=False, server_default="''::character varying")
    intro = Column(Text, nullable=False)
    introformat = Column(SmallInteger, nullable=False, server_default='0')
    keepdays = Column(BigInteger, nullable=False, server_default='0')
    studentlogs = Column(SmallInteger, nullable=False, server_default='0')
    chattime = Column(BigInteger, nullable=False, server_default='0')
    schedule = Column(SmallInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')


class ChatMessage(Base):
    __tablename__ = 'ssismdl_chat_messages'
    __table_args__ = (
        Index('ssismdl_chatmess_timcha_ix', 'timestamp', 'chatid'),
    )

    id = Column(BigInteger, primary_key=True)
    chatid = Column(BigInteger, nullable=False, index=True, server_default='0')
    userid = Column(BigInteger, nullable=False, index=True, server_default='0')
    groupid = Column(BigInteger, nullable=False, index=True, server_default='0')
    system = Column(SmallInteger, nullable=False, server_default='0')
    message = Column(Text, nullable=False)
    timestamp = Column(BigInteger, nullable=False, server_default='0')


class ChatMessagesCurrent(Base):
    __tablename__ = 'ssismdl_chat_messages_current'
    __table_args__ = (
        Index('ssismdl_chatmesscurr_timcha_ix', 'timestamp', 'chatid'),
    )

    id = Column(BigInteger, primary_key=True)
    chatid = Column(BigInteger, nullable=False, index=True, server_default='0')
    userid = Column(BigInteger, nullable=False, index=True, server_default='0')
    groupid = Column(BigInteger, nullable=False, index=True, server_default='0')
    system = Column(SmallInteger, nullable=False, server_default='0')
    message = Column(Text, nullable=False)
    timestamp = Column(BigInteger, nullable=False, server_default='0')


class ChatUser(Base):
    __tablename__ = 'ssismdl_chat_users'

    id = Column(BigInteger, primary_key=True)
    chatid = Column(BigInteger, nullable=False, index=True, server_default='0')
    userid = Column(BigInteger, nullable=False, index=True, server_default='0')
    groupid = Column(BigInteger, nullable=False, index=True, server_default='0')
    version = Column(String(16), nullable=False, server_default="''::character varying")
    ip = Column(String(45), nullable=False, server_default="''::character varying")
    firstping = Column(BigInteger, nullable=False, server_default='0')
    lastping = Column(BigInteger, nullable=False, index=True, server_default='0')
    lastmessageping = Column(BigInteger, nullable=False, server_default='0')
    sid = Column(String(32), nullable=False, server_default="''::character varying")
    course = Column(BigInteger, nullable=False, server_default='0')
    lang = Column(String(30), nullable=False, server_default="''::character varying")


class Choice(Base):
    __tablename__ = 'ssismdl_choice'

    id = Column(BigInteger, primary_key=True)
    course = Column(BigInteger, nullable=False, index=True, server_default='0')
    name = Column(String(255), nullable=False, server_default="''::character varying")
    intro = Column(Text, nullable=False)
    introformat = Column(SmallInteger, nullable=False, server_default='0')
    publish = Column(SmallInteger, nullable=False, server_default='0')
    showresults = Column(SmallInteger, nullable=False, server_default='0')
    display = Column(SmallInteger, nullable=False, server_default='0')
    allowupdate = Column(SmallInteger, nullable=False, server_default='0')
    showunanswered = Column(SmallInteger, nullable=False, server_default='0')
    limitanswers = Column(SmallInteger, nullable=False, server_default='0')
    timeopen = Column(BigInteger, nullable=False, server_default='0')
    timeclose = Column(BigInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')
    completionsubmit = Column(SmallInteger, nullable=False, server_default='0')


class ChoiceAnswer(Base):
    __tablename__ = 'ssismdl_choice_answers'

    id = Column(BigInteger, primary_key=True)
    choiceid = Column(BigInteger, nullable=False, index=True, server_default='0')
    userid = Column(BigInteger, nullable=False, index=True, server_default='0')
    optionid = Column(BigInteger, nullable=False, index=True, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')


class ChoiceOption(Base):
    __tablename__ = 'ssismdl_choice_options'

    id = Column(BigInteger, primary_key=True)
    choiceid = Column(BigInteger, nullable=False, index=True, server_default='0')
    text = Column(Text)
    maxanswers = Column(BigInteger, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')


class Cohort(Base):
    __tablename__ = 'ssismdl_cohort'

    id = Column(BigInteger, primary_key=True)
    contextid = Column(BigInteger, nullable=False, index=True)
    name = Column(String(254), nullable=False, server_default="''::character varying")
    idnumber = Column(String(100))
    description = Column(Text)
    descriptionformat = Column(SmallInteger, nullable=False)
    component = Column(String(100), nullable=False, server_default="''::character varying")
    timecreated = Column(BigInteger, nullable=False)
    timemodified = Column(BigInteger, nullable=False)


class CohortMember(Base):
    __tablename__ = 'ssismdl_cohort_members'
    __table_args__ = (
        Index('ssismdl_cohomemb_cohuse_uix', 'cohortid', 'userid'),
    )

    id = Column(BigInteger, primary_key=True)
    cohortid = Column(BigInteger, nullable=False, index=True, server_default='0')
    userid = Column(BigInteger, nullable=False, index=True, server_default='0')
    timeadded = Column(BigInteger, nullable=False, server_default='0')


class Comment(Base):
    __tablename__ = 'ssismdl_comments'

    id = Column(BigInteger, primary_key=True)
    contextid = Column(BigInteger, nullable=False)
    commentarea = Column(String(255), nullable=False, server_default="''::character varying")
    itemid = Column(BigInteger, nullable=False)
    content = Column(Text, nullable=False)
    format = Column(SmallInteger, nullable=False, server_default='0')
    userid = Column(BigInteger, nullable=False)
    timecreated = Column(BigInteger, nullable=False)


class Config(Base):
    __tablename__ = 'ssismdl_config'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(255), nullable=False, unique=True, server_default="''::character varying")
    value = Column(Text, nullable=False)


class ConfigLog(Base):
    __tablename__ = 'ssismdl_config_log'

    id = Column(BigInteger, primary_key=True)
    userid = Column(BigInteger, nullable=False, index=True)
    timemodified = Column(BigInteger, nullable=False, index=True)
    plugin = Column(String(100))
    name = Column(String(100), nullable=False, server_default="''::character varying")
    value = Column(Text)
    oldvalue = Column(Text)


class ConfigPlugin(Base):
    __tablename__ = 'ssismdl_config_plugins'
    __table_args__ = (
        Index('ssismdl_confplug_plunam_uix', 'plugin', 'name'),
    )

    id = Column(BigInteger, primary_key=True)
    plugin = Column(String(100), nullable=False, server_default="'core'::character varying")
    name = Column(String(100), nullable=False, server_default="''::character varying")
    value = Column(Text, nullable=False)


class Context(Base):
    __tablename__ = 'ssismdl_context'
    __table_args__ = (
        Index('ssismdl_cont_conins_uix', 'contextlevel', 'instanceid'),
    )

    id = Column(BigInteger, primary_key=True)
    contextlevel = Column(BigInteger, nullable=False, server_default='0')
    instanceid = Column(BigInteger, nullable=False, index=True, server_default='0')
    path = Column(String(255), index=True)
    depth = Column(SmallInteger, nullable=False, server_default='0')


class ContextTemp(Base):
    __tablename__ = 'ssismdl_context_temp'

    id = Column(BigInteger, primary_key=True)
    path = Column(String(255), nullable=False, server_default="''::character varying")
    depth = Column(SmallInteger, nullable=False)


class Course(Base):
    __tablename__ = 'ssismdl_course'

    id = Column(BigInteger, primary_key=True)
    category = Column(BigInteger, nullable=False, index=True, server_default='0')
    sortorder = Column(BigInteger, nullable=False, index=True, server_default='0')
    fullname = Column(String(254), nullable=False, server_default="''::character varying")
    shortname = Column(String(255), nullable=False, index=True, server_default="''::character varying")
    idnumber = Column(String(100), nullable=False, index=True, server_default="''::character varying")
    summary = Column(Text)
    summaryformat = Column(SmallInteger, nullable=False, server_default='0')
    format = Column(String(21), nullable=False, server_default="'topics'::character varying")
    showgrades = Column(SmallInteger, nullable=False, server_default='1')
    #modinfo = Column(Text)
    newsitems = Column(Integer, nullable=False, server_default='1')
    startdate = Column(BigInteger, nullable=False, server_default='0')
    marker = Column(BigInteger, nullable=False, server_default='0')
    maxbytes = Column(BigInteger, nullable=False, server_default='0')
    legacyfiles = Column(SmallInteger, nullable=False, server_default='0')
    showreports = Column(SmallInteger, nullable=False, server_default='0')
    visible = Column(SmallInteger, nullable=False, server_default='1')
    visibleold = Column(SmallInteger, nullable=False, server_default='1')
    groupmode = Column(SmallInteger, nullable=False, server_default='0')
    groupmodeforce = Column(SmallInteger, nullable=False, server_default='0')
    defaultgroupingid = Column(BigInteger, nullable=False, server_default='0')
    lang = Column(String(30), nullable=False, server_default="''::character varying")
    theme = Column(String(50), nullable=False, server_default="''::character varying")
    timecreated = Column(BigInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')
    requested = Column(SmallInteger, nullable=False, server_default='0')
    enablecompletion = Column(SmallInteger, nullable=False, server_default='0')
    completionnotify = Column(SmallInteger, nullable=False, server_default='0')
    #sectioncache = Column(Text)


class CourseCategory(Base):
    __tablename__ = 'ssismdl_course_categories'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(255), nullable=False, server_default="''::character varying")
    idnumber = Column(String(100))
    description = Column(Text)
    descriptionformat = Column(SmallInteger, nullable=False, server_default='0')
    parent = Column(BigInteger, nullable=False, index=True, server_default='0')
    sortorder = Column(BigInteger, nullable=False, server_default='0')
    coursecount = Column(BigInteger, nullable=False, server_default='0')
    visible = Column(SmallInteger, nullable=False, server_default='1')
    visibleold = Column(SmallInteger, nullable=False, server_default='1')
    timemodified = Column(BigInteger, nullable=False, server_default='0')
    depth = Column(BigInteger, nullable=False, server_default='0')
    path = Column(String(255), nullable=False, server_default="''::character varying")
    theme = Column(String(50))


class CourseCompletionAggrMethd(Base):
    __tablename__ = 'ssismdl_course_completion_aggr_methd'
    __table_args__ = (
        Index('ssismdl_courcompaggrmeth_c_uix', 'course', 'criteriatype'),
    )

    id = Column(BigInteger, primary_key=True)
    course = Column(BigInteger, nullable=False, index=True, server_default='0')
    criteriatype = Column(BigInteger, index=True)
    method = Column(SmallInteger, nullable=False, server_default='0')
    value = Column(Numeric(10, 5))


class CourseCompletionCritCompl(Base):
    __tablename__ = 'ssismdl_course_completion_crit_compl'
    __table_args__ = (
        Index('ssismdl_courcompcritcomp_u_uix', 'userid', 'course', 'criteriaid'),
    )

    id = Column(BigInteger, primary_key=True)
    userid = Column(BigInteger, nullable=False, index=True, server_default='0')
    course = Column(BigInteger, nullable=False, index=True, server_default='0')
    criteriaid = Column(BigInteger, nullable=False, index=True, server_default='0')
    gradefinal = Column(Numeric(10, 5))
    unenroled = Column(BigInteger)
    timecompleted = Column(BigInteger, index=True)


class CourseCompletionCriterion(Base):
    __tablename__ = 'ssismdl_course_completion_criteria'

    id = Column(BigInteger, primary_key=True)
    course = Column(BigInteger, nullable=False, index=True, server_default='0')
    criteriatype = Column(BigInteger, nullable=False, server_default='0')
    module = Column(String(100))
    moduleinstance = Column(BigInteger)
    courseinstance = Column(BigInteger)
    enrolperiod = Column(BigInteger)
    timeend = Column(BigInteger)
    gradepass = Column(Numeric(10, 5))
    role = Column(BigInteger)


class CourseCompletion(Base):
    __tablename__ = 'ssismdl_course_completions'
    __table_args__ = (
        Index('ssismdl_courcomp_usecou_uix', 'userid', 'course'),
    )

    id = Column(BigInteger, primary_key=True)
    userid = Column(BigInteger, nullable=False, index=True, server_default='0')
    course = Column(BigInteger, nullable=False, index=True, server_default='0')
    timeenrolled = Column(BigInteger, nullable=False, server_default='0')
    timestarted = Column(BigInteger, nullable=False, server_default='0')
    timecompleted = Column(BigInteger, index=True)
    reaggregate = Column(BigInteger, nullable=False, server_default='0')


class CourseFormatOption(Base):
    __tablename__ = 'ssismdl_course_format_options'
    __table_args__ = (
        Index('ssismdl_courformopti_coufo_uix', 'courseid', 'format', 'sectionid', 'name'),
    )

    id = Column(BigInteger, primary_key=True)
    courseid = Column(BigInteger, nullable=False, index=True)
    format = Column(String(21), nullable=False, server_default="''::character varying")
    sectionid = Column(BigInteger, nullable=False, server_default='0')
    name = Column(String(100), nullable=False, server_default="''::character varying")
    value = Column(Text)


class CourseModule(Base):
    __tablename__ = 'ssismdl_course_modules'
    __table_args__ = (
        Index('ssismdl_courmodu_idncou_ix', 'idnumber', 'course'),
    )

    id = Column(BigInteger, primary_key=True)
    course = Column(BigInteger, nullable=False, index=True, server_default='0')
    module = Column(BigInteger, nullable=False, index=True, server_default='0')
    instance = Column(BigInteger, nullable=False, index=True, server_default='0')
    section = Column(BigInteger, nullable=False, server_default='0')
    idnumber = Column(String(100))
    added = Column(BigInteger, nullable=False, server_default='0')
    score = Column(SmallInteger, nullable=False, server_default='0')
    indent = Column(Integer, nullable=False, server_default='0')
    visible = Column(SmallInteger, nullable=False, index=True, server_default='1')
    visibleold = Column(SmallInteger, nullable=False, server_default='1')
    groupmode = Column(SmallInteger, nullable=False, server_default='0')
    groupingid = Column(BigInteger, nullable=False, index=True, server_default='0')
    groupmembersonly = Column(SmallInteger, nullable=False, server_default='0')
    completion = Column(SmallInteger, nullable=False, server_default='0')
    completiongradeitemnumber = Column(BigInteger)
    completionview = Column(SmallInteger, nullable=False, server_default='0')
    completionexpected = Column(BigInteger, nullable=False, server_default='0')
    availablefrom = Column(BigInteger, nullable=False, server_default='0')
    availableuntil = Column(BigInteger, nullable=False, server_default='0')
    showavailability = Column(SmallInteger, nullable=False, server_default='0')
    showdescription = Column(SmallInteger, nullable=False, server_default='0')


class CourseModulesAvailField(Base):
    __tablename__ = 'ssismdl_course_modules_avail_fields'

    id = Column(BigInteger, primary_key=True)
    coursemoduleid = Column(BigInteger, nullable=False, index=True)
    userfield = Column(String(50))
    customfieldid = Column(BigInteger)
    operator = Column(String(20), nullable=False, server_default="''::character varying")
    value = Column(String(255), nullable=False, server_default="''::character varying")


class CourseModulesAvailability(Base):
    __tablename__ = 'ssismdl_course_modules_availability'

    id = Column(BigInteger, primary_key=True)
    coursemoduleid = Column(BigInteger, nullable=False, index=True)
    sourcecmid = Column(BigInteger, index=True)
    requiredcompletion = Column(SmallInteger)
    gradeitemid = Column(BigInteger, index=True)
    grademin = Column(Numeric(10, 5))
    grademax = Column(Numeric(10, 5))


class CourseModulesCompletion(Base):
    __tablename__ = 'ssismdl_course_modules_completion'
    __table_args__ = (
        Index('ssismdl_courmoducomp_useco_uix', 'userid', 'coursemoduleid'),
    )

    id = Column(BigInteger, primary_key=True)
    coursemoduleid = Column(BigInteger, nullable=False, index=True)
    userid = Column(BigInteger, nullable=False)
    completionstate = Column(SmallInteger, nullable=False)
    viewed = Column(SmallInteger)
    timemodified = Column(BigInteger, nullable=False)


class CoursePublished(Base):
    __tablename__ = 'ssismdl_course_published'

    id = Column(BigInteger, primary_key=True)
    huburl = Column(String(255))
    courseid = Column(BigInteger, nullable=False)
    timepublished = Column(BigInteger, nullable=False)
    enrollable = Column(SmallInteger, nullable=False, server_default='1')
    hubcourseid = Column(BigInteger, nullable=False)
    status = Column(SmallInteger, server_default='0')
    timechecked = Column(BigInteger)


class CourseRequest(Base):
    __tablename__ = 'ssismdl_course_request'

    id = Column(BigInteger, primary_key=True)
    fullname = Column(String(254), nullable=False, server_default="''::character varying")
    shortname = Column(String(100), nullable=False, index=True, server_default="''::character varying")
    summary = Column(Text, nullable=False)
    summaryformat = Column(SmallInteger, nullable=False, server_default='0')
    reason = Column(Text, nullable=False)
    requester = Column(BigInteger, nullable=False, server_default='0')
    password = Column(String(50), nullable=False, server_default="''::character varying")
    category = Column(BigInteger, nullable=False, server_default='0')


class CourseSection(Base):
    __tablename__ = 'ssismdl_course_sections'
    __table_args__ = (
        Index('ssismdl_coursect_cousec_uix', 'course', 'section'),
    )

    id = Column(BigInteger, primary_key=True)
    course = Column(BigInteger, nullable=False, server_default='0')
    section = Column(BigInteger, nullable=False, server_default='0')
    name = Column(String(255))
    summary = Column(Text)
    summaryformat = Column(SmallInteger, nullable=False, server_default='0')
    sequence = Column(Text)
    visible = Column(SmallInteger, nullable=False, server_default='1')
    availablefrom = Column(BigInteger, nullable=False, server_default='0')
    availableuntil = Column(BigInteger, nullable=False, server_default='0')
    showavailability = Column(SmallInteger, nullable=False, server_default='0')
    groupingid = Column(BigInteger, nullable=False, server_default='0')


class CourseSectionsAvailField(Base):
    __tablename__ = 'ssismdl_course_sections_avail_fields'

    id = Column(BigInteger, primary_key=True)
    coursesectionid = Column(BigInteger, nullable=False, index=True)
    userfield = Column(String(50))
    customfieldid = Column(BigInteger)
    operator = Column(String(20), nullable=False, server_default="''::character varying")
    value = Column(String(255), nullable=False, server_default="''::character varying")


class CourseSectionsAvailability(Base):
    __tablename__ = 'ssismdl_course_sections_availability'

    id = Column(BigInteger, primary_key=True)
    coursesectionid = Column(BigInteger, nullable=False, index=True)
    sourcecmid = Column(BigInteger, index=True)
    requiredcompletion = Column(SmallInteger)
    gradeitemid = Column(BigInteger, index=True)
    grademin = Column(Numeric(10, 5))
    grademax = Column(Numeric(10, 5))


class CourseSsisMetadatum(Base):
    __tablename__ = 'ssismdl_course_ssis_metadata'

    courseid = Column(Integer, primary_key=True, nullable=False)
    field = Column(String(255), primary_key=True, nullable=False)
    value = Column(String(255))


class Datum(Base):
    __tablename__ = 'ssismdl_data'

    id = Column(BigInteger, primary_key=True)
    course = Column(BigInteger, nullable=False, index=True, server_default='0')
    name = Column(String(255), nullable=False, server_default="''::character varying")
    intro = Column(Text, nullable=False)
    introformat = Column(SmallInteger, nullable=False, server_default='0')
    comments = Column(SmallInteger, nullable=False, server_default='0')
    timeavailablefrom = Column(BigInteger, nullable=False, server_default='0')
    timeavailableto = Column(BigInteger, nullable=False, server_default='0')
    timeviewfrom = Column(BigInteger, nullable=False, server_default='0')
    timeviewto = Column(BigInteger, nullable=False, server_default='0')
    requiredentries = Column(Integer, nullable=False, server_default='0')
    requiredentriestoview = Column(Integer, nullable=False, server_default='0')
    maxentries = Column(Integer, nullable=False, server_default='0')
    rssarticles = Column(SmallInteger, nullable=False, server_default='0')
    singletemplate = Column(Text)
    listtemplate = Column(Text)
    listtemplateheader = Column(Text)
    listtemplatefooter = Column(Text)
    addtemplate = Column(Text)
    rsstemplate = Column(Text)
    rsstitletemplate = Column(Text)
    csstemplate = Column(Text)
    jstemplate = Column(Text)
    asearchtemplate = Column(Text)
    approval = Column(SmallInteger, nullable=False, server_default='0')
    scale = Column(BigInteger, nullable=False, server_default='0')
    assessed = Column(BigInteger, nullable=False, server_default='0')
    assesstimestart = Column(BigInteger, nullable=False, server_default='0')
    assesstimefinish = Column(BigInteger, nullable=False, server_default='0')
    defaultsort = Column(BigInteger, nullable=False, server_default='0')
    defaultsortdir = Column(SmallInteger, nullable=False, server_default='0')
    editany = Column(SmallInteger, nullable=False, server_default='0')
    notification = Column(BigInteger, nullable=False, server_default='0')


class DataContent(Base):
    __tablename__ = 'ssismdl_data_content'

    id = Column(BigInteger, primary_key=True)
    fieldid = Column(BigInteger, nullable=False, index=True, server_default='0')
    recordid = Column(BigInteger, nullable=False, index=True, server_default='0')
    content = Column(Text)
    content1 = Column(Text)
    content2 = Column(Text)
    content3 = Column(Text)
    content4 = Column(Text)


class DataField(Base):
    __tablename__ = 'ssismdl_data_fields'
    __table_args__ = (
        Index('ssismdl_datafiel_typdat_ix', 'type', 'dataid'),
    )

    id = Column(BigInteger, primary_key=True)
    dataid = Column(BigInteger, nullable=False, index=True, server_default='0')
    type = Column(String(255), nullable=False, server_default="''::character varying")
    name = Column(String(255), nullable=False, server_default="''::character varying")
    description = Column(Text, nullable=False)
    param1 = Column(Text)
    param2 = Column(Text)
    param3 = Column(Text)
    param4 = Column(Text)
    param5 = Column(Text)
    param6 = Column(Text)
    param7 = Column(Text)
    param8 = Column(Text)
    param9 = Column(Text)
    param10 = Column(Text)


class DataRecord(Base):
    __tablename__ = 'ssismdl_data_records'

    id = Column(BigInteger, primary_key=True)
    userid = Column(BigInteger, nullable=False, server_default='0')
    groupid = Column(BigInteger, nullable=False, server_default='0')
    dataid = Column(BigInteger, nullable=False, index=True, server_default='0')
    timecreated = Column(BigInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')
    approved = Column(SmallInteger, nullable=False, server_default='0')


class DnetDestinyImported(Base):
    __tablename__ = 'ssismdl_dnet_destiny_imported'

    id = Column(BigInteger, primary_key=True)
    patron_name = Column(String(255))
    patron_barcode = Column(String(255))
    patron_districtid = Column(String(255))
    due = Column(BigInteger)
    call_number = Column(String(255))
    title = Column(String(255))


class DnetDestinyLog(Base):
    __tablename__ = 'ssismdl_dnet_destiny_log'

    id = Column(BigInteger, primary_key=True)
    date = Column(String(255))
    records = Column(BigInteger)


class DnetPwresetKey(Base):
    __tablename__ = 'ssismdl_dnet_pwreset_keys'

    id = Column(BigInteger, primary_key=True)
    userid = Column(BigInteger)
    key = Column(String(50))
    time = Column(BigInteger)
    used = Column(SmallInteger)


class Enrol(Base):
    __tablename__ = 'ssismdl_enrol'

    id = Column(BigInteger, primary_key=True)
    enrol = Column(String(20), nullable=False, index=True, server_default="''::character varying")
    status = Column(BigInteger, nullable=False, server_default='0')
    courseid = Column(BigInteger, nullable=False, index=True)
    sortorder = Column(BigInteger, nullable=False, server_default='0')
    name = Column(String(255))
    enrolperiod = Column(BigInteger, server_default='0')
    enrolstartdate = Column(BigInteger, server_default='0')
    enrolenddate = Column(BigInteger, server_default='0')
    expirynotify = Column(SmallInteger, server_default='0')
    expirythreshold = Column(BigInteger, server_default='0')
    notifyall = Column(SmallInteger, server_default='0')
    password = Column(String(50))
    cost = Column(String(20))
    currency = Column(String(3))
    roleid = Column(BigInteger, server_default='0')
    customint1 = Column(BigInteger)
    customint2 = Column(BigInteger)
    customint3 = Column(BigInteger)
    customint4 = Column(BigInteger)
    customchar1 = Column(String(255))
    customchar2 = Column(String(255))
    customdec1 = Column(Numeric(12, 7))
    customdec2 = Column(Numeric(12, 7))
    customtext1 = Column(Text)
    customtext2 = Column(Text)
    timecreated = Column(BigInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')
    customint5 = Column(BigInteger)
    customint6 = Column(BigInteger)
    customint7 = Column(BigInteger)
    customint8 = Column(BigInteger)
    customchar3 = Column(String(1333))
    customtext3 = Column(Text)
    customtext4 = Column(Text)


class EnrolAuthorize(Base):
    __tablename__ = 'ssismdl_enrol_authorize'

    id = Column(BigInteger, primary_key=True)
    paymentmethod = Column(String(6), nullable=False, server_default="'cc'::character varying")
    refundinfo = Column(SmallInteger, nullable=False, server_default='0')
    ccname = Column(String(255), nullable=False, server_default="''::character varying")
    courseid = Column(BigInteger, nullable=False, index=True, server_default='0')
    instanceid = Column(BigInteger, nullable=False, server_default='0')
    userid = Column(BigInteger, nullable=False, index=True, server_default='0')
    transid = Column(BigInteger, nullable=False, index=True, server_default='0')
    status = Column(BigInteger, nullable=False, index=True, server_default='0')
    timecreated = Column(BigInteger, nullable=False, server_default='0')
    settletime = Column(BigInteger, nullable=False, server_default='0')
    amount = Column(String(10), nullable=False, server_default="''::character varying")
    currency = Column(String(3), nullable=False, server_default="'USD'::character varying")


class EnrolAuthorizeRefund(Base):
    __tablename__ = 'ssismdl_enrol_authorize_refunds'

    id = Column(BigInteger, primary_key=True)
    orderid = Column(BigInteger, nullable=False, index=True, server_default='0')
    status = Column(SmallInteger, nullable=False, server_default='0')
    amount = Column(String(10), nullable=False, server_default="''::character varying")
    transid = Column(BigInteger, index=True, server_default='0')
    settletime = Column(BigInteger, nullable=False, server_default='0')


class EnrolFlatfile(Base):
    __tablename__ = 'ssismdl_enrol_flatfile'

    id = Column(BigInteger, primary_key=True)
    action = Column(String(30), nullable=False, server_default="''::character varying")
    roleid = Column(BigInteger, nullable=False, index=True)
    userid = Column(BigInteger, nullable=False, index=True)
    courseid = Column(BigInteger, nullable=False, index=True)
    timestart = Column(BigInteger, nullable=False, server_default='0')
    timeend = Column(BigInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')


class EnrolPaypal(Base):
    __tablename__ = 'ssismdl_enrol_paypal'

    id = Column(BigInteger, primary_key=True)
    business = Column(String(255), nullable=False, server_default="''::character varying")
    receiver_email = Column(String(255), nullable=False, server_default="''::character varying")
    receiver_id = Column(String(255), nullable=False, server_default="''::character varying")
    item_name = Column(String(255), nullable=False, server_default="''::character varying")
    courseid = Column(BigInteger, nullable=False, server_default='0')
    userid = Column(BigInteger, nullable=False, server_default='0')
    instanceid = Column(BigInteger, nullable=False, server_default='0')
    memo = Column(String(255), nullable=False, server_default="''::character varying")
    tax = Column(String(255), nullable=False, server_default="''::character varying")
    option_name1 = Column(String(255), nullable=False, server_default="''::character varying")
    option_selection1_x = Column(String(255), nullable=False, server_default="''::character varying")
    option_name2 = Column(String(255), nullable=False, server_default="''::character varying")
    option_selection2_x = Column(String(255), nullable=False, server_default="''::character varying")
    payment_status = Column(String(255), nullable=False, server_default="''::character varying")
    pending_reason = Column(String(255), nullable=False, server_default="''::character varying")
    reason_code = Column(String(30), nullable=False, server_default="''::character varying")
    txn_id = Column(String(255), nullable=False, server_default="''::character varying")
    parent_txn_id = Column(String(255), nullable=False, server_default="''::character varying")
    payment_type = Column(String(30), nullable=False, server_default="''::character varying")
    timeupdated = Column(BigInteger, nullable=False, server_default='0')


class Etherpad(Base):
    __tablename__ = 'ssismdl_etherpad'

    id = Column(BigInteger, primary_key=True)
    course = Column(BigInteger, nullable=False, server_default='0')
    name = Column(String(255), nullable=False, server_default="''::character varying")
    padname = Column(String(255), nullable=False, server_default="''::character varying")
    intro = Column(Text, nullable=False)
    introformat = Column(BigInteger, server_default='1')
    timemodified = Column(BigInteger, nullable=False, server_default='0')


class Event(Base):
    __tablename__ = 'ssismdl_event'
    __table_args__ = (
        Index('ssismdl_even_grocouvisuse_ix', 'groupid', 'courseid', 'visible', 'userid'),
    )

    id = Column(BigInteger, primary_key=True)
    name = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    format = Column(SmallInteger, nullable=False, server_default='0')
    courseid = Column(BigInteger, nullable=False, index=True, server_default='0')
    groupid = Column(BigInteger, nullable=False, server_default='0')
    userid = Column(BigInteger, nullable=False, index=True, server_default='0')
    repeatid = Column(BigInteger, nullable=False, server_default='0')
    modulename = Column(String(20), nullable=False, server_default="''::character varying")
    instance = Column(BigInteger, nullable=False, server_default='0')
    eventtype = Column(String(20), nullable=False, server_default="''::character varying")
    timestart = Column(BigInteger, nullable=False, index=True, server_default='0')
    timeduration = Column(BigInteger, nullable=False, index=True, server_default='0')
    visible = Column(SmallInteger, nullable=False, server_default='1')
    uuid = Column(String(255), nullable=False, server_default="''::character varying")
    sequence = Column(BigInteger, nullable=False, server_default='1')
    timemodified = Column(BigInteger, nullable=False, server_default='0')
    subscriptionid = Column(BigInteger)


class EventSubscription(Base):
    __tablename__ = 'ssismdl_event_subscriptions'

    id = Column(BigInteger, primary_key=True)
    url = Column(String(255), nullable=False, server_default="''::character varying")
    courseid = Column(BigInteger, nullable=False, server_default='0')
    groupid = Column(BigInteger, nullable=False, server_default='0')
    userid = Column(BigInteger, nullable=False, server_default='0')
    pollinterval = Column(BigInteger, nullable=False, server_default='0')
    lastupdated = Column(BigInteger)
    name = Column(String(255), nullable=False, server_default="''::character varying")
    eventtype = Column(String(20), nullable=False, server_default="''::character varying")


class EventsHandler(Base):
    __tablename__ = 'ssismdl_events_handlers'
    __table_args__ = (
        Index('ssismdl_evenhand_evecom_uix', 'eventname', 'component'),
    )

    id = Column(BigInteger, primary_key=True)
    eventname = Column(String(166), nullable=False, server_default="''::character varying")
    component = Column(String(166), nullable=False, server_default="''::character varying")
    handlerfile = Column(String(255), nullable=False, server_default="''::character varying")
    handlerfunction = Column(Text)
    schedule = Column(String(255))
    status = Column(BigInteger, nullable=False, server_default='0')
    internal = Column(SmallInteger, nullable=False, server_default='1')


class EventsQueue(Base):
    __tablename__ = 'ssismdl_events_queue'

    id = Column(BigInteger, primary_key=True)
    eventdata = Column(Text, nullable=False)
    stackdump = Column(Text)
    userid = Column(BigInteger, index=True)
    timecreated = Column(BigInteger, nullable=False)


class EventsQueueHandler(Base):
    __tablename__ = 'ssismdl_events_queue_handlers'

    id = Column(BigInteger, primary_key=True)
    queuedeventid = Column(BigInteger, nullable=False, index=True)
    handlerid = Column(BigInteger, nullable=False, index=True)
    status = Column(BigInteger)
    errormessage = Column(Text)
    timemodified = Column(BigInteger, nullable=False)


class ExternalFunction(Base):
    __tablename__ = 'ssismdl_external_functions'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(200), nullable=False, unique=True, server_default="''::character varying")
    classname = Column(String(100), nullable=False, server_default="''::character varying")
    methodname = Column(String(100), nullable=False, server_default="''::character varying")
    classpath = Column(String(255))
    component = Column(String(100), nullable=False, server_default="''::character varying")
    capabilities = Column(String(255))


class ExternalService(Base):
    __tablename__ = 'ssismdl_external_services'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(200), nullable=False, unique=True, server_default="''::character varying")
    enabled = Column(SmallInteger, nullable=False)
    requiredcapability = Column(String(150))
    restrictedusers = Column(SmallInteger, nullable=False)
    component = Column(String(100))
    timecreated = Column(BigInteger, nullable=False)
    timemodified = Column(BigInteger)
    shortname = Column(String(255))
    downloadfiles = Column(SmallInteger, nullable=False, server_default='0')


class ExternalServicesFunction(Base):
    __tablename__ = 'ssismdl_external_services_functions'

    id = Column(BigInteger, primary_key=True)
    externalserviceid = Column(BigInteger, nullable=False, index=True)
    functionname = Column(String(200), nullable=False, server_default="''::character varying")


class ExternalServicesUser(Base):
    __tablename__ = 'ssismdl_external_services_users'

    id = Column(BigInteger, primary_key=True)
    externalserviceid = Column(BigInteger, nullable=False, index=True)
    userid = Column(BigInteger, nullable=False, index=True)
    iprestriction = Column(String(255))
    validuntil = Column(BigInteger)
    timecreated = Column(BigInteger)


class ExternalToken(Base):
    __tablename__ = 'ssismdl_external_tokens'

    id = Column(BigInteger, primary_key=True)
    token = Column(String(128), nullable=False, server_default="''::character varying")
    tokentype = Column(SmallInteger, nullable=False)
    userid = Column(BigInteger, nullable=False, index=True)
    externalserviceid = Column(BigInteger, nullable=False, index=True)
    sid = Column(String(128))
    contextid = Column(BigInteger, nullable=False, index=True)
    creatorid = Column(BigInteger, nullable=False, index=True, server_default='1')
    iprestriction = Column(String(255))
    validuntil = Column(BigInteger)
    timecreated = Column(BigInteger, nullable=False)
    lastaccess = Column(BigInteger)


class Feedback(Base):
    __tablename__ = 'ssismdl_feedback'

    id = Column(BigInteger, primary_key=True)
    course = Column(BigInteger, nullable=False, index=True, server_default='0')
    name = Column(String(255), nullable=False, server_default="''::character varying")
    intro = Column(Text, nullable=False)
    introformat = Column(SmallInteger, nullable=False, server_default='0')
    anonymous = Column(SmallInteger, nullable=False, server_default='1')
    email_notification = Column(SmallInteger, nullable=False, server_default='1')
    multiple_submit = Column(SmallInteger, nullable=False, server_default='1')
    autonumbering = Column(SmallInteger, nullable=False, server_default='1')
    site_after_submit = Column(String(255), nullable=False, server_default="''::character varying")
    page_after_submit = Column(Text, nullable=False)
    page_after_submitformat = Column(SmallInteger, nullable=False, server_default='0')
    publish_stats = Column(SmallInteger, nullable=False, server_default='0')
    timeopen = Column(BigInteger, nullable=False, server_default='0')
    timeclose = Column(BigInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')
    completionsubmit = Column(SmallInteger, nullable=False, server_default='0')


class FeedbackCompleted(Base):
    __tablename__ = 'ssismdl_feedback_completed'

    id = Column(BigInteger, primary_key=True)
    feedback = Column(BigInteger, nullable=False, index=True, server_default='0')
    userid = Column(BigInteger, nullable=False, index=True, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')
    random_response = Column(BigInteger, nullable=False, server_default='0')
    anonymous_response = Column(SmallInteger, nullable=False, server_default='0')


class FeedbackCompletedtmp(Base):
    __tablename__ = 'ssismdl_feedback_completedtmp'

    id = Column(BigInteger, primary_key=True)
    feedback = Column(BigInteger, nullable=False, index=True, server_default='0')
    userid = Column(BigInteger, nullable=False, index=True, server_default='0')
    guestid = Column(String(255), nullable=False, server_default="''::character varying")
    timemodified = Column(BigInteger, nullable=False, server_default='0')
    random_response = Column(BigInteger, nullable=False, server_default='0')
    anonymous_response = Column(SmallInteger, nullable=False, server_default='0')


class FeedbackItem(Base):
    __tablename__ = 'ssismdl_feedback_item'

    id = Column(BigInteger, primary_key=True)
    feedback = Column(BigInteger, nullable=False, index=True, server_default='0')
    template = Column(BigInteger, nullable=False, index=True, server_default='0')
    name = Column(String(255), nullable=False, server_default="''::character varying")
    label = Column(String(255), nullable=False, server_default="''::character varying")
    presentation = Column(Text, nullable=False)
    typ = Column(String(255), nullable=False, server_default="''::character varying")
    hasvalue = Column(SmallInteger, nullable=False, server_default='0')
    position = Column(SmallInteger, nullable=False, server_default='0')
    required = Column(SmallInteger, nullable=False, server_default='0')
    dependitem = Column(BigInteger, nullable=False, server_default='0')
    dependvalue = Column(String(255), nullable=False, server_default="''::character varying")
    options = Column(String(255), nullable=False, server_default="''::character varying")


class FeedbackSitecourseMap(Base):
    __tablename__ = 'ssismdl_feedback_sitecourse_map'

    id = Column(BigInteger, primary_key=True)
    feedbackid = Column(BigInteger, nullable=False, index=True, server_default='0')
    courseid = Column(BigInteger, nullable=False, index=True, server_default='0')


class FeedbackTemplate(Base):
    __tablename__ = 'ssismdl_feedback_template'

    id = Column(BigInteger, primary_key=True)
    course = Column(BigInteger, nullable=False, index=True, server_default='0')
    ispublic = Column(SmallInteger, nullable=False, server_default='0')
    name = Column(String(255), nullable=False, server_default="''::character varying")


class FeedbackTracking(Base):
    __tablename__ = 'ssismdl_feedback_tracking'

    id = Column(BigInteger, primary_key=True)
    userid = Column(BigInteger, nullable=False, index=True, server_default='0')
    feedback = Column(BigInteger, nullable=False, index=True, server_default='0')
    completed = Column(BigInteger, nullable=False, index=True, server_default='0')
    tmp_completed = Column(BigInteger, nullable=False, server_default='0')


class FeedbackValue(Base):
    __tablename__ = 'ssismdl_feedback_value'

    id = Column(BigInteger, primary_key=True)
    course_id = Column(BigInteger, nullable=False, index=True, server_default='0')
    item = Column(BigInteger, nullable=False, index=True, server_default='0')
    completed = Column(BigInteger, nullable=False, server_default='0')
    tmp_completed = Column(BigInteger, nullable=False, server_default='0')
    value = Column(Text, nullable=False)


class FeedbackValuetmp(Base):
    __tablename__ = 'ssismdl_feedback_valuetmp'

    id = Column(BigInteger, primary_key=True)
    course_id = Column(BigInteger, nullable=False, index=True, server_default='0')
    item = Column(BigInteger, nullable=False, index=True, server_default='0')
    completed = Column(BigInteger, nullable=False, server_default='0')
    tmp_completed = Column(BigInteger, nullable=False, server_default='0')
    value = Column(Text, nullable=False)


class File(Base):
    __tablename__ = 'ssismdl_files'
    __table_args__ = (
        Index('ssismdl_file_comfilconite_ix', 'component', 'filearea', 'contextid', 'itemid'),
    )

    id = Column(BigInteger, primary_key=True)
    contenthash = Column(String(40), nullable=False, index=True, server_default="''::character varying")
    pathnamehash = Column(String(40), nullable=False, unique=True, server_default="''::character varying")
    contextid = Column(BigInteger, nullable=False, index=True)
    component = Column(String(100), nullable=False, server_default="''::character varying")
    filearea = Column(String(50), nullable=False, server_default="''::character varying")
    itemid = Column(BigInteger, nullable=False)
    filepath = Column(String(255), nullable=False, server_default="''::character varying")
    filename = Column(String(255), nullable=False, server_default="''::character varying")
    userid = Column(BigInteger, index=True)
    filesize = Column(BigInteger, nullable=False)
    mimetype = Column(String(100))
    status = Column(BigInteger, nullable=False, server_default='0')
    source = Column(Text)
    author = Column(String(255))
    license = Column(String(255))
    timecreated = Column(BigInteger, nullable=False)
    timemodified = Column(BigInteger, nullable=False)
    sortorder = Column(BigInteger, nullable=False, server_default='0')
    referencefileid = Column(BigInteger, index=True)
    referencelastsync = Column(BigInteger)
    referencelifetime = Column(BigInteger)


class FilesReference(Base):
    __tablename__ = 'ssismdl_files_reference'
    __table_args__ = (
        Index('ssismdl_filerefe_repref_uix', 'repositoryid', 'referencehash'),
    )

    id = Column(BigInteger, primary_key=True)
    repositoryid = Column(BigInteger, nullable=False, index=True)
    lastsync = Column(BigInteger)
    lifetime = Column(BigInteger)
    reference = Column(Text)
    referencehash = Column(String(40), nullable=False, server_default="''::character varying")


class FilterActive(Base):
    __tablename__ = 'ssismdl_filter_active'
    __table_args__ = (
        Index('ssismdl_filtacti_confil_uix', 'contextid', 'filter'),
    )

    id = Column(BigInteger, primary_key=True)
    filter = Column(String(32), nullable=False, server_default="''::character varying")
    contextid = Column(BigInteger, nullable=False, index=True)
    active = Column(SmallInteger, nullable=False)
    sortorder = Column(BigInteger, nullable=False, server_default='0')


class FilterConfig(Base):
    __tablename__ = 'ssismdl_filter_config'
    __table_args__ = (
        Index('ssismdl_filtconf_confilnam_uix', 'contextid', 'filter', 'name'),
    )

    id = Column(BigInteger, primary_key=True)
    filter = Column(String(32), nullable=False, server_default="''::character varying")
    contextid = Column(BigInteger, nullable=False, index=True)
    name = Column(String(255), nullable=False, server_default="''::character varying")
    value = Column(Text)


class Flashcard(Base):
    __tablename__ = 'ssismdl_flashcard'

    id = Column(BigInteger, primary_key=True)
    course = Column(BigInteger, nullable=False, server_default='0')
    name = Column(String(255))
    intro = Column(Text, nullable=False)
    introformat = Column(SmallInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')
    starttime = Column(BigInteger)
    endtime = Column(BigInteger)
    questionid = Column(BigInteger, nullable=False, server_default='0')
    autodowngrade = Column(SmallInteger, nullable=False, server_default='1')
    decks = Column(SmallInteger, nullable=False, server_default='3')
    deck2_release = Column(BigInteger, nullable=False, server_default='96')
    deck3_release = Column(BigInteger, nullable=False, server_default='96')
    deck4_release = Column(BigInteger, nullable=False, server_default='96')
    deck1_delay = Column(BigInteger, nullable=False, server_default='48')
    deck2_delay = Column(BigInteger, nullable=False, server_default='96')
    deck3_delay = Column(BigInteger, nullable=False, server_default='168')
    deck4_delay = Column(BigInteger, nullable=False, server_default='376')
    questionsmediatype = Column(SmallInteger, nullable=False, server_default='0')
    answersmediatype = Column(SmallInteger, nullable=False, server_default='0')
    flipdeck = Column(SmallInteger, server_default='0')


class FlashcardCard(Base):
    __tablename__ = 'ssismdl_flashcard_card'

    id = Column(BigInteger, primary_key=True)
    flashcardid = Column(BigInteger, nullable=False)
    userid = Column(BigInteger)
    entryid = Column(BigInteger, nullable=False)
    deck = Column(BigInteger, nullable=False)
    lastaccessed = Column(BigInteger, server_default='0')
    accesscount = Column(BigInteger, nullable=False, server_default='0')


class FlashcardDeckdatum(Base):
    __tablename__ = 'ssismdl_flashcard_deckdata'

    id = Column(BigInteger, primary_key=True)
    flashcardid = Column(BigInteger, nullable=False, server_default='0')
    questiontext = Column(Text)
    answertext = Column(Text)


class Folder(Base):
    __tablename__ = 'ssismdl_folder'

    id = Column(BigInteger, primary_key=True)
    course = Column(BigInteger, nullable=False, index=True, server_default='0')
    name = Column(String(255), nullable=False, server_default="''::character varying")
    intro = Column(Text)
    introformat = Column(SmallInteger, nullable=False, server_default='0')
    revision = Column(BigInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')
    display = Column(SmallInteger, nullable=False, server_default='0')
    showexpanded = Column(SmallInteger, nullable=False, server_default='1')


class FormatGridIcon(Base):
    __tablename__ = 'ssismdl_format_grid_icon'

    id = Column(BigInteger, primary_key=True)
    imagepath = Column(Text)
    sectionid = Column(BigInteger, nullable=False, unique=True)
    courseid = Column(BigInteger, nullable=False, server_default='1')
    color = Column(String)


class FormatGridSummary(Base):
    __tablename__ = 'ssismdl_format_grid_summary'

    id = Column(BigInteger, primary_key=True)
    showsummary = Column(SmallInteger, nullable=False)
    courseid = Column(BigInteger, nullable=False)


class Forum(Base):
    __tablename__ = 'ssismdl_forum'

    id = Column(BigInteger, primary_key=True)
    course = Column(BigInteger, nullable=False, index=True, server_default='0')
    type = Column(String(20), nullable=False, server_default="'general'::character varying")
    name = Column(String(255), nullable=False, server_default="''::character varying")
    intro = Column(Text, nullable=False)
    introformat = Column(SmallInteger, nullable=False, server_default='0')
    assessed = Column(BigInteger, nullable=False, server_default='0')
    assesstimestart = Column(BigInteger, nullable=False, server_default='0')
    assesstimefinish = Column(BigInteger, nullable=False, server_default='0')
    scale = Column(BigInteger, nullable=False, server_default='0')
    maxbytes = Column(BigInteger, nullable=False, server_default='0')
    maxattachments = Column(BigInteger, nullable=False, server_default='1')
    forcesubscribe = Column(SmallInteger, nullable=False, server_default='0')
    trackingtype = Column(SmallInteger, nullable=False, server_default='1')
    rsstype = Column(SmallInteger, nullable=False, server_default='0')
    rssarticles = Column(SmallInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')
    warnafter = Column(BigInteger, nullable=False, server_default='0')
    blockafter = Column(BigInteger, nullable=False, server_default='0')
    blockperiod = Column(BigInteger, nullable=False, server_default='0')
    completiondiscussions = Column(Integer, nullable=False, server_default='0')
    completionreplies = Column(Integer, nullable=False, server_default='0')
    completionposts = Column(Integer, nullable=False, server_default='0')
    displaywordcount = Column(SmallInteger, nullable=False, server_default='0')


class ForumDiscussion(Base):
    __tablename__ = 'ssismdl_forum_discussions'

    id = Column(BigInteger, primary_key=True)
    course = Column(BigInteger, nullable=False, server_default='0')
    forum = Column(BigInteger, nullable=False, index=True, server_default='0')
    name = Column(String(255), nullable=False, server_default="''::character varying")
    firstpost = Column(BigInteger, nullable=False, server_default='0')
    userid = Column(BigInteger, nullable=False, index=True, server_default='0')
    groupid = Column(BigInteger, nullable=False, server_default='(-1)')
    assessed = Column(SmallInteger, nullable=False, server_default='1')
    timemodified = Column(BigInteger, nullable=False, server_default='0')
    usermodified = Column(BigInteger, nullable=False, server_default='0')
    timestart = Column(BigInteger, nullable=False, server_default='0')
    timeend = Column(BigInteger, nullable=False, server_default='0')


class ForumPost(Base):
    __tablename__ = 'ssismdl_forum_posts'

    id = Column(BigInteger, primary_key=True)
    discussion = Column(BigInteger, nullable=False, index=True, server_default='0')
    parent = Column(BigInteger, nullable=False, index=True, server_default='0')
    userid = Column(BigInteger, nullable=False, index=True, server_default='0')
    created = Column(BigInteger, nullable=False, index=True, server_default='0')
    modified = Column(BigInteger, nullable=False, server_default='0')
    mailed = Column(SmallInteger, nullable=False, index=True, server_default='0')
    subject = Column(String(255), nullable=False, server_default="''::character varying")
    message = Column(Text, nullable=False)
    messageformat = Column(SmallInteger, nullable=False, server_default='0')
    messagetrust = Column(SmallInteger, nullable=False, server_default='0')
    attachment = Column(String(100), nullable=False, server_default="''::character varying")
    totalscore = Column(SmallInteger, nullable=False, server_default='0')
    mailnow = Column(BigInteger, nullable=False, server_default='0')


class ForumQueue(Base):
    __tablename__ = 'ssismdl_forum_queue'

    id = Column(BigInteger, primary_key=True)
    userid = Column(BigInteger, nullable=False, index=True, server_default='0')
    discussionid = Column(BigInteger, nullable=False, index=True, server_default='0')
    postid = Column(BigInteger, nullable=False, index=True, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')


class ForumRead(Base):
    __tablename__ = 'ssismdl_forum_read'
    __table_args__ = (
        Index('ssismdl_foruread_usedis_ix', 'userid', 'discussionid'),
        Index('ssismdl_foruread_usepos_ix', 'userid', 'postid'),
        Index('ssismdl_foruread_usefor_ix', 'userid', 'forumid')
    )

    id = Column(BigInteger, primary_key=True)
    userid = Column(BigInteger, nullable=False, server_default='0')
    forumid = Column(BigInteger, nullable=False, server_default='0')
    discussionid = Column(BigInteger, nullable=False, server_default='0')
    postid = Column(BigInteger, nullable=False, server_default='0')
    firstread = Column(BigInteger, nullable=False, server_default='0')
    lastread = Column(BigInteger, nullable=False, server_default='0')


class ForumSubscription(Base):
    __tablename__ = 'ssismdl_forum_subscriptions'

    id = Column(BigInteger, primary_key=True)
    userid = Column(BigInteger, nullable=False, index=True, server_default='0')
    forum = Column(BigInteger, nullable=False, index=True, server_default='0')


class ForumTrackPref(Base):
    __tablename__ = 'ssismdl_forum_track_prefs'
    __table_args__ = (
        Index('ssismdl_forutracpref_usefor_ix', 'userid', 'forumid'),
    )

    id = Column(BigInteger, primary_key=True)
    userid = Column(BigInteger, nullable=False, server_default='0')
    forumid = Column(BigInteger, nullable=False, server_default='0')


class Glossary(Base):
    __tablename__ = 'ssismdl_glossary'

    id = Column(BigInteger, primary_key=True)
    course = Column(BigInteger, nullable=False, index=True, server_default='0')
    name = Column(String(255), nullable=False, server_default="''::character varying")
    intro = Column(Text, nullable=False)
    introformat = Column(SmallInteger, nullable=False, server_default='0')
    allowduplicatedentries = Column(SmallInteger, nullable=False, server_default='0')
    displayformat = Column(String(50), nullable=False, server_default="'dictionary'::character varying")
    mainglossary = Column(SmallInteger, nullable=False, server_default='0')
    showspecial = Column(SmallInteger, nullable=False, server_default='1')
    showalphabet = Column(SmallInteger, nullable=False, server_default='1')
    showall = Column(SmallInteger, nullable=False, server_default='1')
    allowcomments = Column(SmallInteger, nullable=False, server_default='0')
    allowprintview = Column(SmallInteger, nullable=False, server_default='1')
    usedynalink = Column(SmallInteger, nullable=False, server_default='1')
    defaultapproval = Column(SmallInteger, nullable=False, server_default='1')
    globalglossary = Column(SmallInteger, nullable=False, server_default='0')
    entbypage = Column(SmallInteger, nullable=False, server_default='10')
    editalways = Column(SmallInteger, nullable=False, server_default='0')
    rsstype = Column(SmallInteger, nullable=False, server_default='0')
    rssarticles = Column(SmallInteger, nullable=False, server_default='0')
    assessed = Column(BigInteger, nullable=False, server_default='0')
    assesstimestart = Column(BigInteger, nullable=False, server_default='0')
    assesstimefinish = Column(BigInteger, nullable=False, server_default='0')
    scale = Column(BigInteger, nullable=False, server_default='0')
    timecreated = Column(BigInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')
    completionentries = Column(Integer, nullable=False, server_default='0')
    approvaldisplayformat = Column(String(50), nullable=False, server_default="'default'::character varying")


class GlossaryAlia(Base):
    __tablename__ = 'ssismdl_glossary_alias'

    id = Column(BigInteger, primary_key=True)
    entryid = Column(BigInteger, nullable=False, index=True, server_default='0')
    alias = Column(String(255), nullable=False, server_default="''::character varying")


class GlossaryCategory(Base):
    __tablename__ = 'ssismdl_glossary_categories'

    id = Column(BigInteger, primary_key=True)
    glossaryid = Column(BigInteger, nullable=False, index=True, server_default='0')
    name = Column(String(255), nullable=False, server_default="''::character varying")
    usedynalink = Column(SmallInteger, nullable=False, server_default='1')


class GlossaryEntry(Base):
    __tablename__ = 'ssismdl_glossary_entries'

    id = Column(BigInteger, primary_key=True)
    glossaryid = Column(BigInteger, nullable=False, index=True, server_default='0')
    userid = Column(BigInteger, nullable=False, index=True, server_default='0')
    concept = Column(String(255), nullable=False, index=True, server_default="''::character varying")
    definition = Column(Text, nullable=False)
    definitionformat = Column(SmallInteger, nullable=False, server_default='0')
    definitiontrust = Column(SmallInteger, nullable=False, server_default='0')
    attachment = Column(String(100), nullable=False, server_default="''::character varying")
    timecreated = Column(BigInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')
    teacherentry = Column(SmallInteger, nullable=False, server_default='0')
    sourceglossaryid = Column(BigInteger, nullable=False, server_default='0')
    usedynalink = Column(SmallInteger, nullable=False, server_default='1')
    casesensitive = Column(SmallInteger, nullable=False, server_default='0')
    fullmatch = Column(SmallInteger, nullable=False, server_default='1')
    approved = Column(SmallInteger, nullable=False, server_default='1')


class GlossaryEntriesCategory(Base):
    __tablename__ = 'ssismdl_glossary_entries_categories'

    id = Column(BigInteger, primary_key=True)
    categoryid = Column(BigInteger, nullable=False, index=True, server_default='0')
    entryid = Column(BigInteger, nullable=False, index=True, server_default='0')


class GlossaryFormat(Base):
    __tablename__ = 'ssismdl_glossary_formats'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(50), nullable=False, server_default="''::character varying")
    popupformatname = Column(String(50), nullable=False, server_default="''::character varying")
    visible = Column(SmallInteger, nullable=False, server_default='1')
    showgroup = Column(SmallInteger, nullable=False, server_default='1')
    defaultmode = Column(String(50), nullable=False, server_default="''::character varying")
    defaulthook = Column(String(50), nullable=False, server_default="''::character varying")
    sortkey = Column(String(50), nullable=False, server_default="''::character varying")
    sortorder = Column(String(50), nullable=False, server_default="''::character varying")


class GradeCategory(Base):
    __tablename__ = 'ssismdl_grade_categories'

    id = Column(BigInteger, primary_key=True)
    courseid = Column(BigInteger, nullable=False, index=True)
    parent = Column(BigInteger, index=True)
    depth = Column(BigInteger, nullable=False, server_default='0')
    path = Column(String(255))
    fullname = Column(String(255), nullable=False, server_default="''::character varying")
    aggregation = Column(BigInteger, nullable=False, server_default='0')
    keephigh = Column(BigInteger, nullable=False, server_default='0')
    droplow = Column(BigInteger, nullable=False, server_default='0')
    aggregateonlygraded = Column(SmallInteger, nullable=False, server_default='0')
    aggregateoutcomes = Column(SmallInteger, nullable=False, server_default='0')
    aggregatesubcats = Column(SmallInteger, nullable=False, server_default='0')
    timecreated = Column(BigInteger, nullable=False)
    timemodified = Column(BigInteger, nullable=False)
    hidden = Column(SmallInteger, nullable=False, server_default='0')


class GradeCategoriesHistory(Base):
    __tablename__ = 'ssismdl_grade_categories_history'

    id = Column(BigInteger, primary_key=True)
    action = Column(BigInteger, nullable=False, index=True, server_default='0')
    oldid = Column(BigInteger, nullable=False, index=True)
    source = Column(String(255))
    timemodified = Column(BigInteger)
    loggeduser = Column(BigInteger, index=True)
    courseid = Column(BigInteger, nullable=False, index=True)
    parent = Column(BigInteger, index=True)
    depth = Column(BigInteger, nullable=False, server_default='0')
    path = Column(String(255))
    fullname = Column(String(255), nullable=False, server_default="''::character varying")
    aggregation = Column(BigInteger, nullable=False, server_default='0')
    keephigh = Column(BigInteger, nullable=False, server_default='0')
    droplow = Column(BigInteger, nullable=False, server_default='0')
    aggregateonlygraded = Column(SmallInteger, nullable=False, server_default='0')
    aggregateoutcomes = Column(SmallInteger, nullable=False, server_default='0')
    aggregatesubcats = Column(SmallInteger, nullable=False, server_default='0')
    hidden = Column(SmallInteger, nullable=False, server_default='0')


class GradeGrade(Base):
    __tablename__ = 'ssismdl_grade_grades'
    __table_args__ = (
        Index('ssismdl_gradgrad_useite_uix', 'userid', 'itemid'),
        Index('ssismdl_gradgrad_locloc_ix', 'locked', 'locktime')
    )

    id = Column(BigInteger, primary_key=True)
    itemid = Column(BigInteger, nullable=False, index=True)
    userid = Column(BigInteger, nullable=False, index=True)
    rawgrade = Column(Numeric(10, 5))
    rawgrademax = Column(Numeric(10, 5), nullable=False, server_default='100')
    rawgrademin = Column(Numeric(10, 5), nullable=False, server_default='0')
    rawscaleid = Column(BigInteger, index=True)
    usermodified = Column(BigInteger, index=True)
    finalgrade = Column(Numeric(10, 5))
    hidden = Column(BigInteger, nullable=False, server_default='0')
    locked = Column(BigInteger, nullable=False, server_default='0')
    locktime = Column(BigInteger, nullable=False, server_default='0')
    exported = Column(BigInteger, nullable=False, server_default='0')
    overridden = Column(BigInteger, nullable=False, server_default='0')
    excluded = Column(BigInteger, nullable=False, server_default='0')
    feedback = Column(Text)
    feedbackformat = Column(BigInteger, nullable=False, server_default='0')
    information = Column(Text)
    informationformat = Column(BigInteger, nullable=False, server_default='0')
    timecreated = Column(BigInteger)
    timemodified = Column(BigInteger)


class GradeGradesHistory(Base):
    __tablename__ = 'ssismdl_grade_grades_history'

    id = Column(BigInteger, primary_key=True)
    action = Column(BigInteger, nullable=False, index=True, server_default='0')
    oldid = Column(BigInteger, nullable=False, index=True)
    source = Column(String(255))
    timemodified = Column(BigInteger, index=True)
    loggeduser = Column(BigInteger, index=True)
    itemid = Column(BigInteger, nullable=False, index=True)
    userid = Column(BigInteger, nullable=False, index=True)
    rawgrade = Column(Numeric(10, 5))
    rawgrademax = Column(Numeric(10, 5), nullable=False, server_default='100')
    rawgrademin = Column(Numeric(10, 5), nullable=False, server_default='0')
    rawscaleid = Column(BigInteger, index=True)
    usermodified = Column(BigInteger, index=True)
    finalgrade = Column(Numeric(10, 5))
    hidden = Column(BigInteger, nullable=False, server_default='0')
    locked = Column(BigInteger, nullable=False, server_default='0')
    locktime = Column(BigInteger, nullable=False, server_default='0')
    exported = Column(BigInteger, nullable=False, server_default='0')
    overridden = Column(BigInteger, nullable=False, server_default='0')
    excluded = Column(BigInteger, nullable=False, server_default='0')
    feedback = Column(Text)
    feedbackformat = Column(BigInteger, nullable=False, server_default='0')
    information = Column(Text)
    informationformat = Column(BigInteger, nullable=False, server_default='0')


class GradeImportNewitem(Base):
    __tablename__ = 'ssismdl_grade_import_newitem'

    id = Column(BigInteger, primary_key=True)
    itemname = Column(String(255), nullable=False, server_default="''::character varying")
    importcode = Column(BigInteger, nullable=False)
    importer = Column(BigInteger, nullable=False, index=True)


class GradeImportValue(Base):
    __tablename__ = 'ssismdl_grade_import_values'

    id = Column(BigInteger, primary_key=True)
    itemid = Column(BigInteger, index=True)
    newgradeitem = Column(BigInteger, index=True)
    userid = Column(BigInteger, nullable=False)
    finalgrade = Column(Numeric(10, 5))
    feedback = Column(Text)
    importcode = Column(BigInteger, nullable=False)
    importer = Column(BigInteger, index=True)


class GradeItem(Base):
    __tablename__ = 'ssismdl_grade_items'
    __table_args__ = (
        Index('ssismdl_graditem_itenee_ix', 'itemtype', 'needsupdate'),
        Index('ssismdl_graditem_idncou_ix', 'idnumber', 'courseid'),
        Index('ssismdl_graditem_locloc_ix', 'locked', 'locktime')
    )

    id = Column(BigInteger, primary_key=True)
    courseid = Column(BigInteger, index=True)
    categoryid = Column(BigInteger, index=True)
    itemname = Column(String(255))
    itemtype = Column(String(30), nullable=False, server_default="''::character varying")
    itemmodule = Column(String(30))
    iteminstance = Column(BigInteger)
    itemnumber = Column(BigInteger)
    iteminfo = Column(Text)
    idnumber = Column(String(255))
    calculation = Column(Text)
    gradetype = Column(SmallInteger, nullable=False, index=True, server_default='1')
    grademax = Column(Numeric(10, 5), nullable=False, server_default='100')
    grademin = Column(Numeric(10, 5), nullable=False, server_default='0')
    scaleid = Column(BigInteger, index=True)
    outcomeid = Column(BigInteger, index=True)
    gradepass = Column(Numeric(10, 5), nullable=False, server_default='0')
    multfactor = Column(Numeric(10, 5), nullable=False, server_default='1.0')
    plusfactor = Column(Numeric(10, 5), nullable=False, server_default='0')
    aggregationcoef = Column(Numeric(10, 5), nullable=False, server_default='0')
    sortorder = Column(BigInteger, nullable=False, server_default='0')
    display = Column(BigInteger, nullable=False, server_default='0')
    decimals = Column(SmallInteger)
    hidden = Column(BigInteger, nullable=False, server_default='0')
    locked = Column(BigInteger, nullable=False, server_default='0')
    locktime = Column(BigInteger, nullable=False, server_default='0')
    needsupdate = Column(BigInteger, nullable=False, server_default='0')
    timecreated = Column(BigInteger)
    timemodified = Column(BigInteger)


class GradeItemsHistory(Base):
    __tablename__ = 'ssismdl_grade_items_history'

    id = Column(BigInteger, primary_key=True)
    action = Column(BigInteger, nullable=False, index=True, server_default='0')
    oldid = Column(BigInteger, nullable=False, index=True)
    source = Column(String(255))
    timemodified = Column(BigInteger)
    loggeduser = Column(BigInteger, index=True)
    courseid = Column(BigInteger, index=True)
    categoryid = Column(BigInteger, index=True)
    itemname = Column(String(255))
    itemtype = Column(String(30), nullable=False, server_default="''::character varying")
    itemmodule = Column(String(30))
    iteminstance = Column(BigInteger)
    itemnumber = Column(BigInteger)
    iteminfo = Column(Text)
    idnumber = Column(String(255))
    calculation = Column(Text)
    gradetype = Column(SmallInteger, nullable=False, server_default='1')
    grademax = Column(Numeric(10, 5), nullable=False, server_default='100')
    grademin = Column(Numeric(10, 5), nullable=False, server_default='0')
    scaleid = Column(BigInteger, index=True)
    outcomeid = Column(BigInteger, index=True)
    gradepass = Column(Numeric(10, 5), nullable=False, server_default='0')
    multfactor = Column(Numeric(10, 5), nullable=False, server_default='1.0')
    plusfactor = Column(Numeric(10, 5), nullable=False, server_default='0')
    aggregationcoef = Column(Numeric(10, 5), nullable=False, server_default='0')
    sortorder = Column(BigInteger, nullable=False, server_default='0')
    hidden = Column(BigInteger, nullable=False, server_default='0')
    locked = Column(BigInteger, nullable=False, server_default='0')
    locktime = Column(BigInteger, nullable=False, server_default='0')
    needsupdate = Column(BigInteger, nullable=False, server_default='0')
    display = Column(BigInteger, nullable=False, server_default='0')
    decimals = Column(SmallInteger)


class GradeLetter(Base):
    __tablename__ = 'ssismdl_grade_letters'
    __table_args__ = (
        Index('ssismdl_gradlett_conlowlet_uix', 'contextid', 'lowerboundary', 'letter'),
    )

    id = Column(BigInteger, primary_key=True)
    contextid = Column(BigInteger, nullable=False)
    lowerboundary = Column(Numeric(10, 5), nullable=False)
    letter = Column(String(255), nullable=False, server_default="''::character varying")


class GradeOutcome(Base):
    __tablename__ = 'ssismdl_grade_outcomes'
    __table_args__ = (
        Index('ssismdl_gradoutc_cousho_uix', 'courseid', 'shortname'),
    )

    id = Column(BigInteger, primary_key=True)
    courseid = Column(BigInteger, index=True)
    shortname = Column(String(255), nullable=False, server_default="''::character varying")
    fullname = Column(Text, nullable=False)
    scaleid = Column(BigInteger, index=True)
    description = Column(Text)
    descriptionformat = Column(SmallInteger, nullable=False, server_default='0')
    timecreated = Column(BigInteger)
    timemodified = Column(BigInteger)
    usermodified = Column(BigInteger, index=True)


class GradeOutcomesCourse(Base):
    __tablename__ = 'ssismdl_grade_outcomes_courses'
    __table_args__ = (
        Index('ssismdl_gradoutccour_couou_uix', 'courseid', 'outcomeid'),
    )

    id = Column(BigInteger, primary_key=True)
    courseid = Column(BigInteger, nullable=False, index=True)
    outcomeid = Column(BigInteger, nullable=False, index=True)


class GradeOutcomesHistory(Base):
    __tablename__ = 'ssismdl_grade_outcomes_history'

    id = Column(BigInteger, primary_key=True)
    action = Column(BigInteger, nullable=False, index=True, server_default='0')
    oldid = Column(BigInteger, nullable=False, index=True)
    source = Column(String(255))
    timemodified = Column(BigInteger)
    loggeduser = Column(BigInteger, index=True)
    courseid = Column(BigInteger, index=True)
    shortname = Column(String(255), nullable=False, server_default="''::character varying")
    fullname = Column(Text, nullable=False)
    scaleid = Column(BigInteger, index=True)
    description = Column(Text)
    descriptionformat = Column(SmallInteger, nullable=False, server_default='0')


class GradeSetting(Base):
    __tablename__ = 'ssismdl_grade_settings'
    __table_args__ = (
        Index('ssismdl_gradsett_counam_uix', 'courseid', 'name'),
    )

    id = Column(BigInteger, primary_key=True)
    courseid = Column(BigInteger, nullable=False, index=True)
    name = Column(String(255), nullable=False, server_default="''::character varying")
    value = Column(Text)


class GradingArea(Base):
    __tablename__ = 'ssismdl_grading_areas'
    __table_args__ = (
        Index('ssismdl_gradarea_concomare_uix', 'contextid', 'component', 'areaname'),
    )

    id = Column(BigInteger, primary_key=True)
    contextid = Column(BigInteger, nullable=False, index=True)
    component = Column(String(100), nullable=False, server_default="''::character varying")
    areaname = Column(String(100), nullable=False, server_default="''::character varying")
    activemethod = Column(String(100))


class GradingDefinition(Base):
    __tablename__ = 'ssismdl_grading_definitions'
    __table_args__ = (
        Index('ssismdl_graddefi_aremet_uix', 'areaid', 'method'),
    )

    id = Column(BigInteger, primary_key=True)
    areaid = Column(BigInteger, nullable=False, index=True)
    method = Column(String(100), nullable=False, server_default="''::character varying")
    name = Column(String(255), nullable=False, server_default="''::character varying")
    description = Column(Text)
    descriptionformat = Column(SmallInteger)
    status = Column(BigInteger, nullable=False, server_default='0')
    copiedfromid = Column(BigInteger)
    timecreated = Column(BigInteger, nullable=False)
    usercreated = Column(BigInteger, nullable=False, index=True)
    timemodified = Column(BigInteger, nullable=False)
    usermodified = Column(BigInteger, nullable=False, index=True)
    timecopied = Column(BigInteger, server_default='0')
    options = Column(Text)


class GradingInstance(Base):
    __tablename__ = 'ssismdl_grading_instances'

    id = Column(BigInteger, primary_key=True)
    definitionid = Column(BigInteger, nullable=False, index=True)
    raterid = Column(BigInteger, nullable=False, index=True)
    itemid = Column(BigInteger)
    rawgrade = Column(Numeric(10, 5))
    status = Column(BigInteger, nullable=False, server_default='0')
    feedback = Column(Text)
    feedbackformat = Column(SmallInteger)
    timemodified = Column(BigInteger, nullable=False)


class GradingformGuideComment(Base):
    __tablename__ = 'ssismdl_gradingform_guide_comments'

    id = Column(BigInteger, primary_key=True)
    definitionid = Column(BigInteger, nullable=False, index=True)
    sortorder = Column(BigInteger, nullable=False)
    description = Column(Text)
    descriptionformat = Column(SmallInteger)


class GradingformGuideCriterion(Base):
    __tablename__ = 'ssismdl_gradingform_guide_criteria'

    id = Column(BigInteger, primary_key=True)
    definitionid = Column(BigInteger, nullable=False, index=True)
    sortorder = Column(BigInteger, nullable=False)
    shortname = Column(String(255), nullable=False, server_default="''::character varying")
    description = Column(Text)
    descriptionformat = Column(SmallInteger)
    descriptionmarkers = Column(Text)
    descriptionmarkersformat = Column(SmallInteger)
    maxscore = Column(Numeric(10, 5), nullable=False)


class GradingformGuideFilling(Base):
    __tablename__ = 'ssismdl_gradingform_guide_fillings'
    __table_args__ = (
        Index('ssismdl_gradguidfill_inscr_uix', 'instanceid', 'criterionid'),
    )

    id = Column(BigInteger, primary_key=True)
    instanceid = Column(BigInteger, nullable=False, index=True)
    criterionid = Column(BigInteger, nullable=False, index=True)
    remark = Column(Text)
    remarkformat = Column(SmallInteger)
    score = Column(Numeric(10, 5), nullable=False)


class GradingformRubricCriterion(Base):
    __tablename__ = 'ssismdl_gradingform_rubric_criteria'

    id = Column(BigInteger, primary_key=True)
    definitionid = Column(BigInteger, nullable=False, index=True)
    sortorder = Column(BigInteger, nullable=False)
    description = Column(Text)
    descriptionformat = Column(SmallInteger)


class GradingformRubricFilling(Base):
    __tablename__ = 'ssismdl_gradingform_rubric_fillings'
    __table_args__ = (
        Index('ssismdl_gradrubrfill_inscr_uix', 'instanceid', 'criterionid'),
    )

    id = Column(BigInteger, primary_key=True)
    instanceid = Column(BigInteger, nullable=False, index=True)
    criterionid = Column(BigInteger, nullable=False, index=True)
    levelid = Column(BigInteger, index=True)
    remark = Column(Text)
    remarkformat = Column(SmallInteger)


class GradingformRubricLevel(Base):
    __tablename__ = 'ssismdl_gradingform_rubric_levels'

    id = Column(BigInteger, primary_key=True)
    criterionid = Column(BigInteger, nullable=False, index=True)
    score = Column(Numeric(10, 5), nullable=False)
    definition = Column(Text)
    definitionformat = Column(BigInteger)


class Grouping(Base):
    __tablename__ = 'ssismdl_groupings'

    id = Column(BigInteger, primary_key=True)
    courseid = Column(BigInteger, nullable=False, index=True, server_default='0')
    name = Column(String(255), nullable=False, server_default="''::character varying")
    description = Column(Text)
    descriptionformat = Column(SmallInteger, nullable=False, server_default='0')
    configdata = Column(Text)
    timecreated = Column(BigInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')
    idnumber = Column(String(100), nullable=False, index=True, server_default="''::character varying")


class GroupingsGroup(Base):
    __tablename__ = 'ssismdl_groupings_groups'

    id = Column(BigInteger, primary_key=True)
    groupingid = Column(BigInteger, nullable=False, index=True, server_default='0')
    groupid = Column(BigInteger, nullable=False, index=True, server_default='0')
    timeadded = Column(BigInteger, nullable=False, server_default='0')


class Group(Base):
    __tablename__ = 'ssismdl_groups'

    id = Column(BigInteger, primary_key=True)
    courseid = Column(BigInteger, nullable=False, index=True)
    name = Column(String(254), nullable=False, server_default="''::character varying")
    description = Column(Text)
    descriptionformat = Column(SmallInteger, nullable=False, server_default='0')
    enrolmentkey = Column(String(50))
    picture = Column(BigInteger, nullable=False, server_default='0')
    hidepicture = Column(SmallInteger, nullable=False, server_default='0')
    timecreated = Column(BigInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')
    idnumber = Column(String(100), nullable=False, index=True, server_default="''::character varying")


class GroupsMember(Base):
    __tablename__ = 'ssismdl_groups_members'

    id = Column(BigInteger, primary_key=True)
    groupid = Column(BigInteger, nullable=False, index=True, server_default='0')
    userid = Column(BigInteger, nullable=False, index=True, server_default='0')
    timeadded = Column(BigInteger, nullable=False, server_default='0')
    component = Column(String(100), nullable=False, server_default="''::character varying")
    itemid = Column(BigInteger, nullable=False, server_default='0')


class Htmltable(Base):
    __tablename__ = 'ssismdl_htmltable'

    id = Column(BigInteger, primary_key=True)
    course = Column(BigInteger, nullable=False, index=True, server_default='0')
    name = Column(String(255), nullable=False, server_default="''::character varying")
    intro = Column(Text)
    introformat = Column(SmallInteger, nullable=False, server_default='0')
    content = Column(Text)
    contentformat = Column(SmallInteger, nullable=False, server_default='0')
    legacyfiles = Column(SmallInteger, nullable=False, server_default='0')
    legacyfileslast = Column(BigInteger)
    display = Column(SmallInteger, nullable=False, server_default='0')
    displayoptions = Column(Text)
    revision = Column(BigInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')


class Imscp(Base):
    __tablename__ = 'ssismdl_imscp'

    id = Column(BigInteger, primary_key=True)
    course = Column(BigInteger, nullable=False, index=True, server_default='0')
    name = Column(String(255), nullable=False, server_default="''::character varying")
    intro = Column(Text)
    introformat = Column(SmallInteger, nullable=False, server_default='0')
    revision = Column(BigInteger, nullable=False, server_default='0')
    keepold = Column(BigInteger, nullable=False, server_default='(-1)')
    structure = Column(Text)
    timemodified = Column(BigInteger, nullable=False, server_default='0')


class Journal(Base):
    __tablename__ = 'ssismdl_journal'

    id = Column(BigInteger, primary_key=True)
    course = Column(BigInteger, nullable=False, index=True, server_default='0')
    name = Column(String(255), nullable=False, server_default="''::character varying")
    intro = Column(Text, nullable=False)
    introformat = Column(SmallInteger, nullable=False, server_default='0')
    days = Column(Integer, nullable=False, server_default='7')
    grade = Column(BigInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')


class JournalEntry(Base):
    __tablename__ = 'ssismdl_journal_entries'

    id = Column(BigInteger, primary_key=True)
    journal = Column(BigInteger, nullable=False, index=True, server_default='0')
    userid = Column(BigInteger, nullable=False, index=True, server_default='0')
    modified = Column(BigInteger, nullable=False, server_default='0')
    text = Column(Text, nullable=False)
    format = Column(SmallInteger, nullable=False, server_default='0')
    rating = Column(BigInteger)
    entrycomment = Column(Text)
    teacher = Column(BigInteger, nullable=False, server_default='0')
    timemarked = Column(BigInteger, nullable=False, server_default='0')
    mailed = Column(SmallInteger, nullable=False, server_default='0')


class Label(Base):
    __tablename__ = 'ssismdl_label'

    id = Column(BigInteger, primary_key=True)
    course = Column(BigInteger, nullable=False, index=True, server_default='0')
    name = Column(String(255), nullable=False, server_default="''::character varying")
    intro = Column(Text, nullable=False)
    introformat = Column(SmallInteger, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')


class Lesson(Base):
    __tablename__ = 'ssismdl_lesson'

    id = Column(BigInteger, primary_key=True)
    course = Column(BigInteger, nullable=False, index=True, server_default='0')
    name = Column(String(255), nullable=False, server_default="''::character varying")
    practice = Column(SmallInteger, nullable=False, server_default='0')
    modattempts = Column(SmallInteger, nullable=False, server_default='0')
    usepassword = Column(SmallInteger, nullable=False, server_default='0')
    password = Column(String(32), nullable=False, server_default="''::character varying")
    dependency = Column(BigInteger, nullable=False, server_default='0')
    conditions = Column(Text, nullable=False)
    grade = Column(SmallInteger, nullable=False, server_default='0')
    custom = Column(SmallInteger, nullable=False, server_default='0')
    ongoing = Column(SmallInteger, nullable=False, server_default='0')
    usemaxgrade = Column(SmallInteger, nullable=False, server_default='0')
    maxanswers = Column(SmallInteger, nullable=False, server_default='4')
    maxattempts = Column(SmallInteger, nullable=False, server_default='5')
    review = Column(SmallInteger, nullable=False, server_default='0')
    nextpagedefault = Column(SmallInteger, nullable=False, server_default='0')
    feedback = Column(SmallInteger, nullable=False, server_default='1')
    minquestions = Column(SmallInteger, nullable=False, server_default='0')
    maxpages = Column(SmallInteger, nullable=False, server_default='0')
    timed = Column(SmallInteger, nullable=False, server_default='0')
    maxtime = Column(BigInteger, nullable=False, server_default='0')
    retake = Column(SmallInteger, nullable=False, server_default='1')
    activitylink = Column(BigInteger, nullable=False, server_default='0')
    mediafile = Column(String(255), nullable=False, server_default="''::character varying")
    mediaheight = Column(BigInteger, nullable=False, server_default='100')
    mediawidth = Column(BigInteger, nullable=False, server_default='650')
    mediaclose = Column(SmallInteger, nullable=False, server_default='0')
    slideshow = Column(SmallInteger, nullable=False, server_default='0')
    width = Column(BigInteger, nullable=False, server_default='640')
    height = Column(BigInteger, nullable=False, server_default='480')
    bgcolor = Column(String(7), nullable=False, server_default="'#FFFFFF'::character varying")
    displayleft = Column(SmallInteger, nullable=False, server_default='0')
    displayleftif = Column(SmallInteger, nullable=False, server_default='0')
    progressbar = Column(SmallInteger, nullable=False, server_default='0')
    highscores = Column(SmallInteger, nullable=False, server_default='0')
    maxhighscores = Column(BigInteger, nullable=False, server_default='0')
    available = Column(BigInteger, nullable=False, server_default='0')
    deadline = Column(BigInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')


class LessonAnswer(Base):
    __tablename__ = 'ssismdl_lesson_answers'

    id = Column(BigInteger, primary_key=True)
    lessonid = Column(BigInteger, nullable=False, index=True, server_default='0')
    pageid = Column(BigInteger, nullable=False, index=True, server_default='0')
    jumpto = Column(BigInteger, nullable=False, server_default='0')
    grade = Column(SmallInteger, nullable=False, server_default='0')
    score = Column(BigInteger, nullable=False, server_default='0')
    flags = Column(SmallInteger, nullable=False, server_default='0')
    timecreated = Column(BigInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')
    answer = Column(Text)
    answerformat = Column(SmallInteger, nullable=False, server_default='0')
    response = Column(Text)
    responseformat = Column(SmallInteger, nullable=False, server_default='0')


class LessonAttempt(Base):
    __tablename__ = 'ssismdl_lesson_attempts'

    id = Column(BigInteger, primary_key=True)
    lessonid = Column(BigInteger, nullable=False, index=True, server_default='0')
    pageid = Column(BigInteger, nullable=False, index=True, server_default='0')
    userid = Column(BigInteger, nullable=False, index=True, server_default='0')
    answerid = Column(BigInteger, nullable=False, index=True, server_default='0')
    retry = Column(SmallInteger, nullable=False, server_default='0')
    correct = Column(BigInteger, nullable=False, server_default='0')
    useranswer = Column(Text)
    timeseen = Column(BigInteger, nullable=False, server_default='0')


class LessonBranch(Base):
    __tablename__ = 'ssismdl_lesson_branch'

    id = Column(BigInteger, primary_key=True)
    lessonid = Column(BigInteger, nullable=False, index=True, server_default='0')
    userid = Column(BigInteger, nullable=False, index=True, server_default='0')
    pageid = Column(BigInteger, nullable=False, index=True, server_default='0')
    retry = Column(BigInteger, nullable=False, server_default='0')
    flag = Column(SmallInteger, nullable=False, server_default='0')
    timeseen = Column(BigInteger, nullable=False, server_default='0')


class LessonGrade(Base):
    __tablename__ = 'ssismdl_lesson_grades'

    id = Column(BigInteger, primary_key=True)
    lessonid = Column(BigInteger, nullable=False, index=True, server_default='0')
    userid = Column(BigInteger, nullable=False, index=True, server_default='0')
    grade = Column(Float(53), nullable=False, server_default='0')
    late = Column(SmallInteger, nullable=False, server_default='0')
    completed = Column(BigInteger, nullable=False, server_default='0')


class LessonHighScore(Base):
    __tablename__ = 'ssismdl_lesson_high_scores'

    id = Column(BigInteger, primary_key=True)
    lessonid = Column(BigInteger, nullable=False, index=True, server_default='0')
    userid = Column(BigInteger, nullable=False, index=True, server_default='0')
    gradeid = Column(BigInteger, nullable=False, server_default='0')
    nickname = Column(String(5), nullable=False, server_default="''::character varying")


class LessonPage(Base):
    __tablename__ = 'ssismdl_lesson_pages'

    id = Column(BigInteger, primary_key=True)
    lessonid = Column(BigInteger, nullable=False, index=True, server_default='0')
    prevpageid = Column(BigInteger, nullable=False, server_default='0')
    nextpageid = Column(BigInteger, nullable=False, server_default='0')
    qtype = Column(SmallInteger, nullable=False, server_default='0')
    qoption = Column(SmallInteger, nullable=False, server_default='0')
    layout = Column(SmallInteger, nullable=False, server_default='1')
    display = Column(SmallInteger, nullable=False, server_default='1')
    timecreated = Column(BigInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')
    title = Column(String(255), nullable=False, server_default="''::character varying")
    contents = Column(Text, nullable=False)
    contentsformat = Column(SmallInteger, nullable=False, server_default='0')


class LessonTimer(Base):
    __tablename__ = 'ssismdl_lesson_timer'

    id = Column(BigInteger, primary_key=True)
    lessonid = Column(BigInteger, nullable=False, index=True, server_default='0')
    userid = Column(BigInteger, nullable=False, index=True, server_default='0')
    starttime = Column(BigInteger, nullable=False, server_default='0')
    lessontime = Column(BigInteger, nullable=False, server_default='0')


class License(Base):
    __tablename__ = 'ssismdl_license'

    id = Column(BigInteger, primary_key=True)
    shortname = Column(String(255))
    fullname = Column(Text)
    source = Column(String(255))
    enabled = Column(SmallInteger, nullable=False, server_default='1')
    version = Column(BigInteger, nullable=False, server_default='0')


class Lightboxgallery(Base):
    __tablename__ = 'ssismdl_lightboxgallery'

    id = Column(BigInteger, primary_key=True)
    course = Column(BigInteger, nullable=False, index=True, server_default='0')
    folder = Column(String(255), nullable=False, server_default="''::character varying")
    name = Column(String(255), nullable=False, server_default="''::character varying")
    perpage = Column(SmallInteger, nullable=False, server_default='0')
    perrow = Column(SmallInteger, nullable=False, server_default='0')
    comments = Column(SmallInteger, nullable=False, server_default='0')
    ispublic = Column(SmallInteger, nullable=False, server_default='0')
    rss = Column(SmallInteger, nullable=False, server_default='0')
    autoresize = Column(SmallInteger, nullable=False, server_default='0')
    resize = Column(SmallInteger, nullable=False, server_default='0')
    extinfo = Column(SmallInteger, nullable=False, server_default='0')
    captionfull = Column(SmallInteger, nullable=False, server_default='0')
    captionpos = Column(SmallInteger, nullable=False, server_default='0')
    intro = Column(Text)
    introformat = Column(SmallInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')


class LightboxgalleryComment(Base):
    __tablename__ = 'ssismdl_lightboxgallery_comments'

    id = Column(BigInteger, primary_key=True)
    gallery = Column(BigInteger, nullable=False, index=True, server_default='0')
    userid = Column(BigInteger, nullable=False, server_default='0')
    commenttext = Column(Text, nullable=False)
    timemodified = Column(BigInteger, nullable=False, server_default='0')


class LightboxgalleryImageMeta(Base):
    __tablename__ = 'ssismdl_lightboxgallery_image_meta'

    id = Column(BigInteger, primary_key=True)
    gallery = Column(BigInteger, nullable=False, index=True, server_default='0')
    image = Column(String(255), nullable=False, server_default="''::character varying")
    metatype = Column(String(20), nullable=False, server_default="'caption'::character varying")
    description = Column(Text, nullable=False)


class LocalDnetDestiny(Base):
    __tablename__ = 'ssismdl_local_dnet_destiny'

    id = Column(BigInteger, primary_key=True)


class Log(Base):
    __tablename__ = 'ssismdl_log'
    __table_args__ = (
        Index('ssismdl_log_usecou_ix', 'userid', 'course'),
        Index('ssismdl_log_coumodact_ix', 'course', 'module', 'action')
    )

    id = Column(BigInteger, primary_key=True)
    time = Column(BigInteger, nullable=False, index=True, server_default='0')
    userid = Column(BigInteger, nullable=False, server_default='0')
    ip = Column(String(45), nullable=False, server_default="''::character varying")
    course = Column(BigInteger, nullable=False, server_default='0')
    module = Column(String(20), nullable=False, server_default="''::character varying")
    cmid = Column(BigInteger, nullable=False, index=True, server_default='0')
    action = Column(String(40), nullable=False, index=True, server_default="''::character varying")
    url = Column(String(100), nullable=False, server_default="''::character varying")
    info = Column(String(255), nullable=False, server_default="''::character varying")


class LogDisplay(Base):
    __tablename__ = 'ssismdl_log_display'
    __table_args__ = (
        Index('ssismdl_logdisp_modact_uix', 'module', 'action'),
    )

    id = Column(BigInteger, primary_key=True)
    module = Column(String(20), nullable=False, server_default="''::character varying")
    action = Column(String(40), nullable=False, server_default="''::character varying")
    mtable = Column(String(30), nullable=False, server_default="''::character varying")
    field = Column(String(200), nullable=False, server_default="''::character varying")
    component = Column(String(100), nullable=False, server_default="''::character varying")


class LogQuery(Base):
    __tablename__ = 'ssismdl_log_queries'

    id = Column(BigInteger, primary_key=True)
    qtype = Column(Integer, nullable=False)
    sqltext = Column(Text, nullable=False)
    sqlparams = Column(Text)
    error = Column(Integer, nullable=False, server_default='0')
    info = Column(Text)
    backtrace = Column(Text)
    exectime = Column(Numeric(10, 5), nullable=False)
    timelogged = Column(BigInteger, nullable=False)


class Lti(Base):
    __tablename__ = 'ssismdl_lti'

    id = Column(BigInteger, primary_key=True)
    course = Column(BigInteger, nullable=False, index=True, server_default='0')
    name = Column(String(255), nullable=False, server_default="''::character varying")
    intro = Column(Text)
    introformat = Column(SmallInteger, server_default='0')
    timecreated = Column(BigInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')
    typeid = Column(BigInteger)
    toolurl = Column(Text, nullable=False)
    securetoolurl = Column(Text)
    instructorchoicesendname = Column(SmallInteger)
    instructorchoicesendemailaddr = Column(SmallInteger)
    instructorchoiceallowroster = Column(SmallInteger)
    instructorchoiceallowsetting = Column(SmallInteger)
    instructorcustomparameters = Column(String(255))
    instructorchoiceacceptgrades = Column(SmallInteger)
    grade = Column(Numeric(10, 5), nullable=False, server_default='100')
    launchcontainer = Column(SmallInteger, nullable=False, server_default='1')
    resourcekey = Column(String(255))
    password = Column(String(255))
    debuglaunch = Column(SmallInteger, nullable=False, server_default='0')
    showtitlelaunch = Column(SmallInteger, nullable=False, server_default='0')
    showdescriptionlaunch = Column(SmallInteger, nullable=False, server_default='0')
    servicesalt = Column(String(40))
    icon = Column(Text)
    secureicon = Column(Text)


class LtiSubmission(Base):
    __tablename__ = 'ssismdl_lti_submission'

    id = Column(BigInteger, primary_key=True)
    ltiid = Column(BigInteger, nullable=False, index=True)
    userid = Column(BigInteger, nullable=False)
    datesubmitted = Column(BigInteger, nullable=False)
    dateupdated = Column(BigInteger, nullable=False)
    gradepercent = Column(Numeric(10, 5), nullable=False)
    originalgrade = Column(Numeric(10, 5), nullable=False)
    launchid = Column(BigInteger, nullable=False)
    state = Column(SmallInteger, nullable=False)


class LtiType(Base):
    __tablename__ = 'ssismdl_lti_types'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(255), nullable=False, server_default="'basiclti Activity'::character varying")
    baseurl = Column(Text, nullable=False)
    tooldomain = Column(String(255), nullable=False, index=True, server_default="''::character varying")
    state = Column(SmallInteger, nullable=False, server_default='2')
    course = Column(BigInteger, nullable=False, index=True)
    coursevisible = Column(SmallInteger, nullable=False, server_default='0')
    createdby = Column(BigInteger, nullable=False)
    timecreated = Column(BigInteger, nullable=False)
    timemodified = Column(BigInteger, nullable=False)


class LtiTypesConfig(Base):
    __tablename__ = 'ssismdl_lti_types_config'

    id = Column(BigInteger, primary_key=True)
    typeid = Column(BigInteger, nullable=False, index=True)
    name = Column(String(100), nullable=False, server_default="''::character varying")
    value = Column(String(255), nullable=False, server_default="''::character varying")


class Message(Base):
    __tablename__ = 'ssismdl_message'

    id = Column(BigInteger, primary_key=True)
    useridfrom = Column(BigInteger, nullable=False, index=True, server_default='0')
    useridto = Column(BigInteger, nullable=False, index=True, server_default='0')
    subject = Column(Text)
    fullmessage = Column(Text)
    fullmessageformat = Column(SmallInteger, server_default='0')
    fullmessagehtml = Column(Text)
    smallmessage = Column(Text)
    notification = Column(SmallInteger, server_default='0')
    contexturl = Column(Text)
    contexturlname = Column(Text)
    timecreated = Column(BigInteger, nullable=False, server_default='0')


class MessageContact(Base):
    __tablename__ = 'ssismdl_message_contacts'
    __table_args__ = (
        Index('ssismdl_messcont_usecon_uix', 'userid', 'contactid'),
    )

    id = Column(BigInteger, primary_key=True)
    userid = Column(BigInteger, nullable=False, server_default='0')
    contactid = Column(BigInteger, nullable=False, server_default='0')
    blocked = Column(SmallInteger, nullable=False, server_default='0')


class MessageProcessor(Base):
    __tablename__ = 'ssismdl_message_processors'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(166), nullable=False, server_default="''::character varying")
    enabled = Column(SmallInteger, nullable=False, server_default='1')


class MessageProvider(Base):
    __tablename__ = 'ssismdl_message_providers'
    __table_args__ = (
        Index('ssismdl_messprov_comnam_uix', 'component', 'name'),
    )

    id = Column(BigInteger, primary_key=True)
    name = Column(String(100), nullable=False, server_default="''::character varying")
    component = Column(String(200), nullable=False, server_default="''::character varying")
    capability = Column(String(255))


class MessageRead(Base):
    __tablename__ = 'ssismdl_message_read'

    id = Column(BigInteger, primary_key=True)
    useridfrom = Column(BigInteger, nullable=False, index=True, server_default='0')
    useridto = Column(BigInteger, nullable=False, index=True, server_default='0')
    subject = Column(Text)
    fullmessage = Column(Text)
    fullmessageformat = Column(SmallInteger, server_default='0')
    fullmessagehtml = Column(Text)
    smallmessage = Column(Text)
    notification = Column(SmallInteger, server_default='0')
    contexturl = Column(Text)
    contexturlname = Column(Text)
    timecreated = Column(BigInteger, nullable=False, server_default='0')
    timeread = Column(BigInteger, nullable=False, server_default='0')


class MessageWorking(Base):
    __tablename__ = 'ssismdl_message_working'

    id = Column(BigInteger, primary_key=True)
    unreadmessageid = Column(BigInteger, nullable=False, index=True)
    processorid = Column(BigInteger, nullable=False)


class MnetApplication(Base):
    __tablename__ = 'ssismdl_mnet_application'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(50), nullable=False, server_default="''::character varying")
    display_name = Column(String(50), nullable=False, server_default="''::character varying")
    xmlrpc_server_url = Column(String(255), nullable=False, server_default="''::character varying")
    sso_land_url = Column(String(255), nullable=False, server_default="''::character varying")
    sso_jump_url = Column(String(255), nullable=False, server_default="''::character varying")


class MnetHost(Base):
    __tablename__ = 'ssismdl_mnet_host'

    id = Column(BigInteger, primary_key=True)
    deleted = Column(SmallInteger, nullable=False, server_default='0')
    wwwroot = Column(String(255), nullable=False, server_default="''::character varying")
    ip_address = Column(String(45), nullable=False, server_default="''::character varying")
    name = Column(String(80), nullable=False, server_default="''::character varying")
    public_key = Column(Text, nullable=False)
    public_key_expires = Column(BigInteger, nullable=False, server_default='0')
    transport = Column(SmallInteger, nullable=False, server_default='0')
    portno = Column(Integer, nullable=False, server_default='0')
    last_connect_time = Column(BigInteger, nullable=False, server_default='0')
    last_log_id = Column(BigInteger, nullable=False, server_default='0')
    force_theme = Column(SmallInteger, nullable=False, server_default='0')
    theme = Column(String(100))
    applicationid = Column(BigInteger, nullable=False, index=True, server_default='1')


class MnetHost2service(Base):
    __tablename__ = 'ssismdl_mnet_host2service'
    __table_args__ = (
        Index('ssismdl_mnethost_hosser_uix', 'hostid', 'serviceid'),
    )

    id = Column(BigInteger, primary_key=True)
    hostid = Column(BigInteger, nullable=False, server_default='0')
    serviceid = Column(BigInteger, nullable=False, server_default='0')
    publish = Column(SmallInteger, nullable=False, server_default='0')
    subscribe = Column(SmallInteger, nullable=False, server_default='0')


class MnetLog(Base):
    __tablename__ = 'ssismdl_mnet_log'
    __table_args__ = (
        Index('ssismdl_mnetlog_hosusecou_ix', 'hostid', 'userid', 'course'),
    )

    id = Column(BigInteger, primary_key=True)
    hostid = Column(BigInteger, nullable=False, server_default='0')
    remoteid = Column(BigInteger, nullable=False, server_default='0')
    time = Column(BigInteger, nullable=False, server_default='0')
    userid = Column(BigInteger, nullable=False, server_default='0')
    ip = Column(String(45), nullable=False, server_default="''::character varying")
    course = Column(BigInteger, nullable=False, server_default='0')
    coursename = Column(String(40), nullable=False, server_default="''::character varying")
    module = Column(String(20), nullable=False, server_default="''::character varying")
    cmid = Column(BigInteger, nullable=False, server_default='0')
    action = Column(String(40), nullable=False, server_default="''::character varying")
    url = Column(String(100), nullable=False, server_default="''::character varying")
    info = Column(String(255), nullable=False, server_default="''::character varying")


class MnetRemoteRpc(Base):
    __tablename__ = 'ssismdl_mnet_remote_rpc'

    id = Column(BigInteger, primary_key=True)
    functionname = Column(String(40), nullable=False, server_default="''::character varying")
    xmlrpcpath = Column(String(80), nullable=False, server_default="''::character varying")
    plugintype = Column(String(20), nullable=False, server_default="''::character varying")
    pluginname = Column(String(20), nullable=False, server_default="''::character varying")
    enabled = Column(SmallInteger, nullable=False)


class MnetRemoteService2rpc(Base):
    __tablename__ = 'ssismdl_mnet_remote_service2rpc'
    __table_args__ = (
        Index('ssismdl_mnetremoserv_rpcse_uix', 'rpcid', 'serviceid'),
    )

    id = Column(BigInteger, primary_key=True)
    serviceid = Column(BigInteger, nullable=False, server_default='0')
    rpcid = Column(BigInteger, nullable=False, server_default='0')


class MnetRpc(Base):
    __tablename__ = 'ssismdl_mnet_rpc'
    __table_args__ = (
        Index('ssismdl_mnetrpc_enaxml_ix', 'enabled', 'xmlrpcpath'),
    )

    id = Column(BigInteger, primary_key=True)
    functionname = Column(String(40), nullable=False, server_default="''::character varying")
    xmlrpcpath = Column(String(80), nullable=False, server_default="''::character varying")
    plugintype = Column(String(20), nullable=False, server_default="''::character varying")
    pluginname = Column(String(20), nullable=False, server_default="''::character varying")
    enabled = Column(SmallInteger, nullable=False, server_default='0')
    help = Column(Text, nullable=False)
    profile = Column(Text, nullable=False)
    filename = Column(String(100), nullable=False, server_default="''::character varying")
    classname = Column(String(150))
    static = Column(SmallInteger)


class MnetService(Base):
    __tablename__ = 'ssismdl_mnet_service'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(40), nullable=False, server_default="''::character varying")
    description = Column(String(40), nullable=False, server_default="''::character varying")
    apiversion = Column(String(10), nullable=False, server_default="''::character varying")
    offer = Column(SmallInteger, nullable=False, server_default='0')


class MnetService2rpc(Base):
    __tablename__ = 'ssismdl_mnet_service2rpc'
    __table_args__ = (
        Index('ssismdl_mnetserv_rpcser_uix', 'rpcid', 'serviceid'),
    )

    id = Column(BigInteger, primary_key=True)
    serviceid = Column(BigInteger, nullable=False, server_default='0')
    rpcid = Column(BigInteger, nullable=False, server_default='0')


class MnetSession(Base):
    __tablename__ = 'ssismdl_mnet_session'

    id = Column(BigInteger, primary_key=True)
    userid = Column(BigInteger, nullable=False, server_default='0')
    username = Column(String(100), nullable=False, server_default="''::character varying")
    token = Column(String(40), nullable=False, unique=True, server_default="''::character varying")
    mnethostid = Column(BigInteger, nullable=False, server_default='0')
    useragent = Column(String(40), nullable=False, server_default="''::character varying")
    confirm_timeout = Column(BigInteger, nullable=False, server_default='0')
    session_id = Column(String(40), nullable=False, server_default="''::character varying")
    expires = Column(BigInteger, nullable=False, server_default='0')


class MnetSsoAccessControl(Base):
    __tablename__ = 'ssismdl_mnet_sso_access_control'
    __table_args__ = (
        Index('ssismdl_mnetssoaccecont_mn_uix', 'mnet_host_id', 'username'),
    )

    id = Column(BigInteger, primary_key=True)
    username = Column(String(100), nullable=False, server_default="''::character varying")
    mnet_host_id = Column(BigInteger, nullable=False, server_default='0')
    accessctrl = Column(String(20), nullable=False, server_default="'allow'::character varying")


class MnetserviceEnrolCourse(Base):
    __tablename__ = 'ssismdl_mnetservice_enrol_courses'
    __table_args__ = (
        Index('ssismdl_mnetenrocour_hosre_uix', 'hostid', 'remoteid'),
    )

    id = Column(BigInteger, primary_key=True)
    hostid = Column(BigInteger, nullable=False)
    remoteid = Column(BigInteger, nullable=False)
    categoryid = Column(BigInteger, nullable=False)
    categoryname = Column(String(255), nullable=False, server_default="''::character varying")
    sortorder = Column(BigInteger, nullable=False, server_default='0')
    fullname = Column(String(254), nullable=False, server_default="''::character varying")
    shortname = Column(String(100), nullable=False, server_default="''::character varying")
    idnumber = Column(String(100), nullable=False, server_default="''::character varying")
    summary = Column(Text, nullable=False)
    summaryformat = Column(SmallInteger, server_default='0')
    startdate = Column(BigInteger, nullable=False)
    roleid = Column(BigInteger, nullable=False)
    rolename = Column(String(255), nullable=False, server_default="''::character varying")


class MnetserviceEnrolEnrolment(Base):
    __tablename__ = 'ssismdl_mnetservice_enrol_enrolments'

    id = Column(BigInteger, primary_key=True)
    hostid = Column(BigInteger, nullable=False, index=True)
    userid = Column(BigInteger, nullable=False, index=True)
    remotecourseid = Column(BigInteger, nullable=False)
    rolename = Column(String(255), nullable=False, server_default="''::character varying")
    enroltime = Column(BigInteger, nullable=False, server_default='0')
    enroltype = Column(String(20), nullable=False, server_default="''::character varying")


class Module(Base):
    __tablename__ = 'ssismdl_modules'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(20), nullable=False, index=True, server_default="''::character varying")
    version = Column(BigInteger, nullable=False, server_default='0')
    cron = Column(BigInteger, nullable=False, server_default='0')
    lastcron = Column(BigInteger, nullable=False, server_default='0')
    search = Column(String(255), nullable=False, server_default="''::character varying")
    visible = Column(SmallInteger, nullable=False, server_default='1')


class MyPage(Base):
    __tablename__ = 'ssismdl_my_pages'
    __table_args__ = (
        Index('ssismdl_mypage_usepri_ix', 'userid', 'private'),
    )

    id = Column(BigInteger, primary_key=True)
    userid = Column(BigInteger, server_default='0')
    name = Column(String(200), nullable=False, server_default="''::character varying")
    private = Column(SmallInteger, nullable=False, server_default='1')
    sortorder = Column(Integer, nullable=False, server_default='0')


class Page(Base):
    __tablename__ = 'ssismdl_page'

    id = Column(BigInteger, primary_key=True)
    course = Column(BigInteger, nullable=False, index=True, server_default='0')
    name = Column(String(255), nullable=False, server_default="''::character varying")
    intro = Column(Text)
    introformat = Column(SmallInteger, nullable=False, server_default='0')
    content = Column(Text)
    contentformat = Column(SmallInteger, nullable=False, server_default='0')
    legacyfiles = Column(SmallInteger, nullable=False, server_default='0')
    legacyfileslast = Column(BigInteger)
    display = Column(SmallInteger, nullable=False, server_default='0')
    displayoptions = Column(Text)
    revision = Column(BigInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')


class PortfolioInstance(Base):
    __tablename__ = 'ssismdl_portfolio_instance'

    id = Column(BigInteger, primary_key=True)
    plugin = Column(String(50), nullable=False, server_default="''::character varying")
    name = Column(String(255), nullable=False, server_default="''::character varying")
    visible = Column(SmallInteger, nullable=False, server_default='1')


class PortfolioInstanceConfig(Base):
    __tablename__ = 'ssismdl_portfolio_instance_config'

    id = Column(BigInteger, primary_key=True)
    instance = Column(BigInteger, nullable=False, index=True)
    name = Column(String(255), nullable=False, index=True, server_default="''::character varying")
    value = Column(Text)


class PortfolioInstanceUser(Base):
    __tablename__ = 'ssismdl_portfolio_instance_user'

    id = Column(BigInteger, primary_key=True)
    instance = Column(BigInteger, nullable=False, index=True)
    userid = Column(BigInteger, nullable=False, index=True)
    name = Column(String(255), nullable=False, server_default="''::character varying")
    value = Column(Text)


class PortfolioLog(Base):
    __tablename__ = 'ssismdl_portfolio_log'

    id = Column(BigInteger, primary_key=True)
    userid = Column(BigInteger, nullable=False, index=True)
    time = Column(BigInteger, nullable=False)
    portfolio = Column(BigInteger, nullable=False, index=True)
    caller_class = Column(String(150), nullable=False, server_default="''::character varying")
    caller_file = Column(String(255), nullable=False, server_default="''::character varying")
    caller_sha1 = Column(String(255), nullable=False, server_default="''::character varying")
    tempdataid = Column(BigInteger, nullable=False, server_default='0')
    returnurl = Column(String(255), nullable=False, server_default="''::character varying")
    continueurl = Column(String(255), nullable=False, server_default="''::character varying")
    caller_component = Column(String(255))


class PortfolioMaharaQueue(Base):
    __tablename__ = 'ssismdl_portfolio_mahara_queue'

    id = Column(BigInteger, primary_key=True)
    transferid = Column(BigInteger, nullable=False, index=True)
    token = Column(String(50), nullable=False, index=True, server_default="''::character varying")


class PortfolioTempdatum(Base):
    __tablename__ = 'ssismdl_portfolio_tempdata'

    id = Column(BigInteger, primary_key=True)
    data = Column(Text)
    expirytime = Column(BigInteger, nullable=False)
    userid = Column(BigInteger, nullable=False, index=True)
    instance = Column(BigInteger, index=True, server_default='0')


class Post(Base):
    __tablename__ = 'ssismdl_post'
    __table_args__ = (
        Index('ssismdl_post_iduse_uix', 'id', 'userid'),
    )

    id = Column(BigInteger, primary_key=True)
    module = Column(String(20), nullable=False, index=True, server_default="''::character varying")
    userid = Column(BigInteger, nullable=False, server_default='0')
    courseid = Column(BigInteger, nullable=False, server_default='0')
    groupid = Column(BigInteger, nullable=False, server_default='0')
    moduleid = Column(BigInteger, nullable=False, server_default='0')
    coursemoduleid = Column(BigInteger, nullable=False, server_default='0')
    subject = Column(String(128), nullable=False, index=True, server_default="''::character varying")
    summary = Column(Text)
    content = Column(Text)
    uniquehash = Column(String(255), nullable=False, server_default="''::character varying")
    rating = Column(BigInteger, nullable=False, server_default='0')
    format = Column(BigInteger, nullable=False, server_default='0')
    summaryformat = Column(SmallInteger, nullable=False, server_default='0')
    attachment = Column(String(100))
    publishstate = Column(String(20), nullable=False, server_default="'draft'::character varying")
    lastmodified = Column(BigInteger, nullable=False, index=True, server_default='0')
    created = Column(BigInteger, nullable=False, server_default='0')
    usermodified = Column(BigInteger, index=True)


class Profiling(Base):
    __tablename__ = 'ssismdl_profiling'
    __table_args__ = (
        Index('ssismdl_prof_urlrun_ix', 'url', 'runreference'),
        Index('ssismdl_prof_timrun_ix', 'timecreated', 'runreference')
    )

    id = Column(BigInteger, primary_key=True)
    runid = Column(String(32), nullable=False, unique=True, server_default="''::character varying")
    url = Column(String(255), nullable=False, server_default="''::character varying")
    data = Column(Text, nullable=False)
    totalexecutiontime = Column(BigInteger, nullable=False)
    totalcputime = Column(BigInteger, nullable=False)
    totalcalls = Column(BigInteger, nullable=False)
    totalmemory = Column(BigInteger, nullable=False)
    runreference = Column(SmallInteger, nullable=False, server_default='0')
    runcomment = Column(String(255), nullable=False, server_default="''::character varying")
    timecreated = Column(BigInteger, nullable=False)


class QtypeDdimageortext(Base):
    __tablename__ = 'ssismdl_qtype_ddimageortext'

    id = Column(BigInteger, primary_key=True)
    questionid = Column(BigInteger, nullable=False, index=True, server_default='0')
    shuffleanswers = Column(SmallInteger, nullable=False, server_default='1')
    correctfeedback = Column(Text, nullable=False)
    correctfeedbackformat = Column(SmallInteger, nullable=False, server_default='0')
    partiallycorrectfeedback = Column(Text, nullable=False)
    partiallycorrectfeedbackformat = Column(SmallInteger, nullable=False, server_default='0')
    incorrectfeedback = Column(Text, nullable=False)
    incorrectfeedbackformat = Column(SmallInteger, nullable=False, server_default='0')
    shownumcorrect = Column(SmallInteger, nullable=False, server_default='0')


class QtypeDdimageortextDrag(Base):
    __tablename__ = 'ssismdl_qtype_ddimageortext_drags'

    id = Column(BigInteger, primary_key=True)
    questionid = Column(BigInteger, nullable=False, index=True, server_default='0')
    no = Column(BigInteger, nullable=False, server_default='0')
    draggroup = Column(BigInteger, nullable=False, server_default='0')
    infinite = Column(SmallInteger, nullable=False, server_default='0')
    label = Column(Text, nullable=False)


class QtypeDdimageortextDrop(Base):
    __tablename__ = 'ssismdl_qtype_ddimageortext_drops'

    id = Column(BigInteger, primary_key=True)
    questionid = Column(BigInteger, nullable=False, index=True, server_default='0')
    no = Column(BigInteger, nullable=False, server_default='0')
    xleft = Column(BigInteger, nullable=False, server_default='0')
    ytop = Column(BigInteger, nullable=False, server_default='0')
    choice = Column(BigInteger, nullable=False, server_default='0')
    label = Column(Text, nullable=False)


class QtypeDdmarker(Base):
    __tablename__ = 'ssismdl_qtype_ddmarker'

    id = Column(BigInteger, primary_key=True)
    questionid = Column(BigInteger, nullable=False, index=True, server_default='0')
    shuffleanswers = Column(SmallInteger, nullable=False, server_default='1')
    correctfeedback = Column(Text, nullable=False)
    correctfeedbackformat = Column(SmallInteger, nullable=False, server_default='0')
    partiallycorrectfeedback = Column(Text, nullable=False)
    partiallycorrectfeedbackformat = Column(SmallInteger, nullable=False, server_default='0')
    incorrectfeedback = Column(Text, nullable=False)
    incorrectfeedbackformat = Column(SmallInteger, nullable=False, server_default='0')
    shownumcorrect = Column(SmallInteger, nullable=False, server_default='0')
    showmisplaced = Column(SmallInteger, nullable=False, server_default='0')


class QtypeDdmarkerDrag(Base):
    __tablename__ = 'ssismdl_qtype_ddmarker_drags'

    id = Column(BigInteger, primary_key=True)
    questionid = Column(BigInteger, nullable=False, index=True, server_default='0')
    no = Column(BigInteger, nullable=False, server_default='0')
    label = Column(Text, nullable=False)
    infinite = Column(SmallInteger, nullable=False, server_default='0')
    noofdrags = Column(BigInteger, nullable=False, server_default='1')


class QtypeDdmarkerDrop(Base):
    __tablename__ = 'ssismdl_qtype_ddmarker_drops'

    id = Column(BigInteger, primary_key=True)
    questionid = Column(BigInteger, nullable=False, index=True, server_default='0')
    no = Column(BigInteger, nullable=False, server_default='0')
    shape = Column(String(255))
    coords = Column(Text, nullable=False)
    choice = Column(BigInteger, nullable=False, server_default='0')


class QtypeEssayOption(Base):
    __tablename__ = 'ssismdl_qtype_essay_options'

    id = Column(BigInteger, primary_key=True)
    questionid = Column(BigInteger, nullable=False, unique=True)
    responseformat = Column(String(16), nullable=False, server_default="'editor'::character varying")
    responsefieldlines = Column(SmallInteger, nullable=False, server_default='15')
    attachments = Column(SmallInteger, nullable=False, server_default='0')
    graderinfo = Column(Text)
    graderinfoformat = Column(SmallInteger, nullable=False, server_default='0')
    responsetemplate = Column(Text)
    responsetemplateformat = Column(SmallInteger, nullable=False, server_default='0')


class QtypeMatchOption(Base):
    __tablename__ = 'ssismdl_qtype_match_options'

    id = Column(BigInteger, primary_key=True)
    questionid = Column(BigInteger, nullable=False, unique=True, server_default='0')
    shuffleanswers = Column(SmallInteger, nullable=False, server_default='1')
    correctfeedback = Column(Text, nullable=False)
    correctfeedbackformat = Column(SmallInteger, nullable=False, server_default='0')
    partiallycorrectfeedback = Column(Text, nullable=False)
    partiallycorrectfeedbackformat = Column(SmallInteger, nullable=False, server_default='0')
    incorrectfeedback = Column(Text, nullable=False)
    incorrectfeedbackformat = Column(SmallInteger, nullable=False, server_default='0')
    shownumcorrect = Column(SmallInteger, nullable=False, server_default='0')


class QtypeMatchSubquestion(Base):
    __tablename__ = 'ssismdl_qtype_match_subquestions'

    id = Column(BigInteger, primary_key=True)
    questionid = Column(BigInteger, nullable=False, index=True, server_default='0')
    questiontext = Column(Text, nullable=False)
    questiontextformat = Column(SmallInteger, nullable=False, server_default='0')
    answertext = Column(String(255), nullable=False, server_default="''::character varying")


class QtypeShortanswerOption(Base):
    __tablename__ = 'ssismdl_qtype_shortanswer_options'

    id = Column(BigInteger, primary_key=True)
    questionid = Column(BigInteger, nullable=False, unique=True, server_default='0')
    usecase = Column(SmallInteger, nullable=False, server_default='0')


class QtypeStackCasCache(Base):
    __tablename__ = 'ssismdl_qtype_stack_cas_cache'

    id = Column(BigInteger, primary_key=True)
    hash = Column(String(40), nullable=False, index=True, server_default="''::character varying")
    command = Column(Text, nullable=False)
    result = Column(Text, nullable=False)


class QtypeStackDeployedSeed(Base):
    __tablename__ = 'ssismdl_qtype_stack_deployed_seeds'
    __table_args__ = (
        Index('ssismdl_qtypstacdeplseed_q_uix', 'questionid', 'seed'),
    )

    id = Column(BigInteger, primary_key=True)
    questionid = Column(BigInteger, nullable=False, index=True)
    seed = Column(BigInteger, nullable=False)


class QtypeStackInput(Base):
    __tablename__ = 'ssismdl_qtype_stack_inputs'
    __table_args__ = (
        Index('ssismdl_qtypstacinpu_quena_uix', 'questionid', 'name'),
    )

    id = Column(BigInteger, primary_key=True)
    questionid = Column(BigInteger, nullable=False, index=True)
    name = Column(String(32), nullable=False, server_default="''::character varying")
    type = Column(String(32), nullable=False, server_default="''::character varying")
    tans = Column(String(255), nullable=False, server_default="''::character varying")
    boxsize = Column(BigInteger, nullable=False, server_default='15')
    strictsyntax = Column(SmallInteger, nullable=False, server_default='1')
    insertstars = Column(SmallInteger, nullable=False, server_default='0')
    syntaxhint = Column(String(255), nullable=False, server_default="''::character varying")
    forbidwords = Column(String(255), nullable=False, server_default="''::character varying")
    forbidfloat = Column(SmallInteger, nullable=False, server_default='1')
    requirelowestterms = Column(SmallInteger, nullable=False, server_default='0')
    checkanswertype = Column(SmallInteger, nullable=False, server_default='0')
    mustverify = Column(SmallInteger, nullable=False, server_default='1')
    showvalidation = Column(SmallInteger, nullable=False, server_default='1')
    options = Column(Text, nullable=False)
    allowwords = Column(String(255), nullable=False, server_default="''::character varying")


class QtypeStackOption(Base):
    __tablename__ = 'ssismdl_qtype_stack_options'

    id = Column(BigInteger, primary_key=True)
    questionid = Column(BigInteger, nullable=False, unique=True)
    questionvariables = Column(Text, nullable=False)
    specificfeedback = Column(Text, nullable=False)
    specificfeedbackformat = Column(SmallInteger, nullable=False, server_default='0')
    questionnote = Column(String(255), nullable=False, server_default="''::character varying")
    questionsimplify = Column(SmallInteger, nullable=False, server_default='1')
    assumepositive = Column(SmallInteger, nullable=False, server_default='0')
    prtcorrect = Column(Text, nullable=False)
    prtcorrectformat = Column(SmallInteger, nullable=False, server_default='0')
    prtpartiallycorrect = Column(Text, nullable=False)
    prtpartiallycorrectformat = Column(SmallInteger, nullable=False, server_default='0')
    prtincorrect = Column(Text, nullable=False)
    prtincorrectformat = Column(SmallInteger, nullable=False, server_default='0')
    multiplicationsign = Column(String(8), nullable=False, server_default="'dot'::character varying")
    sqrtsign = Column(SmallInteger, nullable=False, server_default='1')
    complexno = Column(String(8), nullable=False, server_default="'i'::character varying")
    inversetrig = Column(String(8), nullable=False, server_default="'cos-1'::character varying")
    variantsselectionseed = Column(String(255))


class QtypeStackPrtNode(Base):
    __tablename__ = 'ssismdl_qtype_stack_prt_nodes'
    __table_args__ = (
        Index('ssismdl_qtypstacprtnode_que_ix', 'questionid', 'prtname'),
        Index('ssismdl_qtypstacprtnode_qu_uix', 'questionid', 'prtname', 'nodename')
    )

    id = Column(BigInteger, primary_key=True)
    questionid = Column(BigInteger, nullable=False)
    prtname = Column(String(32), nullable=False, server_default="''::character varying")
    nodename = Column(String(8), nullable=False, server_default="''::character varying")
    answertest = Column(String(32), nullable=False, server_default="''::character varying")
    sans = Column(String(255), nullable=False, server_default="''::character varying")
    tans = Column(String(255), nullable=False, server_default="''::character varying")
    testoptions = Column(String(255), nullable=False, server_default="''::character varying")
    quiet = Column(SmallInteger, nullable=False, server_default='0')
    truescoremode = Column(String(4), nullable=False, server_default="'='::character varying")
    truescore = Column(Numeric(12, 7), nullable=False, server_default='1')
    truepenalty = Column(Numeric(12, 7))
    truenextnode = Column(String(8))
    trueanswernote = Column(String(255), nullable=False, server_default="''::character varying")
    truefeedback = Column(Text, nullable=False)
    truefeedbackformat = Column(SmallInteger, nullable=False, server_default='0')
    falsescoremode = Column(String(4), nullable=False, server_default="'='::character varying")
    falsescore = Column(Numeric(12, 7), server_default='0')
    falsepenalty = Column(Numeric(12, 7))
    falsenextnode = Column(String(8))
    falseanswernote = Column(String(255), nullable=False, server_default="''::character varying")
    falsefeedback = Column(Text, nullable=False)
    falsefeedbackformat = Column(SmallInteger, nullable=False, server_default='0')


class QtypeStackPrt(Base):
    __tablename__ = 'ssismdl_qtype_stack_prts'
    __table_args__ = (
        Index('ssismdl_qtypstacprts_quena_uix', 'questionid', 'name'),
    )

    id = Column(BigInteger, primary_key=True)
    questionid = Column(BigInteger, nullable=False, index=True)
    name = Column(String(32), nullable=False, server_default="''::character varying")
    value = Column(Numeric(12, 7), nullable=False, server_default='1')
    autosimplify = Column(SmallInteger, nullable=False, server_default='1')
    feedbackvariables = Column(Text, nullable=False)
    firstnodename = Column(String(8), nullable=False, server_default="''::character varying")


class QtypeStackQtestExpected(Base):
    __tablename__ = 'ssismdl_qtype_stack_qtest_expected'
    __table_args__ = (
        Index('ssismdl_qtypstacqtesexpe_q_uix', 'questionid', 'testcase', 'prtname'),
        Index('ssismdl_qtypstacqtesexpe_qu_ix', 'questionid', 'testcase')
    )

    id = Column(BigInteger, primary_key=True)
    questionid = Column(BigInteger, nullable=False)
    testcase = Column(BigInteger, nullable=False)
    prtname = Column(String(32), nullable=False, server_default="''::character varying")
    expectedscore = Column(Numeric(12, 7))
    expectedpenalty = Column(Numeric(12, 7))
    expectedanswernote = Column(String(255), nullable=False, server_default="''::character varying")


class QtypeStackQtestInput(Base):
    __tablename__ = 'ssismdl_qtype_stack_qtest_inputs'
    __table_args__ = (
        Index('ssismdl_qtypstacqtesinpu_q_uix', 'questionid', 'testcase', 'inputname'),
        Index('ssismdl_qtypstacqtesinpu_qu_ix', 'questionid', 'testcase')
    )

    id = Column(BigInteger, primary_key=True)
    questionid = Column(BigInteger, nullable=False)
    testcase = Column(BigInteger, nullable=False)
    inputname = Column(String(32), nullable=False, server_default="''::character varying")
    value = Column(String(255), nullable=False, server_default="''::character varying")


class QtypeStackQtest(Base):
    __tablename__ = 'ssismdl_qtype_stack_qtests'
    __table_args__ = (
        Index('ssismdl_qtypstacqtes_quete_uix', 'questionid', 'testcase'),
    )

    id = Column(BigInteger, primary_key=True)
    questionid = Column(BigInteger, nullable=False, index=True)
    testcase = Column(BigInteger, nullable=False)


class Question(Base):
    __tablename__ = 'ssismdl_question'

    id = Column(BigInteger, primary_key=True)
    category = Column(BigInteger, nullable=False, index=True, server_default='0')
    parent = Column(BigInteger, nullable=False, index=True, server_default='0')
    name = Column(String(255), nullable=False, server_default="''::character varying")
    questiontext = Column(Text, nullable=False)
    questiontextformat = Column(SmallInteger, nullable=False, server_default='0')
    generalfeedback = Column(Text, nullable=False)
    generalfeedbackformat = Column(SmallInteger, nullable=False, server_default='0')
    defaultmark = Column(Numeric(12, 7), nullable=False, server_default='1')
    penalty = Column(Numeric(12, 7), nullable=False, server_default='0.3333333')
    qtype = Column(String(20), nullable=False, server_default="''::character varying")
    length = Column(BigInteger, nullable=False, server_default='1')
    stamp = Column(String(255), nullable=False, server_default="''::character varying")
    version = Column(String(255), nullable=False, server_default="''::character varying")
    hidden = Column(SmallInteger, nullable=False, server_default='0')
    timecreated = Column(BigInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')
    createdby = Column(BigInteger, index=True)
    modifiedby = Column(BigInteger, index=True)


class QuestionAnswer(Base):
    __tablename__ = 'ssismdl_question_answers'

    id = Column(BigInteger, primary_key=True)
    question = Column(BigInteger, nullable=False, index=True, server_default='0')
    answer = Column(Text, nullable=False)
    answerformat = Column(SmallInteger, nullable=False, server_default='0')
    fraction = Column(Numeric(12, 7), nullable=False, server_default='0')
    feedback = Column(Text, nullable=False)
    feedbackformat = Column(SmallInteger, nullable=False, server_default='0')


class QuestionAttemptStepDatum(Base):
    __tablename__ = 'ssismdl_question_attempt_step_data'
    __table_args__ = (
        Index('ssismdl_quesattestepdata_a_uix', 'attemptstepid', 'name'),
    )

    id = Column(BigInteger, primary_key=True)
    attemptstepid = Column(BigInteger, nullable=False, index=True)
    name = Column(String(32), nullable=False, server_default="''::character varying")
    value = Column(Text)


class QuestionAttemptStep(Base):
    __tablename__ = 'ssismdl_question_attempt_steps'
    __table_args__ = (
        Index('ssismdl_quesattestep_quese_uix', 'questionattemptid', 'sequencenumber'),
    )

    id = Column(BigInteger, primary_key=True)
    questionattemptid = Column(BigInteger, nullable=False, index=True)
    sequencenumber = Column(BigInteger, nullable=False)
    state = Column(String(13), nullable=False, server_default="''::character varying")
    fraction = Column(Numeric(12, 7))
    timecreated = Column(BigInteger, nullable=False)
    userid = Column(BigInteger, index=True)


class QuestionAttempt(Base):
    __tablename__ = 'ssismdl_question_attempts'
    __table_args__ = (
        Index('ssismdl_quesatte_queslo_uix', 'questionusageid', 'slot'),
    )

    id = Column(BigInteger, primary_key=True)
    questionusageid = Column(BigInteger, nullable=False, index=True)
    slot = Column(BigInteger, nullable=False)
    behaviour = Column(String(32), nullable=False, server_default="''::character varying")
    questionid = Column(BigInteger, nullable=False, index=True)
    variant = Column(BigInteger, nullable=False, server_default='1')
    maxmark = Column(Numeric(12, 7), nullable=False)
    minfraction = Column(Numeric(12, 7), nullable=False)
    flagged = Column(SmallInteger, nullable=False, server_default='0')
    questionsummary = Column(Text)
    rightanswer = Column(Text)
    responsesummary = Column(Text)
    timemodified = Column(BigInteger, nullable=False)


class QuestionCalculated(Base):
    __tablename__ = 'ssismdl_question_calculated'

    id = Column(BigInteger, primary_key=True)
    question = Column(BigInteger, nullable=False, index=True, server_default='0')
    answer = Column(BigInteger, nullable=False, index=True, server_default='0')
    tolerance = Column(String(20), nullable=False, server_default="'0.0'::character varying")
    tolerancetype = Column(BigInteger, nullable=False, server_default='1')
    correctanswerlength = Column(BigInteger, nullable=False, server_default='2')
    correctanswerformat = Column(BigInteger, nullable=False, server_default='2')


class QuestionCalculatedOption(Base):
    __tablename__ = 'ssismdl_question_calculated_options'

    id = Column(BigInteger, primary_key=True)
    question = Column(BigInteger, nullable=False, index=True, server_default='0')
    synchronize = Column(SmallInteger, nullable=False, server_default='0')
    single = Column(SmallInteger, nullable=False, server_default='0')
    shuffleanswers = Column(SmallInteger, nullable=False, server_default='0')
    correctfeedback = Column(Text)
    correctfeedbackformat = Column(SmallInteger, nullable=False, server_default='0')
    partiallycorrectfeedback = Column(Text)
    partiallycorrectfeedbackformat = Column(SmallInteger, nullable=False, server_default='0')
    incorrectfeedback = Column(Text)
    incorrectfeedbackformat = Column(SmallInteger, nullable=False, server_default='0')
    answernumbering = Column(String(10), nullable=False, server_default="'abc'::character varying")
    shownumcorrect = Column(SmallInteger, nullable=False, server_default='0')


class QuestionCategory(Base):
    __tablename__ = 'ssismdl_question_categories'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(255), nullable=False, server_default="''::character varying")
    contextid = Column(BigInteger, nullable=False, index=True, server_default='0')
    info = Column(Text, nullable=False)
    infoformat = Column(SmallInteger, nullable=False, server_default='0')
    stamp = Column(String(255), nullable=False, server_default="''::character varying")
    parent = Column(BigInteger, nullable=False, index=True, server_default='0')
    sortorder = Column(BigInteger, nullable=False, server_default='999')


class QuestionDatasetDefinition(Base):
    __tablename__ = 'ssismdl_question_dataset_definitions'

    id = Column(BigInteger, primary_key=True)
    category = Column(BigInteger, nullable=False, index=True, server_default='0')
    name = Column(String(255), nullable=False, server_default="''::character varying")
    type = Column(BigInteger, nullable=False, server_default='0')
    options = Column(String(255), nullable=False, server_default="''::character varying")
    itemcount = Column(BigInteger, nullable=False, server_default='0')


class QuestionDatasetItem(Base):
    __tablename__ = 'ssismdl_question_dataset_items'

    id = Column(BigInteger, primary_key=True)
    definition = Column(BigInteger, nullable=False, index=True, server_default='0')
    itemnumber = Column(BigInteger, nullable=False, server_default='0')
    value = Column(String(255), nullable=False, server_default="''::character varying")


class QuestionDataset(Base):
    __tablename__ = 'ssismdl_question_datasets'
    __table_args__ = (
        Index('ssismdl_quesdata_quedat_ix', 'question', 'datasetdefinition'),
    )

    id = Column(BigInteger, primary_key=True)
    question = Column(BigInteger, nullable=False, index=True, server_default='0')
    datasetdefinition = Column(BigInteger, nullable=False, index=True, server_default='0')


class QuestionGapselect(Base):
    __tablename__ = 'ssismdl_question_gapselect'

    id = Column(BigInteger, primary_key=True)
    questionid = Column(BigInteger, nullable=False, index=True, server_default='0')
    shuffleanswers = Column(SmallInteger, nullable=False, server_default='1')
    correctfeedback = Column(Text, nullable=False)
    correctfeedbackformat = Column(SmallInteger, nullable=False, server_default='0')
    partiallycorrectfeedback = Column(Text, nullable=False)
    partiallycorrectfeedbackformat = Column(SmallInteger, nullable=False, server_default='0')
    incorrectfeedback = Column(Text, nullable=False)
    incorrectfeedbackformat = Column(SmallInteger, nullable=False, server_default='0')
    shownumcorrect = Column(SmallInteger, nullable=False, server_default='0')


class QuestionHint(Base):
    __tablename__ = 'ssismdl_question_hints'

    id = Column(BigInteger, primary_key=True)
    questionid = Column(BigInteger, nullable=False, index=True)
    hint = Column(Text, nullable=False)
    hintformat = Column(SmallInteger, nullable=False, server_default='0')
    shownumcorrect = Column(SmallInteger)
    clearwrong = Column(SmallInteger)
    options = Column(String(255))


class QuestionMultianswer(Base):
    __tablename__ = 'ssismdl_question_multianswer'

    id = Column(BigInteger, primary_key=True)
    question = Column(BigInteger, nullable=False, index=True, server_default='0')
    sequence = Column(Text, nullable=False)


class QuestionMultichoice(Base):
    __tablename__ = 'ssismdl_question_multichoice'

    id = Column(BigInteger, primary_key=True)
    question = Column(BigInteger, nullable=False, index=True, server_default='0')
    layout = Column(SmallInteger, nullable=False, server_default='0')
    answers = Column(String(255), nullable=False, server_default="''::character varying")
    single = Column(SmallInteger, nullable=False, server_default='0')
    shuffleanswers = Column(SmallInteger, nullable=False, server_default='1')
    correctfeedback = Column(Text, nullable=False)
    correctfeedbackformat = Column(SmallInteger, nullable=False, server_default='0')
    partiallycorrectfeedback = Column(Text, nullable=False)
    partiallycorrectfeedbackformat = Column(SmallInteger, nullable=False, server_default='0')
    incorrectfeedback = Column(Text, nullable=False)
    incorrectfeedbackformat = Column(SmallInteger, nullable=False, server_default='0')
    answernumbering = Column(String(10), nullable=False, server_default="'abc'::character varying")
    shownumcorrect = Column(SmallInteger, nullable=False, server_default='0')


class QuestionNumerical(Base):
    __tablename__ = 'ssismdl_question_numerical'

    id = Column(BigInteger, primary_key=True)
    question = Column(BigInteger, nullable=False, index=True, server_default='0')
    answer = Column(BigInteger, nullable=False, index=True, server_default='0')
    tolerance = Column(String(255), nullable=False, server_default="'0.0'::character varying")


class QuestionNumericalOption(Base):
    __tablename__ = 'ssismdl_question_numerical_options'

    id = Column(BigInteger, primary_key=True)
    question = Column(BigInteger, nullable=False, index=True, server_default='0')
    showunits = Column(SmallInteger, nullable=False, server_default='0')
    unitsleft = Column(SmallInteger, nullable=False, server_default='0')
    unitgradingtype = Column(SmallInteger, nullable=False, server_default='0')
    unitpenalty = Column(Numeric(12, 7), nullable=False, server_default='0.1')


class QuestionNumericalUnit(Base):
    __tablename__ = 'ssismdl_question_numerical_units'
    __table_args__ = (
        Index('ssismdl_quesnumeunit_queun_uix', 'question', 'unit'),
    )

    id = Column(BigInteger, primary_key=True)
    question = Column(BigInteger, nullable=False, index=True, server_default='0')
    multiplier = Column(Numeric(40, 20), nullable=False, server_default='1.00000000000000000000')
    unit = Column(String(50), nullable=False, server_default="''::character varying")


class QuestionRandomsamatch(Base):
    __tablename__ = 'ssismdl_question_randomsamatch'

    id = Column(BigInteger, primary_key=True)
    question = Column(BigInteger, nullable=False, index=True, server_default='0')
    choose = Column(BigInteger, nullable=False, server_default='4')


class QuestionSession(Base):
    __tablename__ = 'ssismdl_question_sessions'
    __table_args__ = (
        Index('ssismdl_quessess_attque_uix', 'attemptid', 'questionid'),
    )

    id = Column(BigInteger, primary_key=True)
    attemptid = Column(BigInteger, nullable=False, index=True, server_default='0')
    questionid = Column(BigInteger, nullable=False, index=True, server_default='0')
    newest = Column(BigInteger, nullable=False, index=True, server_default='0')
    newgraded = Column(BigInteger, nullable=False, index=True, server_default='0')
    sumpenalty = Column(Numeric(12, 7), nullable=False, server_default='0')
    manualcomment = Column(Text, nullable=False)
    manualcommentformat = Column(SmallInteger, nullable=False, server_default='0')
    flagged = Column(SmallInteger, nullable=False, server_default='0')


class QuestionState(Base):
    __tablename__ = 'ssismdl_question_states'

    id = Column(BigInteger, primary_key=True)
    attempt = Column(BigInteger, nullable=False, index=True, server_default='0')
    question = Column(BigInteger, nullable=False, index=True, server_default='0')
    seq_number = Column(Integer, nullable=False, server_default='0')
    answer = Column(Text, nullable=False)
    timestamp = Column(BigInteger, nullable=False, server_default='0')
    event = Column(SmallInteger, nullable=False, server_default='0')
    grade = Column(Numeric(12, 7), nullable=False, server_default='0')
    raw_grade = Column(Numeric(12, 7), nullable=False, server_default='0')
    penalty = Column(Numeric(12, 7), nullable=False, server_default='0')


class QuestionTruefalse(Base):
    __tablename__ = 'ssismdl_question_truefalse'

    id = Column(BigInteger, primary_key=True)
    question = Column(BigInteger, nullable=False, index=True, server_default='0')
    trueanswer = Column(BigInteger, nullable=False, server_default='0')
    falseanswer = Column(BigInteger, nullable=False, server_default='0')


class QuestionUsage(Base):
    __tablename__ = 'ssismdl_question_usages'

    id = Column(BigInteger, primary_key=True)
    contextid = Column(BigInteger, nullable=False, index=True)
    component = Column(String(255), nullable=False, server_default="''::character varying")
    preferredbehaviour = Column(String(32), nullable=False, server_default="''::character varying")


class Questionnaire(Base):
    __tablename__ = 'ssismdl_questionnaire'

    id = Column(BigInteger, primary_key=True)
    course = Column(BigInteger, nullable=False, server_default='0')
    name = Column(String(255), nullable=False, server_default="''::character varying")
    intro = Column(Text, nullable=False)
    introformat = Column(SmallInteger, nullable=False, server_default='0')
    qtype = Column(BigInteger, nullable=False, server_default='0')
    respondenttype = Column(String(9), nullable=False, server_default="'fullname'::character varying")
    resp_eligible = Column(String(8), nullable=False, server_default="'all'::character varying")
    resp_view = Column(SmallInteger, nullable=False, server_default='0')
    opendate = Column(BigInteger, nullable=False, server_default='0')
    closedate = Column(BigInteger, nullable=False, server_default='0')
    resume = Column(SmallInteger, nullable=False, server_default='0')
    navigate = Column(SmallInteger, nullable=False, server_default='0')
    grade = Column(BigInteger, nullable=False, server_default='0')
    sid = Column(BigInteger, nullable=False, index=True, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')
    completionsubmit = Column(SmallInteger, nullable=False, server_default='0')
    autonum = Column(SmallInteger, nullable=False, server_default='3')


class QuestionnaireAttempt(Base):
    __tablename__ = 'ssismdl_questionnaire_attempts'

    id = Column(BigInteger, primary_key=True)
    qid = Column(BigInteger, nullable=False, server_default='0')
    userid = Column(BigInteger, nullable=False, server_default='0')
    rid = Column(BigInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')


class QuestionnaireQuestChoice(Base):
    __tablename__ = 'ssismdl_questionnaire_quest_choice'

    id = Column(BigInteger, primary_key=True)
    question_id = Column(BigInteger, nullable=False, server_default='0')
    content = Column(Text, nullable=False)
    value = Column(Text)


class QuestionnaireQuestion(Base):
    __tablename__ = 'ssismdl_questionnaire_question'

    id = Column(BigInteger, primary_key=True)
    survey_id = Column(BigInteger, nullable=False, server_default='0')
    name = Column(String(30))
    type_id = Column(BigInteger, nullable=False, server_default='0')
    result_id = Column(BigInteger)
    length = Column(BigInteger, nullable=False, server_default='0')
    precise = Column(BigInteger, nullable=False, server_default='0')
    position = Column(BigInteger, nullable=False, server_default='0')
    content = Column(Text, nullable=False)
    required = Column(String(1), nullable=False, server_default="'n'::character varying")
    deleted = Column(String(1), nullable=False, server_default="'n'::character varying")
    dependquestion = Column(BigInteger, nullable=False, server_default='0')
    dependchoice = Column(BigInteger, nullable=False, server_default='0')


class QuestionnaireQuestionType(Base):
    __tablename__ = 'ssismdl_questionnaire_question_type'

    id = Column(BigInteger, primary_key=True)
    typeid = Column(BigInteger, nullable=False, unique=True, server_default='0')
    type = Column(String(32), nullable=False, server_default="''::character varying")
    has_choices = Column(String(1), nullable=False, server_default="'y'::character varying")
    response_table = Column(String(32))


class QuestionnaireRespMultiple(Base):
    __tablename__ = 'ssismdl_questionnaire_resp_multiple'
    __table_args__ = (
        Index('ssismdl_quesrespmult_resque_ix', 'response_id', 'question_id', 'choice_id'),
    )

    id = Column(BigInteger, primary_key=True)
    response_id = Column(BigInteger, nullable=False, server_default='0')
    question_id = Column(BigInteger, nullable=False, server_default='0')
    choice_id = Column(BigInteger, nullable=False, server_default='0')


class QuestionnaireRespSingle(Base):
    __tablename__ = 'ssismdl_questionnaire_resp_single'
    __table_args__ = (
        Index('ssismdl_quesrespsing_resque_ix', 'response_id', 'question_id'),
    )

    id = Column(BigInteger, primary_key=True)
    response_id = Column(BigInteger, nullable=False, server_default='0')
    question_id = Column(BigInteger, nullable=False, server_default='0')
    choice_id = Column(BigInteger, nullable=False, server_default='0')


class QuestionnaireResponse(Base):
    __tablename__ = 'ssismdl_questionnaire_response'

    id = Column(BigInteger, primary_key=True)
    survey_id = Column(BigInteger, nullable=False, server_default='0')
    submitted = Column(BigInteger, nullable=False, server_default='0')
    complete = Column(String(1), nullable=False, server_default="'n'::character varying")
    grade = Column(BigInteger, nullable=False, server_default='0')
    username = Column(String(64))


class QuestionnaireResponseBool(Base):
    __tablename__ = 'ssismdl_questionnaire_response_bool'
    __table_args__ = (
        Index('ssismdl_quesrespbool_resque_ix', 'response_id', 'question_id'),
    )

    id = Column(BigInteger, primary_key=True)
    response_id = Column(BigInteger, nullable=False, server_default='0')
    question_id = Column(BigInteger, nullable=False, server_default='0')
    choice_id = Column(String(1), nullable=False, server_default="'y'::character varying")


class QuestionnaireResponseDate(Base):
    __tablename__ = 'ssismdl_questionnaire_response_date'
    __table_args__ = (
        Index('ssismdl_quesrespdate_resque_ix', 'response_id', 'question_id'),
    )

    id = Column(BigInteger, primary_key=True)
    response_id = Column(BigInteger, nullable=False, server_default='0')
    question_id = Column(BigInteger, nullable=False, server_default='0')
    response = Column(Text)


class QuestionnaireResponseOther(Base):
    __tablename__ = 'ssismdl_questionnaire_response_other'
    __table_args__ = (
        Index('ssismdl_quesrespothe_resque_ix', 'response_id', 'question_id', 'choice_id'),
    )

    id = Column(BigInteger, primary_key=True)
    response_id = Column(BigInteger, nullable=False, server_default='0')
    question_id = Column(BigInteger, nullable=False, server_default='0')
    choice_id = Column(BigInteger, nullable=False, server_default='0')
    response = Column(Text)


class QuestionnaireResponseRank(Base):
    __tablename__ = 'ssismdl_questionnaire_response_rank'
    __table_args__ = (
        Index('ssismdl_quesresprank_resque_ix', 'response_id', 'question_id', 'choice_id'),
    )

    id = Column(BigInteger, primary_key=True)
    response_id = Column(BigInteger, nullable=False, server_default='0')
    question_id = Column(BigInteger, nullable=False, server_default='0')
    choice_id = Column(BigInteger, nullable=False, server_default='0')
    rank = Column(BigInteger, nullable=False, server_default='0')


class QuestionnaireResponseText(Base):
    __tablename__ = 'ssismdl_questionnaire_response_text'
    __table_args__ = (
        Index('ssismdl_quesresptext_resque_ix', 'response_id', 'question_id'),
    )

    id = Column(BigInteger, primary_key=True)
    response_id = Column(BigInteger, nullable=False, server_default='0')
    question_id = Column(BigInteger, nullable=False, server_default='0')
    response = Column(Text)


class QuestionnaireSurvey(Base):
    __tablename__ = 'ssismdl_questionnaire_survey'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(255), nullable=False, index=True, server_default="''::character varying")
    owner = Column(String(16), nullable=False, index=True, server_default="''::character varying")
    realm = Column(String(64), nullable=False, server_default="''::character varying")
    status = Column(BigInteger, nullable=False, server_default='0')
    title = Column(String(255), nullable=False, server_default="''::character varying")
    email = Column(String(255))
    subtitle = Column(Text)
    info = Column(Text)
    theme = Column(String(64))
    thanks_page = Column(String(255))
    thank_head = Column(String(255))
    thank_body = Column(Text)


class Quiz(Base):
    __tablename__ = 'ssismdl_quiz'

    id = Column(BigInteger, primary_key=True)
    course = Column(BigInteger, nullable=False, index=True, server_default='0')
    name = Column(String(255), nullable=False, server_default="''::character varying")
    intro = Column(Text, nullable=False)
    introformat = Column(SmallInteger, nullable=False, server_default='0')
    timeopen = Column(BigInteger, nullable=False, server_default='0')
    timeclose = Column(BigInteger, nullable=False, server_default='0')
    preferredbehaviour = Column(String(32), nullable=False, server_default="''::character varying")
    attempts = Column(Integer, nullable=False, server_default='0')
    attemptonlast = Column(SmallInteger, nullable=False, server_default='0')
    grademethod = Column(SmallInteger, nullable=False, server_default='1')
    decimalpoints = Column(SmallInteger, nullable=False, server_default='2')
    questiondecimalpoints = Column(SmallInteger, nullable=False, server_default='(-1)')
    reviewattempt = Column(Integer, nullable=False, server_default='0')
    reviewcorrectness = Column(Integer, nullable=False, server_default='0')
    reviewmarks = Column(Integer, nullable=False, server_default='0')
    reviewspecificfeedback = Column(Integer, nullable=False, server_default='0')
    reviewgeneralfeedback = Column(Integer, nullable=False, server_default='0')
    reviewrightanswer = Column(Integer, nullable=False, server_default='0')
    reviewoverallfeedback = Column(Integer, nullable=False, server_default='0')
    questionsperpage = Column(BigInteger, nullable=False, server_default='0')
    shufflequestions = Column(SmallInteger, nullable=False, server_default='0')
    shuffleanswers = Column(SmallInteger, nullable=False, server_default='0')
    questions = Column(Text, nullable=False)
    sumgrades = Column(Numeric(10, 5), nullable=False, server_default='0')
    grade = Column(Numeric(10, 5), nullable=False, server_default='0')
    timecreated = Column(BigInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')
    timelimit = Column(BigInteger, nullable=False, server_default='0')
    password = Column(String(255), nullable=False, server_default="''::character varying")
    subnet = Column(String(255), nullable=False, server_default="''::character varying")
    browsersecurity = Column(String(32), nullable=False, server_default="''::character varying")
    delay1 = Column(BigInteger, nullable=False, server_default='0')
    delay2 = Column(BigInteger, nullable=False, server_default='0')
    showuserpicture = Column(SmallInteger, nullable=False, server_default='0')
    showblocks = Column(SmallInteger, nullable=False, server_default='0')
    navmethod = Column(String(16), nullable=False, server_default="'free'::character varying")
    overduehandling = Column(String(16), nullable=False, server_default="'autoabandon'::character varying")
    graceperiod = Column(BigInteger, nullable=False, server_default='0')


class QuizAttempt(Base):
    __tablename__ = 'ssismdl_quiz_attempts'
    __table_args__ = (
        Index('ssismdl_quizatte_statim_ix', 'state', 'timecheckstate'),
        Index('ssismdl_quizatte_quiuseatt_uix', 'quiz', 'userid', 'attempt')
    )

    id = Column(BigInteger, primary_key=True)
    uniqueid = Column(BigInteger, nullable=False, unique=True, server_default='0')
    quiz = Column(BigInteger, nullable=False, index=True, server_default='0')
    userid = Column(BigInteger, nullable=False, index=True, server_default='0')
    attempt = Column(Integer, nullable=False, server_default='0')
    sumgrades = Column(Numeric(10, 5))
    timestart = Column(BigInteger, nullable=False, server_default='0')
    timefinish = Column(BigInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')
    layout = Column(Text, nullable=False)
    preview = Column(SmallInteger, nullable=False, server_default='0')
    needsupgradetonewqe = Column(SmallInteger, nullable=False, server_default='0')
    currentpage = Column(BigInteger, nullable=False, server_default='0')
    state = Column(String(16), nullable=False, server_default="'inprogress'::character varying")
    timecheckstate = Column(BigInteger, server_default='0')


class QuizFeedback(Base):
    __tablename__ = 'ssismdl_quiz_feedback'

    id = Column(BigInteger, primary_key=True)
    quizid = Column(BigInteger, nullable=False, index=True, server_default='0')
    feedbacktext = Column(Text, nullable=False)
    feedbacktextformat = Column(SmallInteger, nullable=False, server_default='0')
    mingrade = Column(Numeric(10, 5), nullable=False, server_default='0')
    maxgrade = Column(Numeric(10, 5), nullable=False, server_default='0')


class QuizGrade(Base):
    __tablename__ = 'ssismdl_quiz_grades'

    id = Column(BigInteger, primary_key=True)
    quiz = Column(BigInteger, nullable=False, index=True, server_default='0')
    userid = Column(BigInteger, nullable=False, index=True, server_default='0')
    grade = Column(Numeric(10, 5), nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')


class QuizOverride(Base):
    __tablename__ = 'ssismdl_quiz_overrides'

    id = Column(BigInteger, primary_key=True)
    quiz = Column(BigInteger, nullable=False, index=True, server_default='0')
    groupid = Column(BigInteger, index=True)
    userid = Column(BigInteger, index=True)
    timeopen = Column(BigInteger)
    timeclose = Column(BigInteger)
    timelimit = Column(BigInteger)
    attempts = Column(Integer)
    password = Column(String(255))


class QuizOverviewRegrade(Base):
    __tablename__ = 'ssismdl_quiz_overview_regrades'

    id = Column(BigInteger, primary_key=True)
    questionusageid = Column(BigInteger, nullable=False)
    slot = Column(BigInteger, nullable=False)
    newfraction = Column(Numeric(12, 7))
    oldfraction = Column(Numeric(12, 7))
    regraded = Column(SmallInteger, nullable=False)
    timemodified = Column(BigInteger, nullable=False)


class QuizQuestionInstance(Base):
    __tablename__ = 'ssismdl_quiz_question_instances'

    id = Column(BigInteger, primary_key=True)
    quiz = Column(BigInteger, nullable=False, index=True, server_default='0')
    question = Column(BigInteger, nullable=False, index=True, server_default='0')
    grade = Column(Numeric(12, 7), nullable=False, server_default='0')


class QuizQuestionResponseStat(Base):
    __tablename__ = 'ssismdl_quiz_question_response_stats'

    id = Column(BigInteger, primary_key=True)
    quizstatisticsid = Column(BigInteger, nullable=False)
    questionid = Column(BigInteger, nullable=False)
    subqid = Column(String(100), nullable=False, server_default="''::character varying")
    aid = Column(String(100))
    response = Column(Text)
    rcount = Column(BigInteger)
    credit = Column(Numeric(15, 5), nullable=False)


class QuizQuestionStatistic(Base):
    __tablename__ = 'ssismdl_quiz_question_statistics'

    id = Column(BigInteger, primary_key=True)
    quizstatisticsid = Column(BigInteger, nullable=False)
    questionid = Column(BigInteger, nullable=False)
    slot = Column(BigInteger)
    subquestion = Column(SmallInteger, nullable=False)
    s = Column(BigInteger, nullable=False, server_default='0')
    effectiveweight = Column(Numeric(15, 5))
    negcovar = Column(SmallInteger, nullable=False, server_default='0')
    discriminationindex = Column(Numeric(15, 5))
    discriminativeefficiency = Column(Numeric(15, 5))
    sd = Column(Numeric(15, 10))
    facility = Column(Numeric(15, 10))
    subquestions = Column(Text)
    maxmark = Column(Numeric(12, 7))
    positions = Column(Text)
    randomguessscore = Column(Numeric(12, 7))


class QuizReport(Base):
    __tablename__ = 'ssismdl_quiz_reports'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(255), unique=True)
    displayorder = Column(BigInteger, nullable=False)
    capability = Column(String(255))


class QuizStatistic(Base):
    __tablename__ = 'ssismdl_quiz_statistics'

    id = Column(BigInteger, primary_key=True)
    quizid = Column(BigInteger, nullable=False)
    groupid = Column(BigInteger, nullable=False)
    allattempts = Column(SmallInteger, nullable=False)
    timemodified = Column(BigInteger, nullable=False)
    firstattemptscount = Column(BigInteger, nullable=False)
    allattemptscount = Column(BigInteger, nullable=False)
    firstattemptsavg = Column(Numeric(15, 5))
    allattemptsavg = Column(Numeric(15, 5))
    median = Column(Numeric(15, 5))
    standarddeviation = Column(Numeric(15, 5))
    skewness = Column(Numeric(15, 10))
    kurtosis = Column(Numeric(15, 5))
    cic = Column(Numeric(15, 10))
    errorratio = Column(Numeric(15, 10))
    standarderror = Column(Numeric(15, 10))


class Rating(Base):
    __tablename__ = 'ssismdl_rating'
    __table_args__ = (
        Index('ssismdl_rati_comratconite_ix', 'component', 'ratingarea', 'contextid', 'itemid'),
    )

    id = Column(BigInteger, primary_key=True)
    contextid = Column(BigInteger, nullable=False, index=True)
    component = Column(String(100), nullable=False, server_default="''::character varying")
    ratingarea = Column(String(50), nullable=False, server_default="''::character varying")
    itemid = Column(BigInteger, nullable=False)
    scaleid = Column(BigInteger, nullable=False)
    rating = Column(BigInteger, nullable=False)
    userid = Column(BigInteger, nullable=False, index=True)
    timecreated = Column(BigInteger, nullable=False)
    timemodified = Column(BigInteger, nullable=False)


class RegistrationHub(Base):
    __tablename__ = 'ssismdl_registration_hubs'

    id = Column(BigInteger, primary_key=True)
    token = Column(String(255), nullable=False, server_default="''::character varying")
    hubname = Column(String(255), nullable=False, server_default="''::character varying")
    huburl = Column(String(255), nullable=False, server_default="''::character varying")
    confirmed = Column(SmallInteger, nullable=False, server_default='0')
    secret = Column(String(255))


class Repository(Base):
    __tablename__ = 'ssismdl_repository'

    id = Column(BigInteger, primary_key=True)
    type = Column(String(255), nullable=False, server_default="''::character varying")
    visible = Column(SmallInteger, server_default='1')
    sortorder = Column(BigInteger, nullable=False, server_default='0')


class RepositoryInstanceConfig(Base):
    __tablename__ = 'ssismdl_repository_instance_config'

    id = Column(BigInteger, primary_key=True)
    instanceid = Column(BigInteger, nullable=False)
    name = Column(String(255), nullable=False, server_default="''::character varying")
    value = Column(Text)


class RepositoryInstance(Base):
    __tablename__ = 'ssismdl_repository_instances'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(255), nullable=False, server_default="''::character varying")
    typeid = Column(BigInteger, nullable=False)
    userid = Column(BigInteger, nullable=False, server_default='0')
    contextid = Column(BigInteger, nullable=False)
    username = Column(String(255))
    password = Column(String(255))
    timecreated = Column(BigInteger)
    timemodified = Column(BigInteger)
    readonly = Column(SmallInteger, nullable=False, server_default='0')


class Resource(Base):
    __tablename__ = 'ssismdl_resource'

    id = Column(BigInteger, primary_key=True)
    course = Column(BigInteger, nullable=False, index=True, server_default='0')
    name = Column(String(255), nullable=False, server_default="''::character varying")
    intro = Column(Text)
    introformat = Column(SmallInteger, nullable=False, server_default='0')
    tobemigrated = Column(SmallInteger, nullable=False, server_default='0')
    legacyfiles = Column(SmallInteger, nullable=False, server_default='0')
    legacyfileslast = Column(BigInteger)
    display = Column(SmallInteger, nullable=False, server_default='0')
    displayoptions = Column(Text)
    filterfiles = Column(SmallInteger, nullable=False, server_default='0')
    revision = Column(BigInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')


class ResourceOld(Base):
    __tablename__ = 'ssismdl_resource_old'

    id = Column(BigInteger, primary_key=True)
    course = Column(BigInteger, nullable=False, server_default='0')
    name = Column(String(255), nullable=False, server_default="''::character varying")
    type = Column(String(30), nullable=False, server_default="''::character varying")
    reference = Column(String(255), nullable=False, server_default="''::character varying")
    intro = Column(Text)
    introformat = Column(SmallInteger, nullable=False, server_default='0')
    alltext = Column(Text, nullable=False)
    popup = Column(Text, nullable=False)
    options = Column(String(255), nullable=False, server_default="''::character varying")
    timemodified = Column(BigInteger, nullable=False, server_default='0')
    oldid = Column(BigInteger, nullable=False, unique=True)
    cmid = Column(BigInteger, index=True)
    newmodule = Column(String(50))
    newid = Column(BigInteger)
    migrated = Column(BigInteger, nullable=False, server_default='0')


class Role(Base):
    __tablename__ = 'ssismdl_role'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(255), nullable=False, server_default="''::character varying")
    shortname = Column(String(100), nullable=False, unique=True, server_default="''::character varying")
    description = Column(Text, nullable=False)
    sortorder = Column(BigInteger, nullable=False, unique=True, server_default='0')
    archetype = Column(String(30), nullable=False, server_default="''::character varying")


class RoleAllowAssign(Base):
    __tablename__ = 'ssismdl_role_allow_assign'
    __table_args__ = (
        Index('ssismdl_rolealloassi_rolal_uix', 'roleid', 'allowassign'),
    )

    id = Column(BigInteger, primary_key=True)
    roleid = Column(BigInteger, nullable=False, index=True, server_default='0')
    allowassign = Column(BigInteger, nullable=False, index=True, server_default='0')


class RoleAllowOverride(Base):
    __tablename__ = 'ssismdl_role_allow_override'
    __table_args__ = (
        Index('ssismdl_rolealloover_rolal_uix', 'roleid', 'allowoverride'),
    )

    id = Column(BigInteger, primary_key=True)
    roleid = Column(BigInteger, nullable=False, index=True, server_default='0')
    allowoverride = Column(BigInteger, nullable=False, index=True, server_default='0')


class RoleAllowSwitch(Base):
    __tablename__ = 'ssismdl_role_allow_switch'
    __table_args__ = (
        Index('ssismdl_rolealloswit_rolal_uix', 'roleid', 'allowswitch'),
    )

    id = Column(BigInteger, primary_key=True)
    roleid = Column(BigInteger, nullable=False, index=True)
    allowswitch = Column(BigInteger, nullable=False, index=True)


class RoleAssignment(Base):
    __tablename__ = 'ssismdl_role_assignments'
    __table_args__ = (
        Index('ssismdl_roleassi_rolcon_ix', 'roleid', 'contextid'),
        Index('ssismdl_roleassi_comiteuse_ix', 'component', 'itemid', 'userid'),
        Index('ssismdl_roleassi_useconrol_ix', 'userid', 'contextid', 'roleid')
    )

    id = Column(BigInteger, primary_key=True)
    roleid = Column(BigInteger, nullable=False, index=True, server_default='0')
    contextid = Column(BigInteger, nullable=False, index=True, server_default='0')
    userid = Column(BigInteger, nullable=False, index=True, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')
    modifierid = Column(BigInteger, nullable=False, server_default='0')
    component = Column(String(100), nullable=False, server_default="''::character varying")
    itemid = Column(BigInteger, nullable=False, server_default='0')
    sortorder = Column(BigInteger, nullable=False, index=True, server_default='0')


class RoleCapability(Base):
    __tablename__ = 'ssismdl_role_capabilities'
    __table_args__ = (
        Index('ssismdl_rolecapa_rolconcap_uix', 'roleid', 'contextid', 'capability'),
    )

    id = Column(BigInteger, primary_key=True)
    contextid = Column(BigInteger, nullable=False, index=True, server_default='0')
    roleid = Column(BigInteger, nullable=False, index=True, server_default='0')
    capability = Column(String(255), nullable=False, index=True, server_default="''::character varying")
    permission = Column(BigInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')
    modifierid = Column(BigInteger, nullable=False, index=True, server_default='0')


class RoleContextLevel(Base):
    __tablename__ = 'ssismdl_role_context_levels'
    __table_args__ = (
        Index('ssismdl_rolecontleve_conro_uix', 'contextlevel', 'roleid'),
    )

    id = Column(BigInteger, primary_key=True)
    roleid = Column(BigInteger, nullable=False, index=True)
    contextlevel = Column(BigInteger, nullable=False)


class RoleName(Base):
    __tablename__ = 'ssismdl_role_names'
    __table_args__ = (
        Index('ssismdl_rolename_rolcon_uix', 'roleid', 'contextid'),
    )

    id = Column(BigInteger, primary_key=True)
    roleid = Column(BigInteger, nullable=False, index=True, server_default='0')
    contextid = Column(BigInteger, nullable=False, index=True, server_default='0')
    name = Column(String(255), nullable=False, server_default="''::character varying")


class RoleSortorder(Base):
    __tablename__ = 'ssismdl_role_sortorder'
    __table_args__ = (
        Index('ssismdl_rolesort_userolcon_uix', 'userid', 'roleid', 'contextid'),
    )

    id = Column(BigInteger, primary_key=True)
    userid = Column(BigInteger, nullable=False, index=True)
    roleid = Column(BigInteger, nullable=False, index=True)
    contextid = Column(BigInteger, nullable=False, index=True)
    sortoder = Column(BigInteger, nullable=False)


class Scale(Base):
    __tablename__ = 'ssismdl_scale'

    id = Column(BigInteger, primary_key=True)
    courseid = Column(BigInteger, nullable=False, index=True, server_default='0')
    userid = Column(BigInteger, nullable=False, server_default='0')
    name = Column(String(255), nullable=False, server_default="''::character varying")
    scale = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    descriptionformat = Column(SmallInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')


class ScaleHistory(Base):
    __tablename__ = 'ssismdl_scale_history'

    id = Column(BigInteger, primary_key=True)
    action = Column(BigInteger, nullable=False, index=True, server_default='0')
    oldid = Column(BigInteger, nullable=False, index=True)
    source = Column(String(255))
    timemodified = Column(BigInteger)
    loggeduser = Column(BigInteger, index=True)
    courseid = Column(BigInteger, nullable=False, index=True, server_default='0')
    userid = Column(BigInteger, nullable=False, server_default='0')
    name = Column(String(255), nullable=False, server_default="''::character varying")
    scale = Column(Text, nullable=False)
    description = Column(Text, nullable=False)


class Scheduler(Base):
    __tablename__ = 'ssismdl_scheduler'

    id = Column(BigInteger, primary_key=True)
    course = Column(BigInteger, nullable=False, server_default='0')
    name = Column(String(255), nullable=False, server_default="''::character varying")
    intro = Column(Text, nullable=False)
    introformat = Column(SmallInteger, nullable=False, server_default='0')
    schedulermode = Column(String(10))
    reuseguardtime = Column(BigInteger)
    defaultslotduration = Column(SmallInteger, server_default='15')
    allownotifications = Column(SmallInteger, nullable=False, server_default='0')
    staffrolename = Column(String(40), nullable=False, server_default="''::character varying")
    teacher = Column(BigInteger, nullable=False, server_default='0')
    scale = Column(BigInteger, nullable=False, server_default='0')
    gradingstrategy = Column(SmallInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')


class SchedulerAppointment(Base):
    __tablename__ = 'ssismdl_scheduler_appointment'

    id = Column(BigInteger, primary_key=True)
    slotid = Column(BigInteger, nullable=False)
    studentid = Column(BigInteger, nullable=False)
    attended = Column(SmallInteger, nullable=False)
    grade = Column(SmallInteger)
    appointmentnote = Column(Text)
    appointmentnoteformat = Column(SmallInteger, nullable=False, server_default='0')
    timecreated = Column(BigInteger)
    timemodified = Column(BigInteger)


class SchedulerSlot(Base):
    __tablename__ = 'ssismdl_scheduler_slots'

    id = Column(BigInteger, primary_key=True)
    schedulerid = Column(BigInteger, nullable=False, server_default='0')
    starttime = Column(BigInteger, nullable=False, server_default='0')
    duration = Column(BigInteger, nullable=False, server_default='0')
    teacherid = Column(BigInteger, server_default='0')
    appointmentlocation = Column(String(50), nullable=False, server_default="''::character varying")
    reuse = Column(Integer, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')
    notes = Column(Text)
    notesformat = Column(SmallInteger, nullable=False, server_default='0')
    exclusivity = Column(SmallInteger, nullable=False, server_default='1')
    appointmentnote = Column(Text)
    emaildate = Column(BigInteger, server_default='0')
    hideuntil = Column(BigInteger, server_default='0')


class Scorm(Base):
    __tablename__ = 'ssismdl_scorm'

    id = Column(BigInteger, primary_key=True)
    course = Column(BigInteger, nullable=False, index=True, server_default='0')
    name = Column(String(255), nullable=False, server_default="''::character varying")
    scormtype = Column(String(50), nullable=False, server_default="'local'::character varying")
    reference = Column(String(255), nullable=False, server_default="''::character varying")
    intro = Column(Text, nullable=False)
    introformat = Column(SmallInteger, nullable=False, server_default='0')
    version = Column(String(9), nullable=False, server_default="''::character varying")
    maxgrade = Column(Float(53), nullable=False, server_default='0')
    grademethod = Column(SmallInteger, nullable=False, server_default='0')
    whatgrade = Column(BigInteger, nullable=False, server_default='0')
    maxattempt = Column(BigInteger, nullable=False, server_default='1')
    forcecompleted = Column(SmallInteger, nullable=False, server_default='1')
    forcenewattempt = Column(SmallInteger, nullable=False, server_default='0')
    lastattemptlock = Column(SmallInteger, nullable=False, server_default='0')
    displayattemptstatus = Column(SmallInteger, nullable=False, server_default='1')
    displaycoursestructure = Column(SmallInteger, nullable=False, server_default='1')
    updatefreq = Column(SmallInteger, nullable=False, server_default='0')
    sha1hash = Column(String(40))
    md5hash = Column(String(32), nullable=False, server_default="''::character varying")
    revision = Column(BigInteger, nullable=False, server_default='0')
    launch = Column(BigInteger, nullable=False, server_default='0')
    skipview = Column(SmallInteger, nullable=False, server_default='1')
    hidebrowse = Column(SmallInteger, nullable=False, server_default='0')
    hidetoc = Column(SmallInteger, nullable=False, server_default='0')
    hidenav = Column(SmallInteger, nullable=False, server_default='0')
    auto = Column(SmallInteger, nullable=False, server_default='0')
    popup = Column(SmallInteger, nullable=False, server_default='0')
    options = Column(String(255), nullable=False, server_default="''::character varying")
    width = Column(BigInteger, nullable=False, server_default='100')
    height = Column(BigInteger, nullable=False, server_default='600')
    timeopen = Column(BigInteger, nullable=False, server_default='0')
    timeclose = Column(BigInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')
    completionstatusrequired = Column(SmallInteger)
    completionscorerequired = Column(SmallInteger)


class ScormAiccSession(Base):
    __tablename__ = 'ssismdl_scorm_aicc_session'

    id = Column(BigInteger, primary_key=True)
    userid = Column(BigInteger, nullable=False, index=True, server_default='0')
    scormid = Column(BigInteger, nullable=False, index=True, server_default='0')
    hacpsession = Column(String(255), nullable=False, server_default="''::character varying")
    scoid = Column(BigInteger, server_default='0')
    scormmode = Column(String(50))
    scormstatus = Column(String(255))
    attempt = Column(BigInteger)
    lessonstatus = Column(String(255))
    sessiontime = Column(String(255))
    timecreated = Column(BigInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')


class ScormSco(Base):
    __tablename__ = 'ssismdl_scorm_scoes'

    id = Column(BigInteger, primary_key=True)
    scorm = Column(BigInteger, nullable=False, index=True, server_default='0')
    manifest = Column(String(255), nullable=False, server_default="''::character varying")
    organization = Column(String(255), nullable=False, server_default="''::character varying")
    parent = Column(String(255), nullable=False, server_default="''::character varying")
    identifier = Column(String(255), nullable=False, server_default="''::character varying")
    launch = Column(Text, nullable=False)
    scormtype = Column(String(5), nullable=False, server_default="''::character varying")
    title = Column(String(255), nullable=False, server_default="''::character varying")


class ScormScoesDatum(Base):
    __tablename__ = 'ssismdl_scorm_scoes_data'

    id = Column(BigInteger, primary_key=True)
    scoid = Column(BigInteger, nullable=False, index=True, server_default='0')
    name = Column(String(255), nullable=False, server_default="''::character varying")
    value = Column(Text, nullable=False)


class ScormScoesTrack(Base):
    __tablename__ = 'ssismdl_scorm_scoes_track'
    __table_args__ = (
        Index('ssismdl_scorscoetrac_usesc_uix', 'userid', 'scormid', 'scoid', 'attempt', 'element'),
    )

    id = Column(BigInteger, primary_key=True)
    userid = Column(BigInteger, nullable=False, index=True, server_default='0')
    scormid = Column(BigInteger, nullable=False, index=True, server_default='0')
    scoid = Column(BigInteger, nullable=False, index=True, server_default='0')
    attempt = Column(BigInteger, nullable=False, server_default='1')
    element = Column(String(255), nullable=False, index=True, server_default="''::character varying")
    value = Column(Text, nullable=False)
    timemodified = Column(BigInteger, nullable=False, server_default='0')


class ScormSeqMapinfo(Base):
    __tablename__ = 'ssismdl_scorm_seq_mapinfo'
    __table_args__ = (
        Index('ssismdl_scorseqmapi_scoido_uix', 'scoid', 'id', 'objectiveid'),
    )

    id = Column(BigInteger, primary_key=True)
    scoid = Column(BigInteger, nullable=False, index=True, server_default='0')
    objectiveid = Column(BigInteger, nullable=False, index=True, server_default='0')
    targetobjectiveid = Column(BigInteger, nullable=False, server_default='0')
    readsatisfiedstatus = Column(SmallInteger, nullable=False, server_default='1')
    readnormalizedmeasure = Column(SmallInteger, nullable=False, server_default='1')
    writesatisfiedstatus = Column(SmallInteger, nullable=False, server_default='0')
    writenormalizedmeasure = Column(SmallInteger, nullable=False, server_default='0')


class ScormSeqObjective(Base):
    __tablename__ = 'ssismdl_scorm_seq_objective'
    __table_args__ = (
        Index('ssismdl_scorseqobje_scoid_uix', 'scoid', 'id'),
    )

    id = Column(BigInteger, primary_key=True)
    scoid = Column(BigInteger, nullable=False, index=True, server_default='0')
    primaryobj = Column(SmallInteger, nullable=False, server_default='0')
    objectiveid = Column(String(255), nullable=False, server_default="''::character varying")
    satisfiedbymeasure = Column(SmallInteger, nullable=False, server_default='1')
    minnormalizedmeasure = Column(Float, nullable=False, server_default='0.0000')


class ScormSeqRolluprule(Base):
    __tablename__ = 'ssismdl_scorm_seq_rolluprule'
    __table_args__ = (
        Index('ssismdl_scorseqroll_scoid_uix', 'scoid', 'id'),
    )

    id = Column(BigInteger, primary_key=True)
    scoid = Column(BigInteger, nullable=False, index=True, server_default='0')
    childactivityset = Column(String(15), nullable=False, server_default="''::character varying")
    minimumcount = Column(BigInteger, nullable=False, server_default='0')
    minimumpercent = Column(Float, nullable=False, server_default='0.0000')
    conditioncombination = Column(String(3), nullable=False, server_default="'all'::character varying")
    action = Column(String(15), nullable=False, server_default="''::character varying")


class ScormSeqRolluprulecond(Base):
    __tablename__ = 'ssismdl_scorm_seq_rolluprulecond'
    __table_args__ = (
        Index('ssismdl_scorseqroll_scorol_uix', 'scoid', 'rollupruleid', 'id'),
    )

    id = Column(BigInteger, primary_key=True)
    scoid = Column(BigInteger, nullable=False, index=True, server_default='0')
    rollupruleid = Column(BigInteger, nullable=False, index=True, server_default='0')
    operator = Column(String(5), nullable=False, server_default="'noOp'::character varying")
    cond = Column(String(25), nullable=False, server_default="''::character varying")


class ScormSeqRulecond(Base):
    __tablename__ = 'ssismdl_scorm_seq_rulecond'
    __table_args__ = (
        Index('ssismdl_scorseqrule_idscor_uix', 'id', 'scoid', 'ruleconditionsid'),
    )

    id = Column(BigInteger, primary_key=True)
    scoid = Column(BigInteger, nullable=False, index=True, server_default='0')
    ruleconditionsid = Column(BigInteger, nullable=False, index=True, server_default='0')
    refrencedobjective = Column(String(255), nullable=False, server_default="''::character varying")
    measurethreshold = Column(Float, nullable=False, server_default='0.0000')
    operator = Column(String(5), nullable=False, server_default="'noOp'::character varying")
    cond = Column(String(30), nullable=False, server_default="'always'::character varying")


class ScormSeqRuleconds(Base):
    __tablename__ = 'ssismdl_scorm_seq_ruleconds'
    __table_args__ = (
        Index('ssismdl_scorseqrule_scoid_uix', 'scoid', 'id'),
    )

    id = Column(BigInteger, primary_key=True)
    scoid = Column(BigInteger, nullable=False, index=True, server_default='0')
    conditioncombination = Column(String(3), nullable=False, server_default="'all'::character varying")
    ruletype = Column(SmallInteger, nullable=False, server_default='0')
    action = Column(String(25), nullable=False, server_default="''::character varying")


class Session(Base):
    __tablename__ = 'ssismdl_sessions'

    id = Column(BigInteger, primary_key=True)
    state = Column(BigInteger, nullable=False, index=True, server_default='0')
    sid = Column(String(128), nullable=False, unique=True, server_default="''::character varying")
    userid = Column(BigInteger, nullable=False, index=True)
    sessdata = Column(Text)
    timecreated = Column(BigInteger, nullable=False, index=True)
    timemodified = Column(BigInteger, nullable=False, index=True)
    firstip = Column(String(45))
    lastip = Column(String(45))


class Slideshow(Base):
    __tablename__ = 'ssismdl_slideshow'

    id = Column(BigInteger, primary_key=True)
    course = Column(BigInteger, nullable=False, index=True, server_default='0')
    name = Column(String(255), nullable=False, server_default="''::character varying")
    location = Column(Text, nullable=False)
    layout = Column(SmallInteger, nullable=False, server_default='0')
    filename = Column(SmallInteger, nullable=False, server_default='0')
    delaytime = Column(SmallInteger, nullable=False, server_default='7')
    centred = Column(SmallInteger, nullable=False, server_default='0')
    autobgcolor = Column(SmallInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')
    htmlcaptions = Column(SmallInteger, nullable=False, server_default='1')
    keeporiginals = Column(SmallInteger, nullable=False, server_default='1')


class SlideshowCaption(Base):
    __tablename__ = 'ssismdl_slideshow_captions'

    id = Column(BigInteger, primary_key=True)
    slideshow = Column(BigInteger, nullable=False, index=True, server_default='0')
    image = Column(Text, nullable=False)
    title = Column(Text, nullable=False)
    caption = Column(Text, nullable=False)


class StatsDaily(Base):
    __tablename__ = 'ssismdl_stats_daily'

    id = Column(BigInteger, primary_key=True)
    courseid = Column(BigInteger, nullable=False, index=True, server_default='0')
    timeend = Column(BigInteger, nullable=False, index=True, server_default='0')
    roleid = Column(BigInteger, nullable=False, index=True, server_default='0')
    stattype = Column(String(20), nullable=False, server_default="'activity'::character varying")
    stat1 = Column(BigInteger, nullable=False, server_default='0')
    stat2 = Column(BigInteger, nullable=False, server_default='0')


class StatsMonthly(Base):
    __tablename__ = 'ssismdl_stats_monthly'

    id = Column(BigInteger, primary_key=True)
    courseid = Column(BigInteger, nullable=False, index=True, server_default='0')
    timeend = Column(BigInteger, nullable=False, index=True, server_default='0')
    roleid = Column(BigInteger, nullable=False, index=True, server_default='0')
    stattype = Column(String(20), nullable=False, server_default="'activity'::character varying")
    stat1 = Column(BigInteger, nullable=False, server_default='0')
    stat2 = Column(BigInteger, nullable=False, server_default='0')


class StatsUserDaily(Base):
    __tablename__ = 'ssismdl_stats_user_daily'

    id = Column(BigInteger, primary_key=True)
    courseid = Column(BigInteger, nullable=False, index=True, server_default='0')
    userid = Column(BigInteger, nullable=False, index=True, server_default='0')
    roleid = Column(BigInteger, nullable=False, index=True, server_default='0')
    timeend = Column(BigInteger, nullable=False, index=True, server_default='0')
    statsreads = Column(BigInteger, nullable=False, server_default='0')
    statswrites = Column(BigInteger, nullable=False, server_default='0')
    stattype = Column(String(30), nullable=False, server_default="''::character varying")


class StatsUserMonthly(Base):
    __tablename__ = 'ssismdl_stats_user_monthly'

    id = Column(BigInteger, primary_key=True)
    courseid = Column(BigInteger, nullable=False, index=True, server_default='0')
    userid = Column(BigInteger, nullable=False, index=True, server_default='0')
    roleid = Column(BigInteger, nullable=False, index=True, server_default='0')
    timeend = Column(BigInteger, nullable=False, index=True, server_default='0')
    statsreads = Column(BigInteger, nullable=False, server_default='0')
    statswrites = Column(BigInteger, nullable=False, server_default='0')
    stattype = Column(String(30), nullable=False, server_default="''::character varying")


class StatsUserWeekly(Base):
    __tablename__ = 'ssismdl_stats_user_weekly'

    id = Column(BigInteger, primary_key=True)
    courseid = Column(BigInteger, nullable=False, index=True, server_default='0')
    userid = Column(BigInteger, nullable=False, index=True, server_default='0')
    roleid = Column(BigInteger, nullable=False, index=True, server_default='0')
    timeend = Column(BigInteger, nullable=False, index=True, server_default='0')
    statsreads = Column(BigInteger, nullable=False, server_default='0')
    statswrites = Column(BigInteger, nullable=False, server_default='0')
    stattype = Column(String(30), nullable=False, server_default="''::character varying")


class StatsWeekly(Base):
    __tablename__ = 'ssismdl_stats_weekly'

    id = Column(BigInteger, primary_key=True)
    courseid = Column(BigInteger, nullable=False, index=True, server_default='0')
    timeend = Column(BigInteger, nullable=False, index=True, server_default='0')
    roleid = Column(BigInteger, nullable=False, index=True, server_default='0')
    stattype = Column(String(20), nullable=False, server_default="'activity'::character varying")
    stat1 = Column(BigInteger, nullable=False, server_default='0')
    stat2 = Column(BigInteger, nullable=False, server_default='0')


class Survey(Base):
    __tablename__ = 'ssismdl_survey'

    id = Column(BigInteger, primary_key=True)
    course = Column(BigInteger, nullable=False, index=True, server_default='0')
    template = Column(BigInteger, nullable=False, server_default='0')
    days = Column(Integer, nullable=False, server_default='0')
    timecreated = Column(BigInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')
    name = Column(String(255), nullable=False, server_default="''::character varying")
    intro = Column(Text, nullable=False)
    introformat = Column(SmallInteger, nullable=False, server_default='0')
    questions = Column(String(255), nullable=False, server_default="''::character varying")


class SurveyAnalysi(Base):
    __tablename__ = 'ssismdl_survey_analysis'

    id = Column(BigInteger, primary_key=True)
    survey = Column(BigInteger, nullable=False, index=True, server_default='0')
    userid = Column(BigInteger, nullable=False, index=True, server_default='0')
    notes = Column(Text, nullable=False)


class SurveyAnswer(Base):
    __tablename__ = 'ssismdl_survey_answers'

    id = Column(BigInteger, primary_key=True)
    userid = Column(BigInteger, nullable=False, index=True, server_default='0')
    survey = Column(BigInteger, nullable=False, index=True, server_default='0')
    question = Column(BigInteger, nullable=False, index=True, server_default='0')
    time = Column(BigInteger, nullable=False, server_default='0')
    answer1 = Column(Text, nullable=False)
    answer2 = Column(Text, nullable=False)


class SurveyQuestion(Base):
    __tablename__ = 'ssismdl_survey_questions'

    id = Column(BigInteger, primary_key=True)
    text = Column(String(255), nullable=False, server_default="''::character varying")
    shorttext = Column(String(30), nullable=False, server_default="''::character varying")
    multi = Column(String(100), nullable=False, server_default="''::character varying")
    intro = Column(String(50), nullable=False, server_default="''::character varying")
    type = Column(SmallInteger, nullable=False, server_default='0')
    options = Column(Text)


class Tag(Base):
    __tablename__ = 'ssismdl_tag'
    __table_args__ = (
        Index('ssismdl_tag_idnam_uix', 'id', 'name'),
    )

    id = Column(BigInteger, primary_key=True)
    userid = Column(BigInteger, nullable=False, index=True)
    name = Column(String(255), nullable=False, unique=True, server_default="''::character varying")
    rawname = Column(String(255), nullable=False, server_default="''::character varying")
    tagtype = Column(String(255))
    description = Column(Text)
    descriptionformat = Column(SmallInteger, nullable=False, server_default='0')
    flag = Column(SmallInteger, server_default='0')
    timemodified = Column(BigInteger)


class TagCorrelation(Base):
    __tablename__ = 'ssismdl_tag_correlation'

    id = Column(BigInteger, primary_key=True)
    tagid = Column(BigInteger, nullable=False, index=True)
    correlatedtags = Column(Text, nullable=False)


class TagInstance(Base):
    __tablename__ = 'ssismdl_tag_instance'
    __table_args__ = (
        Index('ssismdl_taginst_iteitetagt_uix', 'itemtype', 'itemid', 'tagid', 'tiuserid'),
    )

    id = Column(BigInteger, primary_key=True)
    tagid = Column(BigInteger, nullable=False, index=True)
    itemtype = Column(String(255), nullable=False, server_default="''::character varying")
    itemid = Column(BigInteger, nullable=False)
    tiuserid = Column(BigInteger, nullable=False, server_default='0')
    ordering = Column(BigInteger)
    timemodified = Column(BigInteger, nullable=False, server_default='0')


class TempEnroledTemplate(Base):
    __tablename__ = 'ssismdl_temp_enroled_template'

    id = Column(BigInteger, primary_key=True)
    userid = Column(BigInteger, nullable=False, index=True, server_default='0')
    courseid = Column(BigInteger, nullable=False, index=True, server_default='0')
    roleid = Column(BigInteger, nullable=False, index=True)


class TempLogTemplate(Base):
    __tablename__ = 'ssismdl_temp_log_template'
    __table_args__ = (
        Index('ssismdl_templogtemp_usecoua_ix', 'userid', 'course', 'action'),
    )

    id = Column(BigInteger, primary_key=True)
    userid = Column(BigInteger, nullable=False, index=True, server_default='0')
    course = Column(BigInteger, nullable=False, index=True, server_default='0')
    action = Column(String(40), nullable=False, index=True, server_default="''::character varying")


class Timezone(Base):
    __tablename__ = 'ssismdl_timezone'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(100), nullable=False, server_default="''::character varying")
    year = Column(BigInteger, nullable=False, server_default='0')
    tzrule = Column(String(20), nullable=False, server_default="''::character varying")
    gmtoff = Column(BigInteger, nullable=False, server_default='0')
    dstoff = Column(BigInteger, nullable=False, server_default='0')
    dst_month = Column(SmallInteger, nullable=False, server_default='0')
    dst_startday = Column(SmallInteger, nullable=False, server_default='0')
    dst_weekday = Column(SmallInteger, nullable=False, server_default='0')
    dst_skipweeks = Column(SmallInteger, nullable=False, server_default='0')
    dst_time = Column(String(6), nullable=False, server_default="'00:00'::character varying")
    std_month = Column(SmallInteger, nullable=False, server_default='0')
    std_startday = Column(SmallInteger, nullable=False, server_default='0')
    std_weekday = Column(SmallInteger, nullable=False, server_default='0')
    std_skipweeks = Column(SmallInteger, nullable=False, server_default='0')
    std_time = Column(String(6), nullable=False, server_default="'00:00'::character varying")


class ToolCustomlang(Base):
    __tablename__ = 'ssismdl_tool_customlang'
    __table_args__ = (
        Index('ssismdl_toolcust_lancomstr_uix', 'lang', 'componentid', 'stringid'),
    )

    id = Column(BigInteger, primary_key=True)
    lang = Column(String(20), nullable=False, server_default="''::character varying")
    componentid = Column(BigInteger, nullable=False, index=True)
    stringid = Column(String(255), nullable=False, server_default="''::character varying")
    original = Column(Text, nullable=False)
    master = Column(Text)
    local = Column(Text)
    timemodified = Column(BigInteger, nullable=False)
    timecustomized = Column(BigInteger)
    outdated = Column(SmallInteger, server_default='0')
    modified = Column(SmallInteger, server_default='0')


class ToolCustomlangComponent(Base):
    __tablename__ = 'ssismdl_tool_customlang_components'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(255), nullable=False, server_default="''::character varying")
    version = Column(String(255))


class Turnitintool(Base):
    __tablename__ = 'ssismdl_turnitintool'

    id = Column(BigInteger, primary_key=True)
    course = Column(BigInteger, nullable=False, index=True, server_default='0')
    type = Column(BigInteger, nullable=False, server_default='0')
    name = Column(String(255), nullable=False, server_default="''::character varying")
    grade = Column(BigInteger, nullable=False, server_default='0')
    numparts = Column(BigInteger, nullable=False, server_default='0')
    defaultdtstart = Column(BigInteger, nullable=False, server_default='0')
    defaultdtdue = Column(BigInteger, nullable=False, server_default='0')
    defaultdtpost = Column(BigInteger, nullable=False, server_default='0')
    anon = Column(SmallInteger, server_default='0')
    portfolio = Column(SmallInteger, server_default='0')
    allowlate = Column(SmallInteger, nullable=False, server_default='0')
    reportgenspeed = Column(SmallInteger, nullable=False, server_default='0')
    submitpapersto = Column(SmallInteger, nullable=False, server_default='0')
    spapercheck = Column(SmallInteger, nullable=False, server_default='0')
    internetcheck = Column(SmallInteger, nullable=False, server_default='0')
    journalcheck = Column(SmallInteger, nullable=False, server_default='0')
    maxfilesize = Column(BigInteger, server_default='0')
    intro = Column(Text)
    introformat = Column(SmallInteger, nullable=False, server_default='0')
    timecreated = Column(BigInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')
    studentreports = Column(BigInteger, nullable=False, server_default='0')
    dateformat = Column(Text, nullable=False)
    usegrademark = Column(BigInteger, nullable=False)
    gradedisplay = Column(BigInteger, nullable=False)
    autoupdates = Column(BigInteger, nullable=False)
    commentedittime = Column(BigInteger, nullable=False)
    commentmaxsize = Column(BigInteger, nullable=False)
    autosubmission = Column(BigInteger, nullable=False)
    shownonsubmission = Column(BigInteger, nullable=False)
    excludebiblio = Column(SmallInteger, nullable=False, server_default='0')
    excludequoted = Column(SmallInteger, nullable=False, server_default='0')
    excludevalue = Column(Integer, nullable=False, server_default='0')
    excludetype = Column(SmallInteger, nullable=False, server_default='1')
    perpage = Column(BigInteger, nullable=False, server_default='25')
    erater = Column(BigInteger, nullable=False, server_default='0')
    erater_handbook = Column(BigInteger, nullable=False, server_default='0')
    erater_dictionary = Column(String(10))
    erater_spelling = Column(BigInteger, nullable=False, server_default='0')
    erater_grammar = Column(BigInteger, nullable=False, server_default='0')
    erater_usage = Column(BigInteger, nullable=False, server_default='0')
    erater_mechanics = Column(BigInteger, nullable=False, server_default='0')
    erater_style = Column(BigInteger, nullable=False, server_default='0')
    transmatch = Column(BigInteger, server_default='0')


class TurnitintoolComment(Base):
    __tablename__ = 'ssismdl_turnitintool_comments'

    id = Column(BigInteger, primary_key=True)
    submissionid = Column(BigInteger, nullable=False)
    userid = Column(BigInteger, nullable=False)
    commenttext = Column(Text, nullable=False)
    dateupdated = Column(BigInteger, nullable=False)
    deleted = Column(BigInteger, nullable=False)


class TurnitintoolCourse(Base):
    __tablename__ = 'ssismdl_turnitintool_courses'

    id = Column(BigInteger, primary_key=True)
    courseid = Column(BigInteger, nullable=False)
    ownerid = Column(BigInteger, nullable=False)
    turnitin_ctl = Column(Text, nullable=False)
    turnitin_cid = Column(BigInteger, nullable=False)


class TurnitintoolPart(Base):
    __tablename__ = 'ssismdl_turnitintool_parts'

    id = Column(BigInteger, primary_key=True)
    turnitintoolid = Column(BigInteger, nullable=False)
    partname = Column(Text, nullable=False)
    tiiassignid = Column(BigInteger, nullable=False)
    dtstart = Column(BigInteger, nullable=False)
    dtdue = Column(BigInteger, nullable=False)
    dtpost = Column(BigInteger, nullable=False)
    maxmarks = Column(BigInteger, nullable=False)
    deleted = Column(BigInteger, nullable=False)


class TurnitintoolSubmission(Base):
    __tablename__ = 'ssismdl_turnitintool_submissions'

    id = Column(BigInteger, primary_key=True)
    userid = Column(BigInteger, nullable=False, index=True)
    turnitintoolid = Column(BigInteger, nullable=False, index=True)
    submission_part = Column(BigInteger)
    submission_title = Column(Text, nullable=False)
    submission_type = Column(SmallInteger, nullable=False, server_default='0')
    submission_filename = Column(Text)
    submission_objectid = Column(BigInteger)
    submission_score = Column(BigInteger)
    submission_grade = Column(BigInteger)
    submission_gmimaged = Column(BigInteger, server_default='0')
    submission_status = Column(Text)
    submission_queued = Column(BigInteger, server_default='0')
    submission_attempts = Column(BigInteger, nullable=False, server_default='0')
    submission_modified = Column(BigInteger, nullable=False, server_default='0')
    submission_parent = Column(BigInteger, server_default='0')
    submission_nmuserid = Column(String(100))
    submission_nmfirstname = Column(Text)
    submission_nmlastname = Column(Text)
    submission_unanon = Column(SmallInteger, nullable=False, server_default='0')
    submission_unanonreason = Column(Text)
    submission_transmatch = Column(BigInteger, server_default='0')


class TurnitintoolUser(Base):
    __tablename__ = 'ssismdl_turnitintool_users'

    id = Column(BigInteger, primary_key=True)
    userid = Column(BigInteger, nullable=False, unique=True)
    turnitin_uid = Column(BigInteger, nullable=False)
    turnitin_utp = Column(BigInteger, nullable=False, server_default='0')


class UpgradeLog(Base):
    __tablename__ = 'ssismdl_upgrade_log'
    __table_args__ = (
        Index('ssismdl_upgrlog_typtim_ix', 'type', 'timemodified'),
    )

    id = Column(BigInteger, primary_key=True)
    type = Column(BigInteger, nullable=False)
    plugin = Column(String(100))
    version = Column(String(100))
    targetversion = Column(String(100))
    info = Column(String(255), nullable=False, server_default="''::character varying")
    details = Column(Text)
    backtrace = Column(Text)
    userid = Column(BigInteger, nullable=False, index=True)
    timemodified = Column(BigInteger, nullable=False, index=True)


class Url(Base):
    __tablename__ = 'ssismdl_url'

    id = Column(BigInteger, primary_key=True)
    course = Column(BigInteger, nullable=False, index=True, server_default='0')
    name = Column(String(255), nullable=False, server_default="''::character varying")
    intro = Column(Text)
    introformat = Column(SmallInteger, nullable=False, server_default='0')
    externalurl = Column(Text, nullable=False)
    display = Column(SmallInteger, nullable=False, server_default='0')
    displayoptions = Column(Text)
    parameters = Column(Text)
    timemodified = Column(BigInteger, nullable=False, server_default='0')


class User(Base):
    __tablename__ = 'ssismdl_user'
    __table_args__ = (
        Index('ssismdl_user_mneuse_uix', 'mnethostid', 'username'),
    )

    id = Column(BigInteger, primary_key=True)
    auth = Column(String(20), nullable=False, index=True, server_default="'manual'::character varying")
    confirmed = Column(SmallInteger, nullable=False, index=True, server_default='0')
    policyagreed = Column(SmallInteger, nullable=False, server_default='0')
    deleted = Column(SmallInteger, nullable=False, index=True, server_default='0')
    suspended = Column(SmallInteger, nullable=False, server_default='0')
    mnethostid = Column(BigInteger, nullable=False, server_default='0')
    username = Column(String(100), nullable=False, server_default="''::character varying")
    password = Column(String(255), nullable=False, server_default="''::character varying")
    idnumber = Column(String(255), nullable=False, index=True, server_default="''::character varying")
    firstname = Column(String(100), nullable=False, index=True, server_default="''::character varying")
    lastname = Column(String(100), nullable=False, index=True, server_default="''::character varying")
    email = Column(String(100), nullable=False, index=True, server_default="''::character varying")
    emailstop = Column(SmallInteger, nullable=False, server_default='0')
    icq = Column(String(15), nullable=False, server_default="''::character varying")
    skype = Column(String(50), nullable=False, server_default="''::character varying")
    yahoo = Column(String(50), nullable=False, server_default="''::character varying")
    aim = Column(String(50), nullable=False, server_default="''::character varying")
    msn = Column(String(50), nullable=False, server_default="''::character varying")
    phone1 = Column(String(20), nullable=False, server_default="''::character varying")
    phone2 = Column(String(20), nullable=False, server_default="''::character varying")
    institution = Column(String(40), nullable=False, server_default="''::character varying")
    department = Column(String(30), nullable=False, server_default="''::character varying")
    address = Column(String(70), nullable=False, server_default="''::character varying")
    city = Column(String(120), nullable=False, index=True, server_default="''::character varying")
    country = Column(String(2), nullable=False, index=True, server_default="''::character varying")
    lang = Column(String(30), nullable=False, server_default="'en'::character varying")
    theme = Column(String(50), nullable=False, server_default="''::character varying")
    timezone = Column(String(100), nullable=False, server_default="'99'::character varying")
    firstaccess = Column(BigInteger, nullable=False, server_default='0')
    lastaccess = Column(BigInteger, nullable=False, index=True, server_default='0')
    lastlogin = Column(BigInteger, nullable=False, server_default='0')
    currentlogin = Column(BigInteger, nullable=False, server_default='0')
    lastip = Column(String(45), nullable=False, server_default="''::character varying")
    secret = Column(String(15), nullable=False, server_default="''::character varying")
    picture = Column(BigInteger, nullable=False, server_default='0')
    url = Column(String(255), nullable=False, server_default="''::character varying")
    description = Column(Text)
    descriptionformat = Column(SmallInteger, nullable=False, server_default='1')
    mailformat = Column(SmallInteger, nullable=False, server_default='1')
    maildigest = Column(SmallInteger, nullable=False, server_default='0')
    maildisplay = Column(SmallInteger, nullable=False, server_default='2')
    #htmleditor = Column(SmallInteger, nullable=False, server_default='1')
    autosubscribe = Column(SmallInteger, nullable=False, server_default='1')
    trackforums = Column(SmallInteger, nullable=False, server_default='0')
    timecreated = Column(BigInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')
    trustbitmask = Column(BigInteger, nullable=False, server_default='0')
    imagealt = Column(String(255))
    #password2 = Column(String(255))


class UserActivityBu(Base):
    __tablename__ = 'ssismdl_user_activity_bus'

    id = Column(BigInteger, primary_key=True)
    userid = Column(BigInteger, nullable=False, index=True, server_default="nextval('ssismdl_user_activity_bus_userid_seq'::regclass)")
    bus = Column(SmallInteger, nullable=False)


class UserEmailPasswordReset(Base):
    __tablename__ = 'ssismdl_user_email_password_reset'

    userid = Column(String)
    powerschoolid = Column(String, primary_key=True)
    name = Column(String)
    email = Column(String)


class UserEnrolment(Base):
    __tablename__ = 'ssismdl_user_enrolments'
    __table_args__ = (
        Index('ssismdl_userenro_enruse_uix', 'enrolid', 'userid'),
    )

    id = Column(BigInteger, primary_key=True)
    status = Column(BigInteger, nullable=False, server_default='0')
    enrolid = Column(BigInteger, nullable=False, index=True)
    userid = Column(BigInteger, nullable=False, index=True)
    timestart = Column(BigInteger, nullable=False, server_default='0')
    timeend = Column(BigInteger, nullable=False, server_default='2147483647')
    modifierid = Column(BigInteger, nullable=False, index=True, server_default='0')
    timecreated = Column(BigInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')


class UserInfoCategory(Base):
    __tablename__ = 'ssismdl_user_info_category'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(255), nullable=False, server_default="''::character varying")
    sortorder = Column(BigInteger, nullable=False, server_default='0')


class UserInfoDatum(Base):
    __tablename__ = 'ssismdl_user_info_data'
    __table_args__ = (
        Index('ssismdl_userinfodata_usefie_ix', 'userid', 'fieldid'),
    )

    id = Column(BigInteger, primary_key=True)
    userid = Column(BigInteger, nullable=False, server_default='0')
    fieldid = Column(BigInteger, nullable=False, server_default='0')
    data = Column(Text, nullable=False)
    dataformat = Column(SmallInteger, nullable=False, server_default='0')

class UserInfoField(Base):
    __tablename__ = 'ssismdl_user_info_field'

    id = Column(BigInteger, primary_key=True)
    shortname = Column(String(255), nullable=False, server_default="'shortname'::character varying")
    name = Column(Text, nullable=False)
    datatype = Column(String(255), nullable=False, server_default="''::character varying")
    description = Column(Text)
    descriptionformat = Column(SmallInteger, nullable=False, server_default='0')
    categoryid = Column(BigInteger, nullable=False, server_default='0')
    sortorder = Column(BigInteger, nullable=False, server_default='0')
    required = Column(SmallInteger, nullable=False, server_default='0')
    locked = Column(SmallInteger, nullable=False, server_default='0')
    visible = Column(SmallInteger, nullable=False, server_default='0')
    forceunique = Column(SmallInteger, nullable=False, server_default='0')
    signup = Column(SmallInteger, nullable=False, server_default='0')
    defaultdata = Column(Text)
    defaultdataformat = Column(SmallInteger, nullable=False, server_default='0')
    param1 = Column(Text)
    param2 = Column(Text)
    param3 = Column(Text)
    param4 = Column(Text)
    param5 = Column(Text)


class UserLastacces(Base):
    __tablename__ = 'ssismdl_user_lastaccess'
    __table_args__ = (
        Index('ssismdl_userlast_usecou_uix', 'userid', 'courseid'),
    )

    id = Column(BigInteger, primary_key=True)
    userid = Column(BigInteger, nullable=False, index=True, server_default='0')
    courseid = Column(BigInteger, nullable=False, index=True, server_default='0')
    timeaccess = Column(BigInteger, nullable=False, server_default='0')


class UserPreference(Base):
    __tablename__ = 'ssismdl_user_preferences'
    __table_args__ = (
        Index('ssismdl_userpref_usenam_uix', 'userid', 'name'),
    )

    id = Column(BigInteger, primary_key=True)
    userid = Column(BigInteger, nullable=False, server_default='0')
    name = Column(String(255), nullable=False, server_default="''::character varying")
    value = Column(String(1333), nullable=False, server_default="''::character varying")


class UserPrivateKey(Base):
    __tablename__ = 'ssismdl_user_private_key'
    __table_args__ = (
        Index('ssismdl_userprivkey_scrval_ix', 'script', 'value'),
    )

    id = Column(BigInteger, primary_key=True)
    script = Column(String(128), nullable=False, server_default="''::character varying")
    value = Column(String(128), nullable=False, server_default="''::character varying")
    userid = Column(BigInteger, nullable=False, index=True)
    instance = Column(BigInteger)
    iprestriction = Column(String(255))
    validuntil = Column(BigInteger)
    timecreated = Column(BigInteger)


class WebdavLock(Base):
    __tablename__ = 'ssismdl_webdav_locks'

    id = Column(BigInteger, primary_key=True)
    token = Column(String(255), nullable=False, unique=True, server_default="''::character varying")
    path = Column(String(255), nullable=False, index=True, server_default="''::character varying")
    expiry = Column(BigInteger, nullable=False, index=True, server_default='0')
    userid = Column(BigInteger, nullable=False, server_default='0')
    recursive = Column(SmallInteger, nullable=False, server_default='0')
    exclusivelock = Column(SmallInteger, nullable=False, server_default='0')
    created = Column(BigInteger, nullable=False, server_default='0')
    modified = Column(BigInteger, nullable=False, server_default='0')
    owner = Column(String(255))


class Wiki(Base):
    __tablename__ = 'ssismdl_wiki'

    id = Column(BigInteger, primary_key=True)
    course = Column(BigInteger, nullable=False, index=True, server_default='0')
    name = Column(String(255), nullable=False, server_default="'Wiki'::character varying")
    intro = Column(Text)
    introformat = Column(SmallInteger, nullable=False, server_default='0')
    timecreated = Column(BigInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')
    firstpagetitle = Column(String(255), nullable=False, server_default="'First Page'::character varying")
    wikimode = Column(String(20), nullable=False, server_default="'collaborative'::character varying")
    defaultformat = Column(String(20), nullable=False, server_default="'creole'::character varying")
    forceformat = Column(SmallInteger, nullable=False, server_default='1')
    editbegin = Column(BigInteger, nullable=False, server_default='0')
    editend = Column(BigInteger, server_default='0')


class WikiLink(Base):
    __tablename__ = 'ssismdl_wiki_links'

    id = Column(BigInteger, primary_key=True)
    subwikiid = Column(BigInteger, nullable=False, index=True, server_default='0')
    frompageid = Column(BigInteger, nullable=False, index=True, server_default='0')
    topageid = Column(BigInteger, nullable=False, server_default='0')
    tomissingpage = Column(String(255))


class WikiLock(Base):
    __tablename__ = 'ssismdl_wiki_locks'

    id = Column(BigInteger, primary_key=True)
    pageid = Column(BigInteger, nullable=False, server_default='0')
    sectionname = Column(String(255))
    userid = Column(BigInteger, nullable=False, server_default='0')
    lockedat = Column(BigInteger, nullable=False, server_default='0')


class WikiPage(Base):
    __tablename__ = 'ssismdl_wiki_pages'
    __table_args__ = (
        Index('ssismdl_wikipage_subtituse_uix', 'subwikiid', 'title', 'userid'),
    )

    id = Column(BigInteger, primary_key=True)
    subwikiid = Column(BigInteger, nullable=False, index=True, server_default='0')
    title = Column(String(255), nullable=False, server_default="'title'::character varying")
    cachedcontent = Column(Text, nullable=False)
    timecreated = Column(BigInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')
    timerendered = Column(BigInteger, nullable=False, server_default='0')
    userid = Column(BigInteger, nullable=False, server_default='0')
    pageviews = Column(BigInteger, nullable=False, server_default='0')
    readonly = Column(SmallInteger, nullable=False, server_default='0')


class WikiSubwiki(Base):
    __tablename__ = 'ssismdl_wiki_subwikis'
    __table_args__ = (
        Index('ssismdl_wikisubw_wikgrouse_uix', 'wikiid', 'groupid', 'userid'),
    )

    id = Column(BigInteger, primary_key=True)
    wikiid = Column(BigInteger, nullable=False, index=True, server_default='0')
    groupid = Column(BigInteger, nullable=False, server_default='0')
    userid = Column(BigInteger, nullable=False, server_default='0')


class WikiSynonym(Base):
    __tablename__ = 'ssismdl_wiki_synonyms'
    __table_args__ = (
        Index('ssismdl_wikisyno_pagpag_uix', 'pageid', 'pagesynonym'),
    )

    id = Column(BigInteger, primary_key=True)
    subwikiid = Column(BigInteger, nullable=False, server_default='0')
    pageid = Column(BigInteger, nullable=False, server_default='0')
    pagesynonym = Column(String(255), nullable=False, server_default="'Pagesynonym'::character varying")


class WikiVersion(Base):
    __tablename__ = 'ssismdl_wiki_versions'

    id = Column(BigInteger, primary_key=True)
    pageid = Column(BigInteger, nullable=False, index=True, server_default='0')
    content = Column(Text, nullable=False)
    contentformat = Column(String(20), nullable=False, server_default="'creole'::character varying")
    version = Column(Integer, nullable=False, server_default='0')
    timecreated = Column(BigInteger, nullable=False, server_default='0')
    userid = Column(BigInteger, nullable=False, server_default='0')


class Workshop(Base):
    __tablename__ = 'ssismdl_workshop'

    id = Column(BigInteger, primary_key=True)
    course = Column(BigInteger, nullable=False, index=True)
    name = Column(String(255), nullable=False, server_default="''::character varying")
    intro = Column(Text)
    introformat = Column(SmallInteger, nullable=False, server_default='0')
    instructauthors = Column(Text)
    instructauthorsformat = Column(SmallInteger, nullable=False, server_default='0')
    instructreviewers = Column(Text)
    instructreviewersformat = Column(SmallInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False)
    phase = Column(SmallInteger, server_default='0')
    useexamples = Column(SmallInteger, server_default='0')
    usepeerassessment = Column(SmallInteger, server_default='0')
    useselfassessment = Column(SmallInteger, server_default='0')
    grade = Column(Numeric(10, 5), server_default='80')
    gradinggrade = Column(Numeric(10, 5), server_default='20')
    strategy = Column(String(30), nullable=False, server_default="''::character varying")
    evaluation = Column(String(30), nullable=False, server_default="''::character varying")
    gradedecimals = Column(SmallInteger, server_default='0')
    nattachments = Column(SmallInteger, server_default='0')
    latesubmissions = Column(SmallInteger, server_default='0')
    maxbytes = Column(BigInteger, server_default='100000')
    examplesmode = Column(SmallInteger, server_default='0')
    submissionstart = Column(BigInteger, server_default='0')
    submissionend = Column(BigInteger, server_default='0')
    assessmentstart = Column(BigInteger, server_default='0')
    assessmentend = Column(BigInteger, server_default='0')
    phaseswitchassessment = Column(SmallInteger, nullable=False, server_default='0')
    conclusion = Column(Text)
    conclusionformat = Column(SmallInteger, nullable=False, server_default='1')
    overallfeedbackmode = Column(SmallInteger, server_default='1')
    overallfeedbackfiles = Column(SmallInteger, server_default='0')
    overallfeedbackmaxbytes = Column(BigInteger, server_default='100000')


class WorkshopAggregation(Base):
    __tablename__ = 'ssismdl_workshop_aggregations'
    __table_args__ = (
        Index('ssismdl_workaggr_woruse_uix', 'workshopid', 'userid'),
    )

    id = Column(BigInteger, primary_key=True)
    workshopid = Column(BigInteger, nullable=False, index=True)
    userid = Column(BigInteger, nullable=False, index=True)
    gradinggrade = Column(Numeric(10, 5))
    timegraded = Column(BigInteger)


class WorkshopAssessment(Base):
    __tablename__ = 'ssismdl_workshop_assessments'

    id = Column(BigInteger, primary_key=True)
    submissionid = Column(BigInteger, nullable=False, index=True)
    reviewerid = Column(BigInteger, nullable=False, index=True)
    weight = Column(BigInteger, nullable=False, server_default='1')
    timecreated = Column(BigInteger, server_default='0')
    timemodified = Column(BigInteger, server_default='0')
    grade = Column(Numeric(10, 5))
    gradinggrade = Column(Numeric(10, 5))
    gradinggradeover = Column(Numeric(10, 5))
    gradinggradeoverby = Column(BigInteger, index=True)
    feedbackauthor = Column(Text)
    feedbackauthorformat = Column(SmallInteger, server_default='0')
    feedbackreviewer = Column(Text)
    feedbackreviewerformat = Column(SmallInteger, server_default='0')
    feedbackauthorattachment = Column(SmallInteger, server_default='0')


class WorkshopAssessmentsOld(Base):
    __tablename__ = 'ssismdl_workshop_assessments_old'

    id = Column(BigInteger, primary_key=True)
    workshopid = Column(BigInteger, nullable=False, index=True, server_default='0')
    submissionid = Column(BigInteger, nullable=False, index=True, server_default='0')
    userid = Column(BigInteger, nullable=False, index=True, server_default='0')
    timecreated = Column(BigInteger, nullable=False, server_default='0')
    timegraded = Column(BigInteger, nullable=False, server_default='0')
    timeagreed = Column(BigInteger, nullable=False, server_default='0')
    grade = Column(Float(53), nullable=False, server_default='0')
    gradinggrade = Column(SmallInteger, nullable=False, server_default='0')
    teachergraded = Column(SmallInteger, nullable=False, server_default='0')
    mailed = Column(SmallInteger, nullable=False, index=True, server_default='0')
    resubmission = Column(SmallInteger, nullable=False, server_default='0')
    donotuse = Column(SmallInteger, nullable=False, server_default='0')
    generalcomment = Column(Text)
    teachercomment = Column(Text)
    newplugin = Column(String(28))
    newid = Column(BigInteger)


class WorkshopCommentsOld(Base):
    __tablename__ = 'ssismdl_workshop_comments_old'

    id = Column(BigInteger, primary_key=True)
    workshopid = Column(BigInteger, nullable=False, index=True, server_default='0')
    assessmentid = Column(BigInteger, nullable=False, index=True, server_default='0')
    userid = Column(BigInteger, nullable=False, index=True, server_default='0')
    timecreated = Column(BigInteger, nullable=False, server_default='0')
    mailed = Column(SmallInteger, nullable=False, index=True, server_default='0')
    comments = Column(Text, nullable=False)
    newplugin = Column(String(28))
    newid = Column(BigInteger)


class WorkshopElementsOld(Base):
    __tablename__ = 'ssismdl_workshop_elements_old'

    id = Column(BigInteger, primary_key=True)
    workshopid = Column(BigInteger, nullable=False, index=True, server_default='0')
    elementno = Column(SmallInteger, nullable=False, server_default='0')
    description = Column(Text, nullable=False)
    scale = Column(SmallInteger, nullable=False, server_default='0')
    maxscore = Column(SmallInteger, nullable=False, server_default='1')
    weight = Column(SmallInteger, nullable=False, server_default='11')
    stddev = Column(Float(53), nullable=False, server_default='0')
    totalassessments = Column(BigInteger, nullable=False, server_default='0')
    newplugin = Column(String(28))
    newid = Column(BigInteger)


class WorkshopGrade(Base):
    __tablename__ = 'ssismdl_workshop_grades'
    __table_args__ = (
        Index('ssismdl_workgrad_assstrdim_uix', 'assessmentid', 'strategy', 'dimensionid'),
    )

    id = Column(BigInteger, primary_key=True)
    assessmentid = Column(BigInteger, nullable=False, index=True)
    strategy = Column(String(30), nullable=False, server_default="''::character varying")
    dimensionid = Column(BigInteger, nullable=False)
    grade = Column(Numeric(10, 5), nullable=False)
    peercomment = Column(Text)
    peercommentformat = Column(SmallInteger, server_default='0')


class WorkshopGradesOld(Base):
    __tablename__ = 'ssismdl_workshop_grades_old'

    id = Column(BigInteger, primary_key=True)
    workshopid = Column(BigInteger, nullable=False, index=True, server_default='0')
    assessmentid = Column(BigInteger, nullable=False, index=True, server_default='0')
    elementno = Column(BigInteger, nullable=False, server_default='0')
    feedback = Column(Text, nullable=False)
    grade = Column(SmallInteger, nullable=False, server_default='0')
    newplugin = Column(String(28))
    newid = Column(BigInteger)


class WorkshopOld(Base):
    __tablename__ = 'ssismdl_workshop_old'

    id = Column(BigInteger, primary_key=True)
    course = Column(BigInteger, nullable=False, index=True, server_default='0')
    name = Column(String(255), nullable=False, server_default="''::character varying")
    description = Column(Text, nullable=False)
    wtype = Column(SmallInteger, nullable=False, server_default='0')
    nelements = Column(SmallInteger, nullable=False, server_default='1')
    nattachments = Column(SmallInteger, nullable=False, server_default='0')
    phase = Column(SmallInteger, nullable=False, server_default='0')
    format = Column(SmallInteger, nullable=False, server_default='0')
    gradingstrategy = Column(SmallInteger, nullable=False, server_default='1')
    resubmit = Column(SmallInteger, nullable=False, server_default='0')
    agreeassessments = Column(SmallInteger, nullable=False, server_default='0')
    hidegrades = Column(SmallInteger, nullable=False, server_default='0')
    anonymous = Column(SmallInteger, nullable=False, server_default='0')
    includeself = Column(SmallInteger, nullable=False, server_default='0')
    maxbytes = Column(BigInteger, nullable=False, server_default='100000')
    submissionstart = Column(BigInteger, nullable=False, server_default='0')
    assessmentstart = Column(BigInteger, nullable=False, server_default='0')
    submissionend = Column(BigInteger, nullable=False, server_default='0')
    assessmentend = Column(BigInteger, nullable=False, server_default='0')
    releasegrades = Column(BigInteger, nullable=False, server_default='0')
    grade = Column(SmallInteger, nullable=False, server_default='0')
    gradinggrade = Column(SmallInteger, nullable=False, server_default='0')
    ntassessments = Column(SmallInteger, nullable=False, server_default='0')
    assessmentcomps = Column(SmallInteger, nullable=False, server_default='2')
    nsassessments = Column(SmallInteger, nullable=False, server_default='0')
    overallocation = Column(SmallInteger, nullable=False, server_default='0')
    timemodified = Column(BigInteger, nullable=False, server_default='0')
    teacherweight = Column(SmallInteger, nullable=False, server_default='1')
    showleaguetable = Column(SmallInteger, nullable=False, server_default='0')
    usepassword = Column(SmallInteger, nullable=False, server_default='0')
    password = Column(String(32), nullable=False, server_default="''::character varying")
    newplugin = Column(String(28))
    newid = Column(BigInteger)


class WorkshopRubricsOld(Base):
    __tablename__ = 'ssismdl_workshop_rubrics_old'

    id = Column(BigInteger, primary_key=True)
    workshopid = Column(BigInteger, nullable=False, index=True, server_default='0')
    elementno = Column(BigInteger, nullable=False, server_default='0')
    rubricno = Column(SmallInteger, nullable=False, server_default='0')
    description = Column(Text, nullable=False)
    newplugin = Column(String(28))
    newid = Column(BigInteger)


class WorkshopStockcommentsOld(Base):
    __tablename__ = 'ssismdl_workshop_stockcomments_old'

    id = Column(BigInteger, primary_key=True)
    workshopid = Column(BigInteger, nullable=False, index=True, server_default='0')
    elementno = Column(BigInteger, nullable=False, server_default='0')
    comments = Column(Text, nullable=False)
    newplugin = Column(String(28))
    newid = Column(BigInteger)


class WorkshopSubmission(Base):
    __tablename__ = 'ssismdl_workshop_submissions'

    id = Column(BigInteger, primary_key=True)
    workshopid = Column(BigInteger, nullable=False, index=True)
    example = Column(SmallInteger, server_default='0')
    authorid = Column(BigInteger, nullable=False, index=True)
    timecreated = Column(BigInteger, nullable=False)
    timemodified = Column(BigInteger, nullable=False)
    title = Column(String(255), nullable=False, server_default="''::character varying")
    content = Column(Text)
    contentformat = Column(SmallInteger, nullable=False, server_default='0')
    contenttrust = Column(SmallInteger, nullable=False, server_default='0')
    attachment = Column(SmallInteger, server_default='0')
    grade = Column(Numeric(10, 5))
    gradeover = Column(Numeric(10, 5))
    gradeoverby = Column(BigInteger, index=True)
    feedbackauthor = Column(Text)
    feedbackauthorformat = Column(SmallInteger, server_default='0')
    timegraded = Column(BigInteger)
    published = Column(SmallInteger, server_default='0')
    late = Column(SmallInteger, nullable=False, server_default='0')


class WorkshopSubmissionsOld(Base):
    __tablename__ = 'ssismdl_workshop_submissions_old'

    id = Column(BigInteger, primary_key=True)
    workshopid = Column(BigInteger, nullable=False, index=True, server_default='0')
    userid = Column(BigInteger, nullable=False, index=True, server_default='0')
    title = Column(String(100), nullable=False, server_default="''::character varying")
    timecreated = Column(BigInteger, nullable=False, server_default='0')
    mailed = Column(SmallInteger, nullable=False, index=True, server_default='0')
    description = Column(Text, nullable=False)
    gradinggrade = Column(SmallInteger, nullable=False, server_default='0')
    finalgrade = Column(SmallInteger, nullable=False, server_default='0')
    late = Column(SmallInteger, nullable=False, server_default='0')
    nassessments = Column(BigInteger, nullable=False, server_default='0')
    newplugin = Column(String(28))
    newid = Column(BigInteger)


class WorkshopallocationScheduled(Base):
    __tablename__ = 'ssismdl_workshopallocation_scheduled'

    id = Column(BigInteger, primary_key=True)
    workshopid = Column(BigInteger, nullable=False, unique=True)
    enabled = Column(SmallInteger, nullable=False, server_default='0')
    submissionend = Column(BigInteger, nullable=False)
    timeallocated = Column(BigInteger)
    settings = Column(Text)
    resultstatus = Column(BigInteger)
    resultmessage = Column(String(1333))
    resultlog = Column(Text)


class WorkshopevalBestSetting(Base):
    __tablename__ = 'ssismdl_workshopeval_best_settings'

    id = Column(BigInteger, primary_key=True)
    workshopid = Column(BigInteger, nullable=False, unique=True)
    comparison = Column(SmallInteger, server_default='5')


class WorkshopformAccumulative(Base):
    __tablename__ = 'ssismdl_workshopform_accumulative'

    id = Column(BigInteger, primary_key=True)
    workshopid = Column(BigInteger, nullable=False, index=True)
    sort = Column(BigInteger, server_default='0')
    description = Column(Text)
    descriptionformat = Column(SmallInteger, server_default='0')
    grade = Column(BigInteger, nullable=False)
    weight = Column(Integer, server_default='1')


class WorkshopformComment(Base):
    __tablename__ = 'ssismdl_workshopform_comments'

    id = Column(BigInteger, primary_key=True)
    workshopid = Column(BigInteger, nullable=False, index=True)
    sort = Column(BigInteger, server_default='0')
    description = Column(Text)
    descriptionformat = Column(SmallInteger, server_default='0')


class WorkshopformNumerror(Base):
    __tablename__ = 'ssismdl_workshopform_numerrors'

    id = Column(BigInteger, primary_key=True)
    workshopid = Column(BigInteger, nullable=False, index=True)
    sort = Column(BigInteger, server_default='0')
    description = Column(Text)
    descriptionformat = Column(SmallInteger, server_default='0')
    descriptiontrust = Column(BigInteger)
    grade0 = Column(String(50))
    grade1 = Column(String(50))
    weight = Column(Integer, server_default='1')


class WorkshopformNumerrorsMap(Base):
    __tablename__ = 'ssismdl_workshopform_numerrors_map'
    __table_args__ = (
        Index('ssismdl_worknumemap_wornon_uix', 'workshopid', 'nonegative'),
    )

    id = Column(BigInteger, primary_key=True)
    workshopid = Column(BigInteger, nullable=False, index=True)
    nonegative = Column(BigInteger, nullable=False)
    grade = Column(Numeric(10, 5), nullable=False)


class WorkshopformRubric(Base):
    __tablename__ = 'ssismdl_workshopform_rubric'

    id = Column(BigInteger, primary_key=True)
    workshopid = Column(BigInteger, nullable=False, index=True)
    sort = Column(BigInteger, server_default='0')
    description = Column(Text)
    descriptionformat = Column(SmallInteger, server_default='0')


class WorkshopformRubricConfig(Base):
    __tablename__ = 'ssismdl_workshopform_rubric_config'

    id = Column(BigInteger, primary_key=True)
    workshopid = Column(BigInteger, nullable=False, unique=True)
    layout = Column(String(30), server_default="'list'::character varying")


class WorkshopformRubricLevel(Base):
    __tablename__ = 'ssismdl_workshopform_rubric_levels'

    id = Column(BigInteger, primary_key=True)
    dimensionid = Column(BigInteger, nullable=False, index=True)
    grade = Column(Numeric(10, 5), nullable=False)
    definition = Column(Text)
    definitionformat = Column(SmallInteger, server_default='0')


t_temp_student_email_info = Table(
    'temp_student_email_info', metadata,
    Column('list', String(255)),
    Column('email', String(255))
)


t_temp_to_be_informed = Table(
    'temp_to_be_informed', metadata,
    Column('idnumber', String(255)),
    Column('comment', String(255))
)
