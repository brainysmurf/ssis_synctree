from ssiscli.cli import CLIObject
import click

@click.group()
@click.option('--template', type=click.STRING, default=None, help="Define the template")
@click.option('--tutorial', is_flag=True, default=False, help="Enable debugging features")
@click.pass_context
def psmdlsyncer_entry(ctx, template, tutorial):
    """ PowerSchool -> Moodle syncer """
    ctx.obj = CLIObject()
    ctx.obj.template = template
    if tutorial:
        import gns;gns.set_debug(True)

@psmdlsyncer_entry.command('launch')
@click.option('--template', type=click.STRING, default=None, help="Importable string or 'Output' or 'Testing' ")
@click.pass_context
def psmdlsyncer_launch(ctx, template):
    ctx.invoke(psmdlsyncer_main, synctree_context='newcohorts', template=template)
    ctx.invoke(psmdlsyncer_main, synctree_context='newpeople', template=template)
    ctx.invoke(psmdlsyncer_main, synctree_context='newgroups', template=template)
    ctx.invoke(psmdlsyncer_main, synctree_context='enrollments', template=template)

@psmdlsyncer_entry.command('main')
@click.argument('synctree_context')
@click.option('--read_from_store', is_flag=True, default=False, help="Reads in")
@click.option('--write_to_store', is_flag=True, default=False, help="Writes to default path")
@click.option('--template', type=click.STRING, default=None, help="Importable string or 'Output' or 'Testing' ")
@click.option('--prepare_family', type=click.STRING, default=None, help="PSID for autosend and moodle side, variables in a and m")
@click.pass_obj
def psmdlsyncer_main(obj, synctree_context, read_from_store, write_to_store, template, prepare_family):
    path = '/tmp/ssis_synctree.json'

    # branches = ['autosend', 'moodle']
    # subbranches = ['students', 'staff', 'parents', 'parents_child_link', 'cohorts', 'courses', 'schedule', 'groups']

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

    from synctree.tree import SyncTree

    if read_from_store:
        s = SyncTree.from_file(path)
    else:
        s = SyncTree(
            branches,
            subbranches,
            "ssis_synctree.model.{branch}_model.{branch_title}{subbranch_title}",
            'ssis_synctree.importers.{branch}_importers.{branch_title}{subbranch_title}Importer',
        )

        # import:
        +s

        if write_to_store:
            s.store(path)

    if template is not None:
        # This is the line that makes things go
        # "take the differences between autosend and moodle, and change moodle according to template"
        if template_only_these or template_exclude_these:
            from synctree.templates import BlockedTemplateWrapper
            if template_only_these:
                blocked = BlockedTemplateWrapper(template, only_these=template_only_these)
            elif template_exclude_these:
                blocked = BlockedTemplateWrapper(template, exclude_these=template_exclude_these)
            (s.autosend > s.moodle) | blocked._template
        else:
            (s.autosend > s.moodle) | template

    else:
        if prepare_family:
            # TODO: Make this a family thing rather than just a student
            parent = prepare_family + '0'
            ap, mp = s.autosend.parents.get(parent), s.moodle.parents.get(parent)
            
            a, m = s.autosend.students.get(prepare_student), s.moodle.students.get(prepare_student)

    # autosend = s.autosend
    # moodle = s.moodle

    # from IPython import embed;embed()