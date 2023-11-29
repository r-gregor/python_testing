#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# argpase test 20071026
import argparse
import os, sys

BL = []
curdir = os.getcwd()

# REAL destination:
# JUST FILENAMES (NO PATH)
# BL = os.listdir(curdir)

### # all files relative to curdir
### for root, dirs, files in os.walk("."):
###	 for name in files:
###		 full_path = os.path.join(root, name)
###		 
###		 # RELATIVE PATH
###		 BL.append(full_path)
###		 
###		 # FULL == ABSOLUTE PATHNAME
###		 # BL.append(os.path.abspath(full_path))

# arguments parser:
# options -o --or: any of the arguments (part of the filename) must match,
# options -a --and: all of the arguments (part of the filename) must match,
# options -s --single: only ONE (single) arguments (part of the filename) must match.

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--type", dest = 'type', choices = ['files', 'dirs'], nargs = 1, help = 'set what to look for: FILES or DIRS')
parser.add_argument("-o", "--or", dest = 'orlist', default = [], nargs = '+', help = 'Use option -o to use OR for combination of WORDs')
parser.add_argument("-a", "--and", dest = 'andlist', default = [],  nargs = '+', help = 'Use option -a to use AND for combination of WORDs')
parser.add_argument("-s", "--single", dest = 'single',  default ="", nargs = 1, help = 'Use option -s to use a single WORD')
args = parser.parse_args()


if args.type == ['dirs']:
	what = 'dirs'
elif args.type == ['files']:
	what = 'files'
else:
	print("ERROR!")


# all files relative to curdir
print("Type is:", what)

if args.type == ['dirs']:
	for root, dirs, files in os.walk("."):
		for name in dirs:
			full_path = os.path.join(root, name)
			
			# RELATIVE PATH
			BL.append(full_path)
			
			# FULL == ABSOLUTE PATHNAME
			# BL.append(os.path.abspath(full_path))

elif args.type == ['files']:
	for root, dirs, files in os.walk("."):
		for name in files:
			full_path = os.path.join(root, name)
			
			# RELATIVE PATH
			BL.append(full_path)
			
			# FULL == ABSOLUTE PATHNAME
			# BL.append(os.path.abspath(full_path))

else:
	print("Error, something went WRONG!")
	sys.exit(1)


gr_orlist = args.orlist
gr_andlist = args.andlist
gr_single = ''.join(args.single) # convert list to a string


if gr_orlist != []:
	print('Selected arguments:', gr_orlist)
	for F in BL:
		# True if ANY of the items in gr_orlist match items in F (single filename from BL)
		if any(item in F for item in gr_orlist):
			print(F)
#		else:
#			break
#			print("No argument from", gr_orlist, "matches any part of filenames in", os.getcwd())

elif gr_andlist != []:
	print('Selected arguments:', gr_andlist)
	for F in BL:
		# True if ALL items in gr_andlist match items in F (single filename from BL)
		if all(item in F for item in gr_andlist):
			print(F)
#		else:
#			break
#			print("Arguments from", gr_andlist, "do not match any part of filenames in", os.getcwd())

elif gr_single != '':
	print('Selected argument:', gr_single)
	for F in BL:
		if gr_single in F:
			print(F)
#		else:
#			break
#			print(gr_single, "does not match any part of filenames in", os.getcwd())
