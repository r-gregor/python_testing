#! /usr/bin/env python3
#
# renaming Movie firname -- removing "*[YTS*A*]"
# TEST 20180320
#
# ---------------------------------------------------------------

import re

VNames = ['Movie.fname.1.720p.mp4',
		  'Movie.fname.2.720p-[YTS.AG].mp4',
		  'Movie.fname.3.720p.[YTS-AG].mp4',
		  'Movie.fname.4.1080p-[YTS.AM].avi',
		  'Movie.fname.5.720p.[YTS.AM].mp4',
		  'Movie.fname.6.720p.avi',
		  'Movie.fname.7.720p_[YTS-AM].mkv']
		  
patob = re.compile(r'[-_.]\[\w*[-_.]\w*\]')

pdd = 50

for FN in VNames:
	# print(FN)
	pats = patob.search(FN)
	if pats != None:
		toremove = pats.group()
		# print(toremove)
		newfname = FN.replace(toremove, '')
		print(("Renaming " + FN + " to:").ljust(pdd) + newfname)
	else:
		newfname = FN
		print("-- Keeping original fname: ".ljust(pdd) + newfname)
	