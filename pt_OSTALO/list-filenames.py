#! /usr/bin/env python3
# -*- coding: utf-8 -*-

''' 
filename:   ddbak.py
date:	   20171116

script that finds all *.bak files listed in BASEDIR/dirlist.conf ( to do! ).
Currently the absolute path to dirname is declared as global variable.
'''

import os, sys

# empty list for found filenames
BL = []

# gr_curdir = os.getcwd()

# current dir
gr_curdir = "/c/Users/gregor.redelonghi/2018"

# search pattern (*.bak, *.log -- test = *.txt)
gr_sptn = ".bak"

# Insert found filenames into BL list (absolute pathnames)
for root, dirs, files in os.walk(gr_curdir):
	for name in files:
		full_path = os.path.join(root, name)
		if gr_sptn in full_path:
			# RELATIVE PATH
			# BL.append(full_path)
			
			# FULL == ABSOLUTE PATHNAME
			BL.append(os.path.abspath(full_path))

# If no file found --> BL list is empty
if BL == []:
	print("No \"{}\" files found!".format(gr_sptn))
	print("Done.")
	sys.exit(1)

# If files found BL list not empty --> print: number of files and files
gr_nmf = len(BL)
for L in BL:
	print(L)

print()
print("{} \"{}\" files found!".format(gr_nmf, gr_sptn))

# DELETE?
print()
gr_ans2 = input("Do you wont to delete these files? [y/n] ")

if gr_ans2 in ["y", "Y", "yes", "YES"]:
	for L in BL:
		print("Removing: {}".format(L))
		os.remove(L)

	print()
	print("{} files removed.".format(gr_nmf))

else:
	print()
	print("No files removed. Bye.")
	sys.exit(1)

print("Done.")

