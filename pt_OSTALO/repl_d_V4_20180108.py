#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# version V2: function changef; more pnc-s; formated printout;
# version V3: added .strip() method to string objcts to remove leading/trailing spaces from names and exts
# date: 20180104
#
# replace spaces and uncommon characters from filenames or dirnames [NOT for movie folders -- replaces spaces]

import os, sys
import datetime as dt

# timestamp
def tms():
    return dt.datetime.now().strftime('%Y%m%d_%H%M%S')

# MESSAGE:
print("[ {} ] -- Starting {} ...".format(tms(), sys.argv[0]))

# current dir
gr_curdir = os.getcwd()

# empty list for found dirs
BL = []

# Insert found filenames into BL list (relative pathnames)
for name in os.listdir(gr_curdir):
    BL.append(name)

# TEST
print(BL)
print()

# a dict of characters with replacements - files
pnc = {'(':'',
    ')':'',
    '[':'',
    ']':'',
    ':':'',
    ';':'',
    ' ':'_',
    '.':'-',
    ',':'',
    '?':'',
    '&':'',
    '!':'',
    '#':''}

def changef(name):
    lng = len('Changing:')
    numl = lng + len(S) + 3 # 3 --> 1 spaces + quotes

    # divide filename to name and extension
    if '.' in S:
        Sb, Se = S.rsplit('.', 1)
        Sb = Sb.strip()
        Se = Se.strip()
    else:
        Sb = S.strip()
        Se = '0'


    # initiate empty temporary list to fill in the characters
    L1 = []

    # if character from dict in string --> replace and append to list L1
    for c in Sb:
        for p in pnc.keys():
            if c == p:
                c = pnc[c]
                cnt = True
        L1.append(c)

    # create a string from list L1
    Sb1 = ''.join(L1)

    # replace duplicate underscores
    Sb2 = Sb1.replace('_-_', '-')

    # concatenate name and extension to final filename
    if Se == '0':
        S2 = Sb2
    else:
        S2 = Sb2 + '.' + Se

    if S == S2:
        pass
    else:
        print("{} {}".format("Changing:".rjust(lng), ("'" + S + "'")))
        print("{} {}".format("To:".rjust(lng), ("'" + S2 + "'")))
        print("-"*numl)
        os.rename(S, S2)

for S in BL:
    changef(S)

print("[ {} ] -- Done.".format(tms()))
