#! /usr/bin/env python3
#
# renaming Movie dirname -- removing everything after (YYYY) ...
# TEST 20180320
#
# ---------------------------------------------------------------

import re

S = [' Movie Dirname 1 (2017)',
	 'Movie Dirname 2	 (2018) ',
	 'Movie Dirname 3 (2016) [1080p]',
	 'Movie Dirname 4 (2015) ',
	 'Movie Dirname 5	  (2014) [1080p] - [YTS.AG]']

# re.object --> anything after (YYYY)
mr = re.compile(r'\([12]\d{3}\)(.*)')

# return string with quotes --> for pretty printing --> TO SEE SPACES
def qstr(strng):
	return "'" + strng + "'"

# padding
pdd = 11

# for each element in S list of Movie dirnames
for YR in S:
	# TEST: print original
	print("{0} {1}".format("Original:".ljust(pdd),qstr(YR)))
	YR = YR.strip()
	
	# search for multiple spaces
	# if found --> replace with single space
	spcs = re.search(r'\s{2,}', YR)
	if spcs != None:
		YR = YR.replace(spcs.group(), " ")

	# rgx --> string from re.object
	rgx = mr.search(YR).group(1)
	
	# if regex found replace it with ''
	if rgx != '':
		clean = YR.replace(rgx, '')
		# print("Cleaned: " + qstr(clean))
		print("{0} {1}".format("Cleaned:".ljust(pdd),qstr(clean)))
	else:
		# print("Cleaned: " + qstr(YR))
		print("{0} {1}".format("Cleaned:".ljust(pdd),qstr(YR)))
	print("-"*50)
