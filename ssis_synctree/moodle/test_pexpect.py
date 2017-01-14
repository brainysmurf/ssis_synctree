from ssis_synctree.moodle.php import PHP

if __name__ == "__main__":
    p = PHP()
    here=""
    while here.strip() != "quit":
        a = p.command(here.strip())
        print(a)