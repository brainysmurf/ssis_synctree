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
        if mp.email.endswith('@mail.ssis-suzhou.net') and mp.idnumber[-1] != 'P':
            before = moodle.get_user_from_username(mp.username)
            new_id = before.idnumber[:4] + ('P' * (1 if mp.idnumber[-1] == '0' else 2))
            already = moodle.get_user_from_idnumber(new_id)
            if already:
                print(f'Made a dup: {already.idnumber}: {already.id}, {already.email}')
                moodle.set_user_idnumber_from_username(already.username, already.idnumber + 'dup')

            moodle.set_user_idnumber_from_username(mp.username, new_id)
            print(before.id, before.email, before.username, before.idnumber, ' -> ', new_id)

                

    for mp in tree.moodle.staff:
        if not mp.idnumber.isdigit():
            before = moodle.get_user_from_username(mp.username)
            print(mp.username, mp.email, mp.idnumber)

            found = None
            objects = tree.autosend.staff.get_objects()
            while True:
                try:
                    user = next(objects)
                except StopIteration:
                    break
                if user.username == mp.username:
                    found = user
                    break
            if not found:
                print(f"Must do this one manually: {mp.email}") 
            else:
                moodle.set_user_idnumber_from_username(mp.username, user.idnumber)
                print(user.idnumber)