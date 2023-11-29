#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# 1.0.0 (20161106/1/en -- ORIGINAL)

import os, sys
import time as tt
import datetime as dt
from datetime import date
from dateutil import relativedelta as rlt

import my_textcolors as myc
barva = myc.b_BLUEB
norm = myc.NN


extf = "rdji.txt"
sznm = {}
with open(extf, "r") as f:
    for line in f:
        nm, st = line.split(",")
        dt = st.strip().split(".")
        sznm[nm] = list(dt)

# test
# print(sznm)


danes = date.today()

st_crtic = 30 + 15 + 9
print("-"*st_crtic)
print("{:<30}{:<15}{}".format("Kdo", "RD", "dni do RD"))
print("-"*st_crtic)

for prs, dt in sznm.items():
    thisY = danes.year
    mym = dt[1].rjust(2, "0")
    myd = dt[0].rjust(2, "0")
    myy = dt[2]

    # myrd = "{}-{}-{}".format(myy, mym, myd)
    myrd = "{}.{}.{}".format(myd, mym, myy)

    if int(mym) < danes.month:
        thisY += 1

    myD = date(thisY, int(mym), int(myd))

    ddif = (myD - danes).days
    if ddif < 100:
        clr = barva
    else:
        clr = ""
    print("{}{:<30}{:<15}{}{}".format(clr, prs, myrd, ddif, norm))

print("-"*st_crtic)
