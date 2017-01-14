"""
TODO: New student workflow, emails to homeroom names
"""

import synctree, ssis_synctree
from synctree.settings import setup_settings
setup_settings(ssis_synctree)
from ssis_synctree.templates.moodle_template import MoodleTestTemplate as Testing
from synctree.templates import PrintTemplate as Output