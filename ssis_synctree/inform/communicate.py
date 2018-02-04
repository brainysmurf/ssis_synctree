class Communicate:

    def __init__(self):

        import ssis_synctree_settings
        import configparser

        self.host = ssis_synctree_settings.get("COMMUNICATE", 'smtp')

        self.sender = ssis_synctree_settings.get('COMMUNICATE', 'receivers')
        self.receivers = ssis_synctree_settings.get('COMMUNICATE', 'receivers').split(',')

        self.message = """
From: <""" + self.sender + """>
To: <""" + "><".join(self.receivers) + """>
MIME-Version: 1.0
Content-type: text/html
Subject: Test

"""
        
    def compose(self, html):
        self.message += html

    def send(self):
        import smtplib
        server = smtplib.SMTP(self.host)
        result = server.sendmail(self.sender, self.receivers, self.message)
        if result is not {}:
            print(result)


if __name__ == "__main__":

    import synctree, ssis_synctree
    from synctree.settings import setup_settings
    setup_settings(ssis_synctree)

    com = Communicate()
    com.compose('hi')
    com.send()