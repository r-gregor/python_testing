#! /usr/bin/env python3

import re

'''
# original movie dirname
MN = "The Guardians of the galaxy, Vol. 2 (2017) [DVDRIP] [1080p] [YTS.AM]"

# regex pattern search expression
# everything after the last ')'
regx_MN = re.compile(r'\)(.*)')

# regex object
S2 = regx_MN.search(MN)

# regex rezult pattern
PAT2 = S2.group(1)

# ljust spaces num
JN = 30

MN2 = MN.replace(PAT2, '')
print('Original movie dirname:'.ljust(JN), end = '')
print("'" + MN + "'")

print('Pattern to remove:'.ljust(JN), end = '')
print("'" + PAT2 + "'")

print('NEW movie dirname:'.ljust(JN), end = '')
print("'" + MN2 + "'")
'''

# ------------------------------------------------------------------------------------------------------------
# function

MNL = ["The Guardians of the galaxy, Vol. 2 (2017) [DVDRIP] [1080p] [YTS.AM]",
"King Kong (2016)",
"The Game (1986) [YTS.AG]",
"Fast and Furious (2015) [BlueRay] [YTS.AM]",
"Two Moon Junction: The new order (vol. 2) (2001) [YTS.AG]"]

def clean_dirname(orig_dirname):
	regx_MDN = re.compile(r'\(\d{4}\)(.*)')
	regx_OB = regx_MDN.search(orig_dirname)
	PAT = regx_OB.group(1)
	new_dirname = orig_dirname.replace(PAT, '')
	return new_dirname
   

MNL2 = []
for o_dirname in MNL:
	n_MDN = clean_dirname(o_dirname)
	if not o_dirname == n_MDN:
		print(o_dirname + " --> " + n_MDN)
		MNL2.append(n_MDN)
	else:
		print("OLD == NEW!!")

print("New list with corrected dirnames:")		
print(MNL2)
