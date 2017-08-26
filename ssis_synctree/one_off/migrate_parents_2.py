from synctree.tree import SyncTree
from ssis_synctree.templates.moodle_template import MoodleDB


if __name__ == "__main__":

    moodle = MoodleDB()

    branches = [b for b in "autosend moodle".split(" ")]
    subbranches = [sb for sb in "students staff parents".split(" ")]

    tree = SyncTree(branches, subbranches,
        "ssis_synctree.model.{branch}_model.{branch_title}{subbranch_title}",
        'ssis_synctree.importers.{branch}_importers.{branch_title}{subbranch_title}Importer',
    )

    +tree

    for mp in tree.moodle.parents:
        if mp.username[-1] == 'P':
            family_id = mp.idnumber[:4]
            try:
                existing = moodle.get_user_from_idnumber(family_id + '0')
            except AttributeError:
                print(f"More than one of these already: {family_id}0")
            if existing:
                print(f'Relegating: {existing.idnumber}: {existing.id}, {existing.email}')
                moodle.set_user_idnumber_from_username(mp.username, 'zz' + existing.idnumber + 'delete')
                moodle.set_user_idnumber_from_username(existing.username, family_id + 'P')
                moodle.change_user_username(mp.username, 'zz' + mp.username + 'delete')
                moodle.change_user_username(existing.username, family_id + '0')
            else:
                print(f"Simple change {existing.idnumber}".format())
                moodle.change_user_username(mp.username, family_id + '0')
