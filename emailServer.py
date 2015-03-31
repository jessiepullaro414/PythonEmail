import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import email.utils
from time import localtime, strftime

me = "insert email here"
you = "insert email here"

msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'test message'
msgRoot['me'] = me
msgRoot['you'] = you
msgRoot.preamble = 'This is a multi-part message in MIME format.'

msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

msgText = MIMEText('This is the alternative plain text message.')
msgAlternative.attach(msgText)

msgText = MIMEText('<b>Heck <i>Yes</i> it</b> works with an image.<br>'
                   '<img src="cid:Florida-Polytechnic-University-IBM-supercomputer.jpg"><br>Nifty! '
                   + strftime("%a, %d %b %Y %H:%M:%S", localtime()), 'html')
msgAlternative.attach(msgText)

fp = open('C:/Python34/tcl/Florida-Polytechnic-University-IBM-supercomputer.jpg', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

msgImage.add_header('Content-ID', '<Florida-Polytechnic-University-IBM-supercomputer.jpg>')
msgRoot.attach(msgImage)

s = smtplib.SMTP("smtp.gmail.com:587")
s.starttls()
s.login("insert email here","insert email password here")
s.sendmail(me, you, msgRoot.as_string())
s.quit()