#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# v1.0.1-a (20191106/2/d)

import os, sys
import time as tt
import datetime as dt
from datetime import date

import my_textcolors as myc
barva = myc.b_BLUEB
norm = myc.NN


extf = "rdji.txt"
danes = date.today()


sznm = []
with open(extf, "r") as f:
    for line in f:
        nm, st = line.strip().split(",")
        sznm.append([nm, st])

for el in sznm:
    thisY = danes.year
    name = el[0]
    myd, mym, myy = el[1].split(".")

    if int(mym) < danes.month:
        thisY += 1

    myD = date(thisY, int(mym), int(myd))
    ddif = (myD - danes).days
    newD = "{}.{}.{}".format(str(myD.day).rjust(2, "0"), str(myD.month).rjust(2, "0"), myD.year)

    el.extend([newD, ddif])
sorted_sznm = sorted(sznm, key=lambda x: x[3])

st_crtic = 30 + 15 + 15 + 10 + 9
print("-"*st_crtic) # ------------------------
print("{:<30}{:<15}{:<15}{:<10}{}".format("Ime in priimek", "datum R", "RD", "Let", "dni do RD"))
print("-"*st_crtic) # ------------------------

for el in sorted_sznm:
    prs, myrd, newD, ddif = el
    starost = int(newD.split(".")[2]) - int(myrd.split(".")[2])

    if ddif < 100:
        clr = barva
    else:
        clr = ""
    print("{}{:<30}{:<15}{:<15}{:<10}{:>9}{}".format(clr, prs, myrd, newD, starost, ddif, norm))

print("-"*st_crtic) # ------------------------
