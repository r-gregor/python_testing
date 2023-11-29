#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script that displays all dirs and files under the root dir (startdir). Searches for pattern
in full pathname, and displays it if found, otherwise display a note, that it wos not found.
All printouts are enumerated by counter, and formatted printed.
"""

import subprocess, os, sys
import m_dirs_conf

curdir = m_dirs_conf.gr_DIR
src_p = m_dirs_conf.gr_SRCP

# curdir = "/h/2017/_2017_obdelano" # test
# curdir = "/c/Users/gregor.redelonghi/majstaf/BRISI"
gr_DIRS = []	# initialize empty dirs list
gr_FILES = []   # initialize empty files list

for root, dirs, files in os.walk(curdir):
	for f in files:
		fulf = os.path.join(root, f)	# join root dirs and files
		gr_FILES.append(fulf)		   # append full path to file to files list
	
	for d in dirs:
		fuld = os.path.join(root, d)	# join root dir and subdirs
		gr_DIRS.append(fuld)			# append ful path to subdir to dirs list

### src_p = "Brezov"   # search pattern - for "whole" path: root/subdir/file ...


# main
if __name__ == "__main__":

	ff = 0		  # [cv] control value - updated if search pattern found, otherwise remains "0"
	i = 1		   # initial counter for files
	for f in gr_FILES:
		if src_p in f:
			print("{0:4}{1:2}{2}".format(str(i), "-", f))
			i += 1  # counter for files: if src_p found - increase by "1"
			ff += 1 # [cv] if src_p found - increase by "1"
			
	if ff == 0:	 # [cv] if src_p not found -->value of ff is still "0"
		print("\n" + "Search item \"" + src_p + "\" not found!")
	
	   
	print("----------------------------------------------")
	
	j = 1		   # initial counet for dirs
	for d in gr_DIRS:
		print("{0:4}{1:2}{2}".format(str(j), "-", d))
		j += 1  # counter for files: if src_p found - increase by "1"

