import datetime
import imaplib

__author__ = 'Dmitriy Bulygin'

"""
This script connecting to one server and some user names. 
Deleted messages for some days before (variable beforeDate) 
from 'BACKUP' group in mailserver

demetrius.storm@gmail.com, https://github.com/DemetriusStorm 
"""

# Defines environment variables
imap_host = 'mailserver.org'  # This can be IP adress
# Defines dict of 'accounts: pass'
mails_dict = {
    'mail1@mailserver.org': '12345678',
    'mail2@mailserver.org': '12345678',
    'mail3@mailserver.org': '12345678',
    'mail4@mailserver.org': '12345678',
}

monthListRfc2822 = ['0', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


def mail_connector(username=None, password=None):
    with imaplib.IMAP4(imap_host) as mail:
        mail.login(username, password)
        mail.select('BACKUP')
        typ, data = mail.uid('SEARCH', beforeDateString)
        assert typ == 'OK'
        # For test
        # print(username, typ, data)
        if data:
            for uid in data[0].split():
                print(str(uid))
                mail.uid('STORE', uid, '+FLAGS', '(\\Deleted)')
        mail.expunge()
        mail.logout()


beforeDate = datetime.datetime.today() - datetime.timedelta(days=5)
# For test
# print('beforeDate', beforeDate)
beforeDateString = ("(BEFORE %s-%s-%s)"
                    % (beforeDate.strftime('%d'),
                       monthListRfc2822[beforeDate.month],
                       beforeDate.strftime('%Y')))
# For test
# print('beforeDateString:', beforeDateString + '\n')

for key, item in mails_dict.items():
    mail_connector(key, item)
