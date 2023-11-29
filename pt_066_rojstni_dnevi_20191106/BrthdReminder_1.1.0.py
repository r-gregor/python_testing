#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# v1.0.0    (20191106/1/en)
#   original version
#
# v1.0.2   (20191107/4/en)
#   - added 0-preappend singlenum for day and month: my[d,m].rjust(2, "0")
#     for newD
#   - added green color if ddif <= 30 days
#   - added lila color if ddif <= 7 days
#   - added red color if ddif == 0 days
#   - changed test if ddif < 0 to add 1 year to thisY
#   - added COLORS (not imported from ext module)
#   - changed imput file to: ROJSTNIDNEVI.txt
#   - limited printout to those with ddif <= 100 days
#   - printouts converted into functions
#   - added option if name as arg in list printout for those names
#   - added reltive location of ROJSTNIDNEVI.txt file:
#           script_dir = os.path.dirname(__file__)
#           extf = script_dir + "/ROJSTNIDNEVI.txt"
#
# v1.0.3    (20191107/5/en) ??
# v1.0.4    (20191107/6/d)
#   - corrected realpath of softlinked parent directory so that it
#     can access extf from original location:
#           heref = (Path(__file__)).resolve()
#           here = heref.parent
#           extf = os.path.join(here, "ROJSTNIDNEVI.txt")
#   - Must softlink absolute paths of both source and dest!!
#
# v1.0.5    (20191111/7/en)
#   - Print functions renamed to Display
#   - Display(howmany) --> display persons with less than howmany days till BD
#   - DisplayAll() --> display all (not just 100 days till BD)
#   - display = [el for el in sorted_sznm if el[3] <=100] ... moved to mydisplay in Display(howmany)
#   - if argument all --> Dispay All
#
# v1.1.0    (20200305/8/en)
#   - remove duplicates before appending to a list


# imports
import os, sys
import time as tt
import datetime as dt
from pathlib import Path


# COLORS COLORS COLORS COLORS COLORS COLORS COLORS COLORS COLORS
c_RED = "\x1b[31m"
c_REDB = "\x1b[31;1m"
c_BLACK = "\x1b[30m"
c_BLACKB = "\x1b[30;1m"
c_GREEN = "\x1b[32m"
c_GREENB = "\x1b[32;1m"
c_YELLOW = "\x1b[33m"
c_YELLOWB = "\x1b[33;1m"
c_BLUE = "\x1b[34m"
c_BLUEB = "\x1b[34;1m"
c_MAGENTA = "\x1b[35m"
c_MAGENTAB = "\x1b[35;1m"
c_CYAN = "\x1b[36m"
c_CYANB = "\x1b[36;1m"
c_WHITE = "\x1b[37m"
c_WHITEB = "\x1b[37;1m"

b_RED = "\x1b[41m"
b_REDB = "\x1b[41;1m"
b_BLACK = "\x1b[40m"
b_BLACKB = "\x1b[40;1m"
b_GREEN = "\x1b[42m"
b_GREENB = "\x1b[42;1m"
b_YELLOW = "\x1b[43m"
b_YELLOWB = "\x1b[43;1m"
b_BLUE = "\x1b[44m"
b_BLUEB = "\x1b[44;1m"
b_MAGENTA = "\x1b[45m"
b_MAGENTAB = "\x1b[45;1m"
b_CYAN = "\x1b[46m"
b_CYANB = "\x1b[46;1m"
b_WHITE = "\x1b[47m"
b_WHITEB = "\x1b[47;1m"

NN = "\x1b[0m"
REV = "\x1b[7m"
UNDRL = "\x1b[7m"
# COLORS COLORS COLORS COLORS COLORS COLORS COLORS COLORS COLORS

# color aliases
blue = b_BLUEB
green = b_GREENB
red = b_REDB
lila = b_MAGENTAB
norm = NN

# must softlink absolute paths of both source and dest
heref = (Path(__file__)).resolve()
here = heref.parent
extf = os.path.join(here, "ROJSTNIDNEVI.txt")

danes = dt.date.today()


sznm = []
with open(extf, "r") as f:
    for line in f:
        nm, brdt = line.strip().split(",")
        if [nm, brdt] in sznm:
            continue
        else:
            sznm.append([nm, brdt])



for el in sznm:
    thisY = danes.year
    name = el[0]
    myd, mym, myy = el[1].split(".")

    myD = dt.date(thisY, int(mym), int(myd))
    ddif = (myD - danes).days

    if ddif < 0:
        thisY += 1
        myD = dt.date(thisY, int(mym), int(myd))
        ddif = (myD - danes).days

    newD = "{}.{}.{}".format(myd.rjust(2, "0"), mym.rjust(2, "0"), myD.year)

    el.extend([newD, ddif])

# sorted --> not inplace (like sort()) --> to another list ...
sorted_sznm = sorted(sznm, key=lambda x: x[3])


def Display(howmany):
    mydisplay = [el for el in sorted_sznm if el[3] <= howmany]
    st_crtic = 30 + 15 + 15 + 10 + 9
    print("-"*st_crtic)
    print("{:<30}{:<15}{:<15}{:<10}{}".format("Ime in priimek", "datum R", "RD", "Let", "dni do RD"))
    print("-"*st_crtic)

    for el in mydisplay:
        prs, myrd, newD, ddif = el
        starost = int(newD.split(".")[2]) - int(myrd.split(".")[2])

        if ddif <= 31 and ddif > 7:
            clr = blue
        elif ddif <= 7 and ddif > 0:
            clr = green
        elif ddif == 0:
            clr = red
        else:
            clr = ""
        print("{}{:<30}{:<15}{:<15}{:<10}{:>9}{}".format(clr, prs, myrd, newD, starost, ddif, norm))

    print("-"*st_crtic)
    print("Prikaz oseb z manj kot {} dni do RD\n\n".format(howmany))


def DisplayAll():
    st_crtic = 30 + 15 + 15 + 10 + 9
    print("-"*st_crtic)
    print("{:<30}{:<15}{:<15}{:<10}{}".format("Ime in priimek", "datum R", "RD", "Let", "dni do RD"))
    print("-"*st_crtic)

    for el in sorted_sznm:
        prs, myrd, newD, ddif = el
        starost = int(newD.split(".")[2]) - int(myrd.split(".")[2])

        if ddif <= 31 and ddif > 7:
            clr = blue
        elif ddif <= 7 and ddif > 0:
            clr = green
        elif ddif == 0:
            clr = red
        else:
            clr = ""
        print("{}{:<30}{:<15}{:<15}{:<10}{:>9}{}".format(clr, prs, myrd, newD, starost, ddif, norm))

    print("-"*st_crtic)

def DisplayPers(selected):
    st_crtic = 30 + 15 + 15 + 10 + 9
    print("-"*st_crtic)
    print("{:<30}{:<15}{:<15}{:<10}{}".format("Ime in priimek", "datum R", "RD", "Let", "dni do RD"))
    print("-"*st_crtic)

    for el in selected:
        prs, myrd, newD, ddif = el
        starost = int(newD.split(".")[2]) - int(myrd.split(".")[2])

        if ddif <= 31 and ddif > 7:
            clr = blue
        elif ddif <= 7 and ddif > 0:
            clr = green
        elif ddif == 0:
            clr = red
        else:
            clr = ""
        print("{}{:<30}{:<15}{:<15}{:<10}{:>9}{}".format(clr, prs, myrd, newD, starost, ddif, norm))

    print("-"*st_crtic)

single = []
if len(sys.argv) == 2:
    if sys.argv[1].upper() == "ALL":
        DisplayAll()
        sys.exit(1)
    else:
        person = sys.argv[1].upper()
        for el in sorted_sznm:
            if person in el[0].upper():
                 single.append(el)
            else:
                continue
    if single != []:
        DisplayPers(single)
    else:
        Display(50)
else:
    Display(100)
