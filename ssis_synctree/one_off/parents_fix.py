from synctree.tree import SyncTree
from ssis_synctree.templates.moodle_template import MoodleDB
from ssis_synctree.moodle.php import PHP


if __name__ == "__main__":


    # Get all the family IDs

    branches = [b for b in "autosend".split(" ")]
    subbranches = [sb for sb in "students staff parents".split(" ")]

    tree = SyncTree(branches, subbranches,
        "ssis_synctree.model.{branch}_model.{branch_title}{subbranch_title}",
        'ssis_synctree.importers.{branch}_importers.{branch_title}{subbranch_title}Importer',
    )

    +tree

    family_ids = set([])
    for student in tree.autosend.students:
        family_ids.add(student._family_id)

    moodle = MoodleDB()
    php = PHP()

    for family_id in family_ids:

        family_idP = family_id + 'P'
        family_idPP = family_id + 'PP'
        p1 = moodle.get_user_from_idnumber(family_idP)
        p2 = moodle.get_user_from_idnumber(family_idPP)

        staff_id0 = family_id + '0'
        staff_id1 = family_id + '1'

        if tree.autosend.staff.get(staff_id0):
            s0 = moodle.get_user_from_idnumber(staff_id0)
        else:
            s0 = None
        if tree.autosend.staff.get(staff_id1):
            try:
                s1 = moodle.get_user_from_idnumber(staff_id1)
            except AttributeError:
                print("More than one: {}".format(staff_id1))
                continue
        else:
            s1 = None

        # checks
        if p1 and ('parentsALL' not in moodle.get_cohorts_for_user(p1.idnumber)):
            for cohort in moodle.get_cohorts_for_user(p1.idnumber):
                print(php.remove_user_from_cohort(p1.idnumber, cohort))
            print('parent1', p1.idnumber, 'not in parentsALL')
            print(php.add_user_to_cohort(p1.idnumber, 'parentsALL'))
        if p2 and ('parentsALL' not in moodle.get_cohorts_for_user(p2.idnumber)):
            for cohort in moodle.get_cohorts_for_user(p2.idnumber):
                print(php.remove_user_from_cohort(p2.idnumber, cohort))
            print('parent2', p2.idnumber, 'not in parentsALL')
            print(php.add_user_to_cohort(p2.idnumber, 'parentsALL'))
        if s0 and ('teachersALL' not in moodle.get_cohorts_for_user(s0.idnumber)):
            for cohort in moodle.get_cohorts_for_user(s0.idnumber):
                print(php.remove_user_from_cohort(s0.idnumber, cohort))
            print('staff0', s0.idnumber, 'not in teachersALL')
            print(php.add_user_to_cohort(s0.idnumber, 'teachersALL'))
        if s1 and ('teachersALL' not in moodle.get_cohorts_for_user(s1.idnumber)):
            for cohort in moodle.get_cohorts_for_user(s1.idnumber):
                print(php.remove_user_from_cohort(s1.idnumber, cohort))
            print('staff1', s1.idnumber, 'not in teachersALL')
            print(php.add_user_to_cohort(s1.idnumber, 'teachersALL'))

        if p1 and s0:
            moodle.set_username_from_idnumber(p1.idnumber, p1.idnumber[:4] + 'P')


    tree2 = SyncTree(branches, subbranches,
        "ssis_synctree.model.{branch}_model.{branch_title}{subbranch_title}",
        'ssis_synctree.importers.{branch}_importers.{branch_title}{subbranch_title}Importer',
    )

    +tree2

    for staff in tree2.autosend.staff:
        if not staff.idnumber.isdigit():
            print('staff has wrong idnumber!', staff.idnumber, staff.username)
            exit()

    for family_id in family_ids:
        family_idP = family_id + 'P'
        family_idPP = family_id + 'PP'
        staff_id0 = family_id + '0'
        staff_id1 = family_id + '1'

        fp = moodle.get_user_from_idnumber(family_idP)
        fpp = moodle.get_user_from_idnumber(family_idPP)
        s0 = moodle.get_user_from_idnumber(staff_id0)
        try:
            s1 = moodle.get_user_from_idnumber(staff_id1)
        except AttributeError:
            print("More than one", staff_id1)
            continue
        family_id0username = moodle.get_user_from_username(family_id + '0')
        family_id1username = moodle.get_user_from_username(family_id + '1')

        if fp and family_id0username:
            if s0 and s1: 
                if not tree2.autosend.staff.get(staff_id0) and not tree2.autosend.staff.get(staff_id1):
                    # three parents, not a staff member
                    # delete the fp, not needed
                    moodle.set_username_from_idnumber(family_idP, 'zz' + family_idP+'delete')
                    moodle.set_idnumber_from_idnumber(family_idP, 'zz' + family_idP+'delete')

                    # update the other ones
                    moodle.set_idnumber_from_idnumber(s0.idnumber, family_id + 'P')
                    moodle.set_idnumber_from_idnumber(s1.idnumber, family_id + 'PP')
                else:
                    print("Manually for", family_id)
                    result = input()
                    if result == 'e':
                        from IPython import embed;embed()
                        continue
                    elif result == 'x':
                        exit()



