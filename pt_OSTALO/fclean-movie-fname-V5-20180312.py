#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# version: V5
# date: 20180104
# date: 20180105: curdir, fileslist, action on all files that contain [YTS-AG] ...
# date: 20180312: nef function with regex to select everything after (YYYY) ...
# clean movie dirname

import os, sys
import datetime as dt
import re

# timestamp
def tms():
	return dt.datetime.now().strftime('%Y%m%d_%H%M%S')

# MESSAGE:
print("[ {} ] -- Starting {} ...".format(tms(), sys.argv[0]))

# fnames
fnames = os.listdir(".")

def clean_fname(orig_fname):
	# check if cont_pat in filename
	regx_FNM = re.compile(r'[.-]\[YTS[.-]A.\]')
	regx_FOB = regx_FNM.search(orig_fname)
	if regx_FOB != None:
		regx_PAT = regx_FOB.group()
		PAT = regx_FOB.group()
		new_fname = orig_fname.replace(PAT, '')
		return new_fname
		
TL = []
for fn in fnames:
	n_fname = clean_fname(fn)
	if n_fname != None:
		TL.append(fn)

if TL == []:
	print("[ {} ] -- No files with [YTS*A*] in fname found!".format(tms()))
	print("[ {} ] -- Done.".format(tms()))
	sys.exit(1)		

print("[ {} ] -- {} files with [YTS*A*] in fname found!".format(tms(), len(TL)))
gr_yesno = input("[ {} ] -- Continue?".format(tms()))

for fn in fnames:
	n_fname = clean_fname(fn)
	print("[ {} ] -- Renaming {} --> {}".format(tms(), fn, n_fname))
	os.rename(fn, n_fname)



# ------------------------------------------------------------------------------------------------------------
'''
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
'''
