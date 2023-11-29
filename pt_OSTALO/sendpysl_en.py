#! /usr/bin/python2
# -*- coding: utf-8 -*-

# importing python modules:
print("Importing modules...")
import smtplib
import os
import argparse

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Parsing arguments: subject, body:
parser = argparse.ArgumentParser()

parser.add_argument('subject', help='The message subject')
parser.add_argument('body', help='The BODY of the message')
args = parser.parse_args()

# def func to clear the screen [LINUX]:
def cl():
	os.system('clear')

# clear the screen:
# cl()
print("Starting sendmymail-en ...")


# define mail variables:
print("Defining variables ...")

# gr_SRV='mail.jhl.si:587'	# SMTP:port

### gr_HSTNM="smtp.googlemail.com"
gr_FROM="gregor.redelonghi@energetika.si"
gr_TO="gredelonghi@gmail.com"

# Credentals:
gr_UNM="gregor.redelonghi@energetika.si"
gr_PSWD='/En/gr.01/'


def crt():
	print("\n","-"*80)
	return

print()
gr_SBJ = args.subject
gr_BDY = args.body

print("gr_SBJ = args.subject =", gr_SBJ)
print("gr_BDY = args.body =", gr_BDY)

# 
gr_MSGF = MIMEMultipart()
gr_MSGF['From'] = gr_FROM
gr_MSGF['To'] = gr_TO
gr_MSGF['Subject'] = str(gr_SBJ)

gr_MSGF.attach(MIMEText(gr_BDY, 'plain'))

print("----------------------------------------------------------------------")
print("\nSENDING MAIL ...")

# server = smtplib.SMTP('smtp.gmail.com:587')
server = smtplib.SMTP('mail.jhl.si', 587)
server.starttls()
server.login(gr_UNM,gr_PSWD)
gr_TXT = gr_MSGF.as_string()
server.sendmail(gr_FROM, gr_TO, gr_TXT)
server.quit()

print("DONE!")

