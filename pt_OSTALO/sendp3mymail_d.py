#! /usr/bin/python3

# importing python modules:
print("Importing modules...")
import smtplib
import os

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# def func to clear the screen [LINUX]:
def cl():
    os.system('clear')

# clear the screen:
cl()
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("x Terminate and send by entering \"done\" on it's own line! x")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("\nStarting sendmymail-en ...")

# define mail variables:
print("Defining variables ...")

gr_SRV='smtp.gmail.com:587'     # SMTP:port

### gr_HSTNM="smtp.googlemail.com"
gr_FROM="gredelonghi@gmail.com"
gr_TO="gredelonghi@yahoo.com"

# Credentals:
gr_UNM="gredelonghi@gmail.com"
gr_PSWD='/Gm/rgr?1968/'

# def func to get user input and store it in gr_user_input variable:
def crt():
    print("\n","-"*80)
    return

print("Defining func to get multiline text ...")
def grf_usrinp():
    global gr_user_input
    gr_user_input = [] 
    entry = input("Enter BODY text, 'done' on its own line to quit:\n----------------------------------------------------------------------\n") 
    while entry != "done": 
        gr_user_input.append(entry) 
        entry = input("") 
    gr_user_input = '\n'.join(gr_user_input) 
    return gr_user_input

# assign return value user input func to variable:
print("Assigning return value user input func to variable ...")
print("\nStarting USER input: ")

print()
gr_SBJ = input("Enter the subject:\n")

print()
gr_MSG = grf_usrinp()
gr_MSG = gr_SBJ + ":\n" + gr_MSG

# 
gr_MSGF = MIMEMultipart()
gr_MSGF['From'] = gr_FROM
gr_MSGF['To'] = gr_TO
gr_MSGF['Subject'] = gr_SBJ

gr_MSGF.attach(MIMEText(gr_MSG, 'plain'))

print("----------------------------------------------------------------------")
print("\nSENDING MAIL ...")

server = smtplib.SMTP('smtp.gmail.com', 587)
### server = smtplib.SMTP(gr_SRV)
server.starttls()
server.login(gr_UNM,gr_PSWD)
gr_TXT = gr_MSGF.as_string()
server.sendmail(gr_FROM, gr_TO, gr_TXT)
server.quit()

print("DONE!")

