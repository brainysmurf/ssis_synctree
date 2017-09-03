from synctree.tree import SyncTree
from ssis_synctree.templates.moodle_template import MoodleDB
from ssis_synctree.moodle.php import PHP
from ssis_synctree.moodle.MoodleDBSchema import *
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

if __name__ == "__main__":


    # Get all the family IDs

    branches = [b for b in "autosend".split(" ")]
    subbranches = [sb for sb in "students staff parents".split(" ")]

    tree = SyncTree(branches, subbranches,
        "ssis_synctree.model.{branch}_model.{branch_title}{subbranch_title}",
        'ssis_synctree.importers.{branch}_importers.{branch_title}{subbranch_title}Importer',
    )

    +tree

    student_idnumbers = tree.autosend.students.idnumbers
    parent_idnumbers = tree.autosend.parents.idnumbers
    staff_idnumbers = tree.autosend.staff.idnumbers

    moodle = MoodleDB()
    php = PHP()


    with moodle.db_session() as session:
        statement = session.query(User).filter(User.idnumber != '', User.deleted == 0)
        users = statement.all()

        for user in users:
            if not user.idnumber in student_idnumbers and not user.idnumber in parent_idnumbers and not user.idnumber in staff_idnumbers:
                print(user.idnumber, user.username, user.department)
                user.department = 'left'

                family_id = user.idnumber[:4]
                for parent_idnumber in [family_id + 'P', family_id + 'PP']:
                    if parent_idnumber in parent_idnumbers:
                        continue
                    try:
                        parent = session.query(User).filter(User.idnumber == parent_idnumber).one()
                    except NoResultFound:
                        continue
                    parent.department = 'left'
