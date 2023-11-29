#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# version: V2
# date: 20180104
# date: 20180105: curdir, fileslist, action on all files that contain [YTS-AG] ...
# clean movie dirname

import os, sys
import datetime as dt
import re


# timestamp
def tms():
	return dt.datetime.now().strftime('%Y%m%d_%H%M%S')

# MESSAGE:
print("[ {} ] -- Starting {} ...".format(tms(), sys.argv[0]))

# current dir
gr_curdir = os.getcwd()

# function to clean dirname
def clean_dirname(orig_dirname):
	regx_MDN = re.compile(r'\(\d{4}\)(.*)')
	regx_OB = regx_MDN.search(orig_dirname)
	if regx_OB != None:
		PAT = regx_OB.group(1)
		new_dirname = orig_dirname.replace(PAT, '')
		return new_dirname

# empty list for found dirs
BL = []

for name in os.listdir(gr_curdir):
	new_dirname = clean_dirname(name)
	if name != new_dirname:
		BL.append(name)
	
if BL == []:
	print("[ {} ] -- No dirs with aditional chars after (YYYY) in dirname found!".format(tms()))
	print("[ {} ] -- Done.".format(tms()))
	sys.exit(1)

print("[ {} ] -- {} dirs with aditional chars after (YYYY) in dirname found!".format(tms(), len(BL)))
gr_yesno = input("[ {} ] -- Continue?".format(tms()))

for gr_dir in BL:
	gr_name2 = clean_dirname(gr_dir)
	print("[ {} ] -- Replacing '{}' with '{}'".format(tms(), gr_dir, gr_name2))
	os.rename(gr_dir, gr_name2)

print("[ {} ] -- Done.".format(tms()))
