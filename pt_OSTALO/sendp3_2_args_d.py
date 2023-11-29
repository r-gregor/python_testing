#! /usr/bin/env python3
### (PYTHON3 !!)

# importing python modules:
import smtplib
import os
import argparse
import sys

# import local email settings:
from send_config_d import *

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# clear the screen:
os.system('clear')

# Parsing arguments: subject, body:
parser = argparse.ArgumentParser()

parser.add_argument('subject', help='The message [SUBJECT] (between quotes if it contains spaces)')
parser.add_argument('body', help='The [BODY] of the message (between quotes if it contains spaces, or if multiline -- closing with quote sign!)')
args = parser.parse_args()

# Starting SENDMAIL
gr_SCRNM = sys.argv[0]
print("Starting " + gr_SCRNM + "...")


### # obsolete - fetched from send.config.en:
### # define mail variables:
### # Header info:
### gr_FROM="gregor.redelonghi@energetika-lj.si"
### gr_TO = ['gredelonghi@gmail.com', 'gredelonghi@yahoo.com']
### 
### # Credentals:
### gr_UNM="gregor.redelonghi@energetika-lj.si"
### gr_PSWD='/En/gr.01/'

# Assigning arguments to variables:
gr_SBJ = args.subject
gr_BDY = args.body

# Inserting a SUBJECT as first line into BODY:
gr_BDYF = gr_SBJ + ":\n" + gr_BDY

# Composing a email message: header + body ... 
gr_MSGF = MIMEMultipart()
gr_MSGF['From'] = gr_FROM
# gr_MSGF['To'] = gr_TO
gr_MSGF['To'] = ', '.join(gr_TO)
gr_MSGF['Subject'] = str(gr_SBJ)

gr_MSGF.attach(MIMEText(gr_BDYF, 'plain'))


# send email:
print("\nSENDING MAIL ...")

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(gr_UNM,gr_PSWD)
gr_TXT = gr_MSGF.as_string()
server.sendmail(gr_FROM, gr_TO, gr_TXT)
server.quit()

print("DONE!")

