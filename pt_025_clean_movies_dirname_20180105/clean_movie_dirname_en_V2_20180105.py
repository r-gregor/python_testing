#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# version: V2
# date: 20180104
# date: 20180105: curdir, fileslist, action on all files that contain [YTS-AG] ...
# clean movie dirname

import os, sys
import datetime as dt

# timestamp
def tms():
	return dt.datetime.now().strftime('%Y%m%d_%H%M%S')

# MESSAGE:
print("[ {} ] -- Starting {} ...".format(tms(), sys.argv[0]))

# current dir
gr_curdir = os.getcwd()


# pattern to search and remove
gr_remove = '[YTS-AG]'

# empty list for found dirs
BL = []

# Insert found filenames into BL list (relative pathnames)
for name in os.listdir(gr_curdir):
	if gr_remove in name:
		BL.append(name)


# If no dir found --> BL list is empty
if BL == []:
	print("[ {} ] -- No dirs with \"{}\" in dirname found!".format(tms(), gr_remove))
	print("[ {} ] -- Done.".format(tms()))
	sys.exit(1)


print("[ {} ] -- {} dirs with \"{}\" in dirname found!".format(tms(), len(BL), gr_remove))
gr_yesno = input("[ {} ] -- Continue?".format(tms()))
	
for gr_dir in BL:
	gr_name2 = gr_dir.replace('[YTS-AG]', '').strip()
	print("[ {} ] -- Replacing '{}' with '{}'".format(tms(), gr_dir, gr_name2))
	os.rename(gr_dir, gr_name2)

print("[ {} ] -- Done.".format(tms()))

