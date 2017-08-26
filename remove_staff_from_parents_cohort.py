from synctree.tree import SyncTree
# from ssis_synctree.templates.moodle_template import MoodleDB
from ssis_synctree.moodle.php import PHP


if __name__ == "__main__":

    moodle = MoodleDB()
    php = PHP()

    branches = [b for b in "autosend moodle".split(" ")]
    subbranches = [sb for sb in "students staff parents".split(" ")]

    tree = SyncTree(branches, subbranches,
        "ssis_synctree.model.{branch}_model.{branch_title}{subbranch_title}",
        'ssis_synctree.importers.{branch}_importers.{branch_title}{subbranch_title}Importer',
    )

    +tree

    for mp in tree.moodle.staff:
        if mp.idnumber.endswith('P'):
            php.remove_user_from_cohort(mp.idnumber, 'teachersALL')
            print(f'Removed {mp.idnumber} from teachersALL')
