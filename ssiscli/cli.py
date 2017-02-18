from synctree.settings import setup_settings
import click


class CLIObject:
    """
    Interface with datastoresync with the requisite info
    """
    def __init__(self):
        import ssis_synctree          # import it here to get the desired behaviour, otherwise it is a click.Group?       
                                    # not sure why, but must be something to do with incompatibility with the click package
                                    # since removing 'import click' statement above fixes it too
        setup_settings(ssis_synctree)

    def init_synctreetest(self, template, readfromdisk, writetodisk):
        pass

    def init_pspfsyncer(self):
        self.source = self.autosend_tree
        self.dest = self.postfix

