#! /usr/bin/env python3

''' Date: 20180322
Module contains functions:
1 - to remove '[YTS*A*]' pattern from movie fname (regular file),
2 - to create a dict with oldfnm as key and newfnm as value.

'''

import os, sys
import re

# FUNCTION_01 ------------------------------------------------------------------------------------------------
def remove_yts_fname(fname_orig):
	'''
	FUNCTION_01: remove_yts_fname(fname_orig) removes '*[YTS*A*]' from movie fname.
	It works for the single fname and returns single new fname. For multiple fnames, run function on
	each iteration of collection.
	'''
	patob = re.compile(r'[-_.]\[\w*[-_.]\w*\]')
		
	# check if spaces in fname -- probably a movie DIRNAME ...
	if ' ' in fname_orig:
		return None
		
	pats = patob.search(fname_orig)
	if pats != None:
		toremove = pats.group()
		newfname = fname_orig.replace(toremove, '')

	else:
		return None
	
	return newfname

# FUNCTION_02 ------------------------------------------------------------------------------------------------
# to rename use FUNCTION_01
# input is a list of files in curdir
def new_fnames_dict(mydir):
	'''
	FUNCTION_02: new_fnames_dict(mydir) creates a dictionary with key = original fname,
	val = new fname if key != val for all original movie fnames with '*[YTS*A*]'.
	
	it uses FUNCTION_01: 'remove_yts_fname(fname_orig)' to create new fname.
	
	exmpl:
		{'Movie.1.fname-[YTS.AG].mp4' : 'Movie.1.fname.mp4'}
	
	To really rename: os.rename(oldfname, nefname) --
		for key in dict:
			oldname = key
			newname = dict[key]
			os.rename(oldname, newname)
	'''

	curdir = mydir
	
	# creating a list of regular files in curdir
	flist = [F for F in os.listdir(curdir) if os.path.isfile(curdir + F)]
	# TEST:
	# print(flist)
	
	# initialize empty dict
	new_fnames_d = {}
	
	# for all elements (oldfnames) in the list create newfname if oldfname != None
	for oldfname in flist:
		newfname = remove_yts_fname(oldfname)
		if newfname != None:
			print(oldfname, newfname)
			new_fnames_d[oldfname] = newfname
	
	# return a dict
	return new_fnames_d
