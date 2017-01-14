"""
TODO: Delete this file

from cli.cli import CLIObject
import click
from collections import defaultdict

@click.group()
@click.pass_context
def cli_test_entry(ctx):

    ctx.obj = CLIObject()


@cli_test_entry.command('database')
@click.pass_obj
def test_database(obj):

	from ssis_synctree.importers.moodle_importers import MoodleImporter
	moodle = MoodleImporter('', '','')

	idnumbers = defaultdict(list)

	for item in moodle.get_teaching_learning_courses():

		idnumbers[item.idnumber].append(item)

	from IPython import embed;embed()
"""