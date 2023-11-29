#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# filename: rename1_fname.py
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
		Usage: rename1_fname.py [filename] [patt] [repl]

		[filename]	  existing filename
		[patt]		  patern to replace
		[repl]		  replacement
'''

# FUNCTIONS ==============================================================

def crtice():
	print("[ {} ] -- ".format(tms()) + "-"*80)


def done():
	print("[ {} ] -- ".format(tms()) + "Done")
	crtice()

# FUNCTIONS ==============================================================

def fun2_replace_patt(f_name, frm, rpl):
	'''
	Repplaces substring:
	- replaces a substring [pattern] with [replacement]
	- returns new filename
	'''

	fname2, ext2 = f_name.rsplit(".", 1)
	if ext2 == "backup":
		print("[ {} ] -- ".format(tms()) + "Filename is *.backup ... aborting.")
		sys.exit()

	# create list of filename words
	fnml = fname2
	# print(fnml) # TEST

	if frm in fnml:
		fnml = fnml.replace(frm, rpl)

	f_fname_2 = fnml + "." + ext2
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

if len(sys.argv) == 4:
	my_fname_2 = sys.argv[1]
	frm = sys.argv[2]
	rpl = sys.argv[3]

	if not check_fname(my_fname_2):
		print("[ {} ] -- ".format(tms()) + "A filename [ {} ] NOT found!".format(my_fname_2))
		sys.exit()

	new_fname_2 = fun2_replace_patt(my_fname_2, frm, rpl)
	rename_f(my_fname_2, new_fname_2)


else:
	print("[ {} ] -- ".format(tms()) + "An existing filename and pattern, replacement must be supplied as arguments!")
	print(my_usage)
	sys.exit()
