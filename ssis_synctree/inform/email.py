import email.utils as _email
from email.header import Header
from email.generator import Generator
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

try:
    import html2text
    # Used for the plaintext portion of the email
except ImportError:
    # If html2text isn't available (boo) use a simple html tag extractor using a (very basic) regular expression
    # Better yet, install html2text (http://www.aaronsw.com/2002/html2text/)
    import re
    class html2text:
        html2text = lambda html: re.sub(r'<.*?>', '', html)
import smtplib
from smtplib import SMTPServerDisconnected

def read_in_templates(path, email_object=None):
    """
    Read in files and use them as templates
    Provided externally to Email class to avoid large amounts of disk use
    If attach is passed, it should be an Email object
    """
    import os
    templates = {}

    for fle in os.listdir(path):
        with open(os.path.join(path, fle)) as _f:
            raw = "\n".join(_f.readlines())
            templates[fle] = raw

    if email_object:
        email_object.use_templates(templates)
    else:
        return templates

class Recipient:

    def __init__(self, email="", name="", lang="en", **kwargs):
        if not email or not '@' in email:
            self.email = ""
            email = "noemailprovided@example.org"
        if not name:
            self.name = email[:email.index('@')]
        else:
            self.name = name
        self.email = email
        self.lang = lang
        self.envelope = _email.formataddr( (name, email) )
        self.is_bcc, self.is_cc = (False, False)
        self.set_up_fields(kwargs)

    def __str__(self):
        return self.envelope

    def set_up_fields(self, fields):
        """
        Sets up fields, which are things that can be used to format the template
        And, for special keys, sets the object itself to those values
        """
        self.fields = {
            'name': self.name,
            'email': self.email
            }
        for key in fields.keys():
            # special keys first, not to be used in the template
            if key.upper() == 'CC':
                self.is_cc = fields[key]
            elif key.upper() == 'BCC':
                self.is_bcc = fields[key]
            else:
                self.fields[key] = fields[key]

    def __call__(self):
        return self.envelope

    def __repr__(self):
        return "{}: {}".format(self.name, self.email)

class RecipientList:

    def __init__(self):
        self.lst = []

    def __str__(self):
        result = ""
        for r in self:
            result += str(r) + '\n'
        return result

    def add(self, item):
        """
        Adds recipients, won't add if email address is already present 
        """
        if item.email and item.email not in [i.email for i in self.lst]:
            self.lst.append(item)
        else:
            print("WARN: Recipient not added because a recipient with that email address already exists: {}", item)

    def factory(self, email="", name="", **kwargs):
        return Recipient(email, name, **kwargs)

    def __call__(self):
        return self.lst

    def __iter__(self):
        self.item = 0
        return self

    def __next__(self):
        if self.item < len(self.lst):
            r = self.lst[self.item]
            self.item += 1
            return r
        else:
            raise StopIteration

class Email:

    def __init__(self, domain):
        """
        domain CAN BE localhost
        """
        self.sent = False
        self.domain = domain
        self.html = ""
        self.htmls = {}
        self.lang = ["en"]
        self.fields = {}
        self.clear_recipients()
        self.define_seperator("\n\n")

    def __str__(self):
        result = ""
        result += "------"
        result += str(self.recipients)
        result += str(self.htmls)
        result += "------"
        return result

    def clear_recipients(self):
        self.recipients = RecipientList()

    def define_seperator(self, sep):
        self.sep = sep

    def use_templates(self, templates):
        """
        templates should be a dictionary of languages with html text as their value
        """
        self.htmls = templates
        
    def make_recipient(self, email="", name="", **kwargs):
        return self.recipients.factory(email, name, **kwargs)

    def add_recipient(self, email="", name="", **kwargs):
        self.recipients.add(self.make_recipient(email, name, **kwargs))

    def add_to(self, email="", name=""):
        self.add_recipient(email, name)

    def add_cc(self, email="", name=""):
        self.add_recipient(email, name, CC=True)

    def add_bcc(self, email="", name=""):
        self.add_recipient(email, name, BCC=True)

    def make_subject(self, sbjct):
        self.subject = sbjct

    def define_subject(self, sbjct):
        self.make_subject(sbjct)

    def define_content(self, html):
        """
        Use for simple cases
        """
        self.html_template(html, lang="en")
        self.add_language("en")

    def html_template(self, html, lang="en"):
        self.htmls[lang] = html

    def add_language(self, lang):
        if not lang in self.lang:
            self.lang.append(lang)

    def remove_langauge(self, lang):
        if not lang in self.lang:
            return
        index = self.lang.index(lang)
        self.lang.pop(index)

    def get_template(self):
        """
        Returns text of the templates available with the required languages
        Languages are set in add_language
        """
        return self.sep.join([self.htmls[html] for html in self.lang]).format(**self.fields)

    def define_sender(self, email="", name=""):
        """
        Who the email should be sent from
        """
        if not email:
            return
        if not name:
            name = False
        self.from_who = _email.formataddr( (name, email) )

    def define_field(self, key, value):
        self.fields[key] = value

    def define_fields(self, dictionary):
        for key, value in dictionary.items():
            self.define_field(key, value)

    def send(self):
        template = self.get_template()
        if not template:
            raise NotImplemented
        msg = MIMEMultipart('alternative')

        # Headers
        msg['Subject'] = Header(self.subject.encode('utf-8'), 'UTF-8').encode()
        msg['From'] = self.from_who

        for recipient in self.recipients:
            if recipient.is_bcc:
                hdr = 'BCC'
            elif recipient.is_cc:
                hdr = 'CC'
            else:
                hdr = 'To'
            msg[hdr] = recipient.envelope

        # Make the body of the message the same for both plain text and html.
        plaintext = html2text.html2text(template)

        # Record the MIME types of both parts - text/plain and text/html.
        part1 = MIMEText(plaintext.encode('utf-8'), 'plain', 'utf-8')
        part2 = MIMEText(template.encode('utf-8'), 'html', 'utf-8')

        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.
        msg.attach(part1)
        msg.attach(part2)

        # Check if localhost is specified:
        if self.domain == 'localhost' or not self.domain:
            print(plaintext.encode('utf-8'))
            return

        # Send the message via local SMTP server.
    
        # sendmail function takes 3 arguments: sender's address, recipient's address
        # and message to send - here it is sent as one string.
        # Need to remove unicode characters so that the string converts correctly
        #regexp = re.compile('[^\x09\x0A\x0D\x20-\x7F]')
        #msg_as_string = regexp.sub('', msg.as_string())
        try:
            s = smtplib.SMTP(self.domain)
        except smtplib.socket.error:
            #TODO: Email admin when in production
            print("Not an email server, did not send email from {} to {} with content:\n{}".format(self.from_who, ",".join([r.email for r in self.recipients]), msg.as_string()))
            self.sent = False
            return
        try:
            s.sendmail(_email.parseaddr(self.from_who)[1], [r.email for r in self.recipients], msg.as_string())
        except SMTPServerDisconnected:
            print("Not an email server, did not send email from {} to {} with content:\n{}".format(self.from_who, ",".join([r.email for r in self.recipients]), msg.as_string()))
            self.sent = False
            return

        s.quit()
        self.sent = True

class BulkEmail(Email):
    pass

if __name__ == "__main__":

    email = Email()
    email.define_sender('adammorris@ssis-suzhou.net', 'Adam Morris')

    read_in_templates('../../templates', email)
    
    email.make_subject("DragonNet!")

    email.add_to("amorris@mistermorris.com")
    email.add_cc("adammorris@ssis-suzhou.net", "Adam Morris")
    email.add_language("en")
    email.add_language("kor")
    email.define_field('username', 'piss')
    email.define_field('salutation', 'Dear Mr & Mrs Morris')
    email.send()
