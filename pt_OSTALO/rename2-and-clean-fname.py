#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# filename: rename2_and_clean_fname.py
# version: V1 (20190130)

import os, sys
import datetime as dt
import re
import shutil

# timestamp
def tms():
    return dt.datetime.now().strftime('%Y%m%d_%H%M%S')

# USAGE
my_usage = '''
        Usage: rename_and_clean_fname.py [filename] [patt] [repl]

        [filename]      existing filename
        [patt]          patern to replace
        [repl]          replacement
'''

# FUNCTIONS ==============================================================

def crtice():
    print("[ {} ] -- ".format(tms()) + "-"*80)


def done():
    print("[ {} ] -- ".format(tms()) + "Done")
    crtice()

# FUNCTIONS ==============================================================

def fun1_clean_fname(f_name):
    '''
    Cleans the filename:
        - converts spaces and hypens to underscores
        - removes braces
        - all letters to lowercase
        - returns new filename
    '''

    fname1, ext1 = f_name.rsplit(".", 1)
    if ext1 == "backup":
        print("[ {} ] -- ".format(tms()) + "Filename is *.backup ... aborting.")
        sys.exit()

    # a dict of characters with replacements - files
    pnc = {'(':'',
        ')':'',
        '[':'',
        ']':'',
        ':':'',
        ';':'',
        '.':'-',
        ',':'',
        '?':'',
        '&':'',
        '$':'',
        '!':'',
        '#':'',
        '%':'',
        '*':'',
        '<':'',
        '>':''}

    # initiate empty temporary list to fill in the characters
    L1 = []

    # if character from dict in string --> replace single character and append to list L1
    for c in fname1:
        for p in pnc.keys():
            if c == p:
                c = pnc[c]
                cnt = True
        L1.append(c)

    # create a string from list L1
    f_name = ''.join(L1) + "." + ext1
    # print(f_name)


    f_name = re.sub(' +', '_', f_name)
    f_name = re.sub('-+', '_', f_name)
    f_name = f_name.replace("(", "").replace(")", "").lower()
    f_name = re.sub('_+', '_', f_name)

    return f_name

# FUNCTIONS ==============================================================


def fun3_replace_patt(f_name, frm, rpl):
    '''
    Repplaces substring:
    - calls ext function to clean filename
    - replaces a substring [pattern] with [replacement]
    - returns new filename
    '''

    fname2, ext2 = f_name.rsplit(".", 1)
    if ext2 == "backup":
        print("[ {} ] -- ".format(tms()) + "Filename is *.backup ... aborting.")
        sys.exit()

    # create list of filename words
    fnml = fname2.split("_")
    # print(fnml) # TEST

    if frm in fnml:
        fnml[fnml.index(frm)] = rpl

    f_fname_2 = "_".join(fnml) + "." + ext2
    return f_fname_2

# FUNCTIONS ==============================================================

def check_fname(f_name):
    '''
    Checks if filename exists
    '''
    f_list = os.listdir(".")

    if f_name not in f_list:
        return False
    else:
        return True

# FUNCTIONS ==============================================================

def rename_f(f_name, new_f_name):
    '''
    Rename file.
    '''

    if f_name == new_f_name:
        print("[ {} ] -- ".format(tms()) + "Filenames are equal -- no renaming necessary")
        sys.exit()
    else:
        fname = f_name
        fname_bkp = fname + ".backup"
        print("[ {} ] -- ".format(tms()) + "Creating a backup file: [ {} ]".format(fname_bkp))
        shutil.copy(fname, fname_bkp)

        print("[ {} ] -- ".format(tms()) + "Renaming from [ {} ] to  [ {} ] ...".format(f_name, new_f_name))
        os.rename(f_name, new_f_name)
        done()

# FUNCTIONS ==============================================================


# MAIN
print("[ {} ] -- ".format(tms()) + "Starting {} ...".format(sys.argv[0]))

if len(sys.argv) == 2:
    my_fname_1 = sys.argv[1]

    if not check_fname(my_fname_1):
        print("[ {} ] -- ".format(tms()) + "A filename [ {} ] NOT found!".format(my_fname_1))
        sys.exit()

    new_fname_1 = fun1_clean_fname(my_fname_1)
    rename_f(my_fname_1, new_fname_1)


elif len(sys.argv) == 4:
    my_fname_2 = sys.argv[1]
    frm = sys.argv[2]
    rpl = sys.argv[3]

    if not check_fname(my_fname_2):
        print("[ {} ] -- ".format(tms()) + "A filename [ {} ] NOT found!".format(my_fname_2))
        sys.exit()

    new_fname_2 = fun1_clean_fname(my_fname_2)
    new_fname_3 = fun3_replace_patt(new_fname_2, frm, rpl)
    rename_f(my_fname_2, new_fname_3)


else:
    print("[ {} ] -- ".format(tms()) + "An existing filename and/or pattern, replacement must be supplied as arguments!")
    print(my_usage)
    sys.exit()
