#! /usr/bin/python3
### (PYTHON3 !!)

# importing python modules:
import smtplib
import os
import argparse
import sys

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from send_config_d import *

# clear the screen:
os.system('clear')

# Parsing argument: url:
parser = argparse.ArgumentParser()
parser.add_argument('url', help = "The URL without trailing '/'")
args = parser.parse_args()

gr_URL = args.url
print("URL = ", gr_URL)

gr_3w, gr_FJL = gr_URL.rsplit('/', 1)

print("gr_3w = ", gr_3w)
print("gr_FJL = ", gr_FJL)

if ('.' in gr_FJL):
	gr_NM, gr_ext = gr_FJL.rsplit('.')
else:
	gr_NM = gr_FJL

print("gr_NM = ", gr_NM)


gr_TJTL = str(gr_NM.replace('-', ' '))
gr_SBJ = gr_TJTL.capitalize()
gr_BDYF = gr_SBJ + "\n" + gr_URL


# Starting SENDMAIL
gr_SCRNM = sys.argv[0]
print("Starting " + gr_SCRNM + "...")

# Composing a email message: header + body ...
gr_MSGF = MIMEMultipart()
gr_MSGF['From'] = gr_FROM
gr_MSGF['To'] = ', '.join(gr_TO)
# gr_MSGF['To'] = gr_TO

gr_MSGF['Subject'] = str(gr_SBJ)

gr_MSGF.attach(MIMEText(gr_BDYF, 'plain'))

print("\nSENDING MAIL ...")

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(gr_UNM,gr_PSWD)
gr_TXT = gr_MSGF.as_string()
server.sendmail(gr_FROM, gr_TO, gr_TXT)
server.quit()

print("DONE!")
