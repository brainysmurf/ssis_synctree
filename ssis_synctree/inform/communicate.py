"""

"""
from ssis_synctree.inform.this_emailer import Email, read_in_templates


class Communicate:
    """ Handler """

    def __init__(self, which, fields=None):

        import ssis_synctree_settings

        self.email_templates = ssis_synctree_settings.get("COMMUNICATE", 'templates')
        inform_templates = read_in_templates(f"{self.email_templates}/{which}")
        self.host = ssis_synctree_settings.get("COMMUNICATE", 'smtp')
        self.sender = ssis_synctree_settings.get("COMMUNICATE", 'sender').split(',')
        self.receivers = ssis_synctree_settings.get("COMMUNICATE", 'receivers').split(',')
        email = Email(self.host)
        email.define_sender(self.sender[0], self.sender[1])
        email.use_templates(inform_templates)
        if which == 'sync_failed':
            email.make_subject("Sync did NOT execute due to error")
        else:
            email.make_subject("Sync result for today")
        for receiver in self.receivers:
            email.add_to(receiver)
        email.add_bcc('lcssisadmin@student.ssis-suzhou.net')
        if fields is not None:
            email.define_fields(fields)
        email.send()
