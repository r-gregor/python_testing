#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# version V2: function changef; more pnc-s; formated printout;
# version V3: added .strip() method to string objcts to remove leading/trailing spaces from names and exts
# date: 20180104
#
# replace spaces and uncommon characters from filenames or dirnames [NOT for movie folders -- replaces spaces]


flnms = ["Yoda (The JEDI) - The Grand master.of.the_UNIVERSE.txt",
"Kva je zej Mucke? A se bomo - kej, - mnogo.dool.dajal.mp4",
"Judo - the technics (common actions) - for the strong? While, do we go there.alone.jpg",
"The Terminator (2017) [YTS-AG]  ",
"Mission impossible 3: Rough nation (2016)",
"Walhalla - the content shredding management; extra manual.pdf", 
" Huge, and not so obvious drinking-with-buddies [SHOW] case  . jpg "]

def changef(name):
    lng = len('Changing:')
    numl = lng + len(S) + 3 # 3 --> 1 spaces + quotes

    print("{} {}".format("Changing:".rjust(lng), ("'" + S + "'")))

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
    
    print("{} {}".format("To:".rjust(lng), ("'" + S2 + "'")))
    print("-"*numl)

for S in flnms:
    changef(S)