from synctree.tree import SyncTree
from synctree.templates import BlockedTemplateWrapper
from ssiscli.cli import CLIObject
import click
import hues
from ansi2html import Ansi2HTMLConverter
from collections import defaultdict


@click.group()
@click.option('--template', type=click.STRING, default=None, help="Define the template")
@click.option('--mock', is_flag=True, default=False, help="Enables dry run feature")
@click.option('--tutorial', is_flag=True, default=False, help="Enable debugging features")
@click.pass_context
def psmdlsyncer_entry(ctx, template, mock, tutorial):
    """ PowerSchool -> Moodle syncer """
    ctx.obj = CLIObject()
    ctx.obj.template = template
    ctx.obj.mock = mock
    if tutorial:
        import gns;gns.set_debug(True)


def synctree_contexts():
    return ['newcohorts', 'newpeople', 'newprofiles', 'newgroups', 'newenrollments']


@psmdlsyncer_entry.command('run')
@click.option('--template', type=click.STRING, default=None, help="Importable string or 'Output' or 'Testing' ")
@click.option('--context', type=click.STRING, default=None, help="Context which is defined in settings.ini")
@click.pass_context
def psmdlsyncer_run(ctx, template, context):
    if context is None:
        contexts = synctree_contexts()
    else:
        contexts = [context]
    for synctree_context in contexts:
        ctx.invoke(psmdlsyncer_main, synctree_context=synctree_context, template=template)


class MyAnsi2HTMLConverter(Ansi2HTMLConverter):
    """
    Use settings and patterns effective for an html email
    """
    def __init__(self, inline=True, dark_bg=False):
        super().__init__(inline=inline, dark_bg=dark_bg)

    def convert(self, ansi: list, full=False):
        ret = super().convert("\n".join(ansi), full=full)
        ret = ret.replace('<span style="', '<span style="padding-left:5px; padding-right: 5px;').\
            replace('#aa5500', '#f1cf11').\
            replace('\n', '<br />')
        return ret


@psmdlsyncer_entry.command('launch')
@click.pass_context
def psmdlsyncer_launch(ctx):
    """
    Runs and executes inform methods
    """
    from ssis_synctree.inform.communicate import Communicate

    template = 'ssis_synctree.templates.moodle_template.MoodleFullTemplate'
    for synctree_context in synctree_contexts():
        # Cycle through them, and clear them to save memory
        ctx.invoke(psmdlsyncer_main, synctree_context=synctree_context, template=template)


    # Import the template which will give us the reporter logs
    from synctree.utils import class_string_to_class
    template_inst = class_string_to_class(template)()
    output = []
    reporter_log = template_inst.reporter._log

    shared_idnumber_subbranches = ['students', 'parents', 'teachers', 'parents_child_link', 'enrollments']
    unique_idnumber_subbranches = ['cohorts courses groups']

    info_by_family_ids = defaultdict(lambda : defaultdict(list))
    for subbranch in shared_idnumber_subbranches:
        for idnumber, values in reporter_log[subbranch].items():
            family_id = idnumber[:4]
            info_by_family_ids[family_id][idnumber].extend(values)

    for family_id in sorted(info_by_family_ids):
        output.append('\n\n' + hues.huestr(f"{family_id}x ").white.bg_magenta.bold.colorized)
        for idnumber, values in info_by_family_ids[family_id].items():
            if values:
                _, action, _ = values[0]
                if hasattr(action, 'name'):
                    output.append(hues.huestr(f"\n {action.obj.name} ({action.obj.idnumber}) ").magenta.bold.colorized)
                else:
                    output.append(hues.huestr(f"\n {action.obj.idnumber} ").magenta.bold.colorized)
                output.extend([v[0] for v in values])

    for subbranch in unique_idnumber_subbranches:
        if reporter_log[subbranch]:
            output.append('\n\n' + hues.huestr(f" {subbranch.upper()} ").white.bg_magenta.bold.colorized)
        for idnumber, values in reporter_log[subbranch].items():
            if values:
                _, action, _ = values[0]
                output.append(hues.huestr(f"\n {action.obj.name} ({action.obj.idnumber}) ").magenta.bold.colorized)
                output.extend([v[0] for v in values])

    converter = MyAnsi2HTMLConverter(inline=True, dark_bg=False)
    converted = converter.convert(output)

    with open('/tmp/html.html', 'w') as file_:
        file_.write(converted)

    if ctx.obj.mock:
        Communicate('sync_mocked', {"output": converted})
    else:
        Communicate('sync_succeeded', {"output": converted})


@psmdlsyncer_entry.command('inspect')
@click.pass_context
def psmdlsyncer_inspect(ctx):
    tree = ctx.invoke(psmdlsyncer_main, synctree_context='none', template=None)
    p = tree.autosend
    m = tree.moodle

    def firstname(firstname):
        return lookup(f'firstname:{firstname}')
    def lastname(lastname):
        return lookup(f'lastname:{lastname}')
    def grade(grade):
        return lookup(f'_grade:{grade}')
    def homeroom(homeroom):
        return lookup(f'homeroom:{homeroom}')

    def lookup(bywhat, subbranch=None):
        ret = []
        if subbranch is None:
            subbranch = p.students
        objects = subbranch.find_all(bywhat)
        if objects is None:
            print("Not any of those objects")
            return None
        if len(objects) == 1:
            tree(objects[0].idnumber)
            return [objects[0]]
        else:
            for obj in objects:
                ret.append(obj)
                print(obj._description)
        return ret

    def course(what, subbranch=None):
        ret = []
        courses = lookup(f'idnumber:{what}', subbranch=subbranch or p.courses)
        if courses is None:
            print("No courses found")
            return
        if len(courses):
            print(courses[0]._description)
        else:
            for course in courses:
                ret.append(course)
                print(course._description)
        return ret

    def family(five):
        for subbranch in [(p.staff, p.parents, p.students), (m.staff, m.parents, m.students)]:
            print("====STAFF=====")
            for i in range(2):
                print(subbranch[0].find_all(f'idnumber:{five}{i}'))
            print("====PARENTS===")
            for i in range(2):
                print(subbranch[1].find_all(f'idnumber:{five}{("P" * (i+1))}'))
            print('====STUDENTS==')
            for i in range(2, 10):
                print(subbranch[2].find_all(f'idnumber:{five}{i}'))

    def in_cohorts(idnumber, subbranch=tree.autosend.cohorts):
        ret = []
        for cohort in subbranch.idnumbers:
            if idnumber in subbranch.get(cohort).members:
                ret.append(cohort)
        return ret

    def compare_cohorts(idnumber):
        print("AUTOSEND")
        print(', '.join(sorted(in_cohorts(idnumber, subbranch=tree.autosend.cohorts))))
        print("MOODLE")
        print(', '.join(sorted(in_cohorts(idnumber, subbranch=tree.moodle.cohorts))))

    def random_stu_idnumber(grade=None):
        import random

        if grade is None:
            idnumbers = tree.autosend.students.idnumbers
            return random.choice(list(idnumbers))
        else:
            idnumbers = []
            for student in tree.autosend.students.get_objects():
                if str(student._grade) == str(grade):
                    idnumbers.append(student.idnumber)
            return random.choice(idnumbers)

    compare = lambda idnumber: tree(idnumber)

    from IPython import embed;embed()

@psmdlsyncer_entry.command('manual_context')
@click.argument('branches', type=click.STRING)
@click.argument('subbranches', type=click.STRING)
@click.option('--onlythese', type=click.STRING, default=None, help="")
@click.option('--excludethese', type=click.STRING, default=None, help="")
@click.option('--template', type=click.STRING, default='ssis_synctree.templates.moodle_template.MoodleFullTemplate', help="Importable string, default is MoodleFullTemplate")
@click.option('--inspect', is_flag=True, default=False, help="Use IPython")
@click.pass_obj
def psmdlsyncer_manual_context(obj, branches, subbranches, onlythese, excludethese, template, inspect):
    """
    TODO: Unite this and main below
    """
    import ssis_synctree_settings

    # convert data info
    template_only_these = onlythese
    template_exclude_these = excludethese
    branches = [br.strip(' ') for br in branches.split(" ")]
    subbranches = [sbr.strip(' ') for sbr in subbranches.split(" ")]
    
    tree = SyncTree(
        branches,
        subbranches,
        "ssis_synctree.model.{branch}_model.{branch_title}{subbranch_title}",
        'ssis_synctree.importers.{branch}_importers.{branch_title}{subbranch_title}Importer',
    )

    # import:
    +tree
    hues.log(hues.huestr(f"Import complete").magenta.bold.colorized)

    if template is not None:
        # This is the line that makes things go
        # "take the differences between autosend and moodle, and change moodle according to template"
        if template_only_these or template_exclude_these:
            if template == "Output":
                raise TypeError('Cannot mock using template "Output"; need to use ssis_synctree template')
            if template_only_these:
                blocked = BlockedTemplateWrapper(template, mock=obj.mock, only_these=template_only_these)
            elif template_exclude_these:
                blocked = BlockedTemplateWrapper(template, mock=obj.mock, exclude_these=template_exclude_these)
            (tree.autosend > tree.moodle) | blocked._template
        else:
            if obj.mock:
                # For mocking, we have to initilize the template in order to use the class variable 
                # which will use DyanmicMockIf
                from synctree.utils import class_string_to_class
                template_class = class_string_to_class(template)
                template_class._mock = True
                template = template_class()
            (tree.autosend > tree.moodle) | template

    if inspect:
        from IPython import embed;embed()

    return tree


@psmdlsyncer_entry.command('main')
@click.argument('synctree_context')
@click.option('--read_from_store', is_flag=True, default=False, help="Reads in")
@click.option('--write_to_store', is_flag=True, default=False, help="Writes to default path")
@click.option('--template', type=click.STRING, default='ssis_synctree.templates.moodle_template.MoodleFullTemplate', help="Importable string, default is MoodleFullTemplate")
@click.option('--inspect', is_flag=True, default=False, help="Use IPython")
@click.option('--clear', is_flag=True, default=False, help="Clear at the end of use, doesn't return either")
@click.pass_obj
def psmdlsyncer_main(obj, synctree_context, read_from_store, write_to_store, template, inspect, clear):
    path = '/tmp/ssis_synctree.json'

    import ssis_synctree_settings
    import configparser

    context_key = f"CONTEXT_{synctree_context.upper()}"

    try:
        branches = ssis_synctree_settings.get(context_key, 'branches')
        subbranches = ssis_synctree_settings.get(context_key, 'subbranches')
    except configparser.NoSectionError:
        print(f"No context available called {synctree_context}, make sure settings.ini file has CONTEXT_{synctree_context.upper()} section")
    except configparser.NoOptionError:
        print(f"CONTEXT_{synctree_context.upper()} section needs to have both 'branches' and 'subbranches' options")

    try:
        template_only_these = ssis_synctree_settings.get(context_key, 'only_these')
    except configparser.NoOptionError:
        template_only_these = None # not an error, simply hasn't been provided

    try:
        template_exclude_these = ssis_synctree_settings.get(context_key, 'exclude_these')
    except configparser.NoOptionError:
        template_exclude_these = None # not an error, simply hasn't been provided
    if template_only_these and template_exclude_these:
        click.echo( "Defined too many options" ); exit()

    branches = [br.strip(' ') for br in branches.split(" ")]
    subbranches = [sbr.strip(' ') for sbr in subbranches.split(" ")]
    
    hues.log(hues.huestr(f"psmdlsyncer: {synctree_context} ").white.bg_magenta.bold.colorized)

    if read_from_store:
        tree = SyncTree.from_file(path)
    else:
        tree = SyncTree(
            branches,
            subbranches,
            "ssis_synctree.model.{branch}_model.{branch_title}{subbranch_title}",
            'ssis_synctree.importers.{branch}_importers.{branch_title}{subbranch_title}Importer',
        )

        # import:
        +tree
        hues.log(hues.huestr(f"Import complete").magenta.bold.colorized)

        if write_to_store:
            tree.store(path)

    if template is not None:
        # This is the line that makes things go
        # "take the differences between autosend and moodle, and change moodle according to template"
        if template_only_these or template_exclude_these:
            if template == "Output":
                raise TypeError('Cannot mock using template "Output"; need to use ssis_synctree template')
            if template_only_these:
                blocked = BlockedTemplateWrapper(template, mock=obj.mock, only_these=template_only_these)
            elif template_exclude_these:
                blocked = BlockedTemplateWrapper(template, mock=obj.mock, exclude_these=template_exclude_these)
            (tree.autosend > tree.moodle) | blocked._template
        else:
            if obj.mock:
                # For mocking, we have to initilize the template in order to use the class variable 
                # which will use DyanmicMockIf
                from synctree.utils import class_string_to_class
                template_class = class_string_to_class(template)
                template_class._mock = True
                template = template_class()
            (tree.autosend > tree.moodle) | template

    if inspect:
        from IPython import embed;embed()

    if clear:
        tree.clear()
        return None

    return tree


@psmdlsyncer_entry.command('test_emailer')
@click.pass_obj
def psmdlsyncer_testemailer(obj):
    # import ssis_synctree
    # from synctree.settings import setup_settings
    # setup_settings(ssis_synctree)

    from ssis_synctree.inform.communicate import Communicate

    Communicate()

