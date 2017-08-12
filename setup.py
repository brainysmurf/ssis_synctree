from distutils.core import setup
setup(
    name = "ssis_synctree",
    packages = ['ssis_synctree', 'ssiscli'],
    version = "0.82",
    description = "A python framework that makes syncing between two applications straight-forward.",
    author = "Adam Morris",
    author_email = "amorris@mistermorris.com",
    install_requires = ['treelib', 'click', 'sqlalchemy', 'psycopg2', 'hues', 'ansi2html', 'pexpect'],
    lclassifiers = [
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        ],
    entry_points='''
        [console_scripts]
        psmdlsyncer=ssiscli.psmdlsyncer_cli:psmdlsyncer_entry
        ssis_synctree=ssiscli.cli_test:cli_test_entry
    ''',
    long_description = """\
This version requires Python 3.5 or later.
"""
)
