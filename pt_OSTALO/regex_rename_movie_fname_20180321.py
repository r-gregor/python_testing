#! /usr/bin/env python3
#
# FUNCTION: remove *[YTS*A*] from movie fname
# TEST 20180321
#
# ---------------------------------------------------------------

import re

# function: remove *[YTS*A*] from movie fname
def rename_fnm(FNM):
	''' Function rename_fnm removes '*[YTS*A*]' from movie fname '''

	patob = re.compile(r'[-_.]\[\w*[-_.]\w*\]')
	fname_orig = FNM
	
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

'''
# TEST:
import rnmfnm as rnmf

LFN = [ 'Movie.1.720p_[YTS.AG].mp4',
		'Movie.2.720p.2017.avi',
		'Movie.3.720p.2005_[YTS.AG].mp4',
		'Movie.4.720p_[YTS-AG].mp4',
		'Movie.5.720p-[YTS.AM].mp4',
		'Movie.6.720p_[YTS-AM].mp4',
		'Movie.7.720p.2016.mkv',
		'Movie.8.1080p-[YTS.AG].mkv',
		'Movie.9.1080p.2013-[YTS.AM].mp4'
]

D = {}

for EL in LFN:
	NEWFN = rnmf.rename_fnm(EL)
	if NEWFN == None:
		continue
	D[EL] = NEWFN

for key in D:
	print(("Renaming " + "'" + key + "'").ljust(50) + " to:  " + "'" + D[key] + "'")
'''