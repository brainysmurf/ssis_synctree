from synctree.tree import SyncTree
from ssis_synctree.templates.moodle_template import MoodleDB
from ssis_synctree.moodle.php import PHP
from ssis_synctree.moodle.MoodleDBSchema import *
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

import csv

def output_current_homework(moodle):
    with moodle.db_session() as session:
        statement = session.query(Group)
        groups = statement.all()

        for group in groups:
            if (group.idnumber and len(group.idnumber.split('-'))==4):
                print(group.idnumber)
                homeworks = session.query(BlockHomework).filter(BlockHomework.groupid == group.id)
                for homework in homeworks.all():
                    print(homework)

if __name__ == "__main__":

    moodle = MoodleDB()
    #output_current_homework(moodle)

    old_groups = {}
    with open('group_ids_old.txt') as old_file:
        reader = csv.reader(old_file, delimiter=" ")
        for row in reader:
            old_groups[" ".join(row[1:])] = row[0]

    new_groups = {}
    with moodle.db_session() as session:
        statement = session.query(Group)
        groups = statement.all()

        for group in groups:
            if (group.idnumber and len(group.idnumber.split('-'))==4):
                new_groups[group.idnumber] = group.id

    with moodle.db_session() as session:
        for groupname, current_groupid in new_groups.items():
            old_groupid = old_groups.get(groupname)
            if old_groupid is None:
                print("Nope!: {}".format(groupname))
                continue
            session.query(Group).filter(Group.id==current_groupid).update({'id': old_groupid})



