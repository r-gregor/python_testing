#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# version V2: function changef; more pnc-s; formated printout;
# version V3: added .strip() method to string objcts to remove leading/trailing spaces from names and exts
# date: 20180104
#
# replace spaces and uncommon characters from filenames or dirnames [NOT for movie folders -- replaces spaces]

import os, sys
import datetime as dt

# timestamp
def tms():
	return dt.datetime.now().strftime('%Y%m%d_%H%M%S')

# MESSAGE:
print("[ {} ] -- Starting {} ...".format(tms(), sys.argv[0]))

# current dir
gr_curdir = os.getcwd()

# empty list for found dirs
BL = []

# Insert found filenames into BL list (relative pathnames)
for name in os.listdir(gr_curdir):
	BL.append(name)

# a dict of characters with replacements - files
pnc = {'(':'',
	')':'',
	'[':'',
	']':'',
	':':'',
	';':'',
	' ':'_',
	'.':'-',
	',':'',
	'?':'',
	'&':'',
	'!':'',
	'#':''}
	
def crtice(fname):
	lng = len('Changing:')
	numl = lng + len(fname) + 3 # 3 --> 1 spaces + quotes
	return lng, numl

# START BIG changef function ---
def changef(name):
	
	# divide filename to name and extension
	if '.' in name:
		Sb, Se = name.rsplit('.', 1)
		Sb = Sb.strip()
		Se = Se.strip()
	else:
		Sb = name.strip()
		Se = '0'


	# initiate empty temporary list to fill in the characters
	L1 = []

	# if character from dict in string --> replace single character and append to list L1
	for c in Sb:
		for p in pnc.keys():
			if c == p:
				c = pnc[c]
				cnt = True
		L1.append(c)

	# create a string from list L1
	Sb1 = ''.join(L1)

	# concatenate name and extension to final filename
	if Se == '0':
		S2 = Sb1
	else:
		S2 = Sb1 + '.' + Se
	
	# if strings same: do nothing ...
	if name == S2:
		pass
	else:
		lng, numl = crtice(name)
		print("{} {}".format("Changing:".rjust(lng), ("'" + name + "'")))
		print("{} {}".format("To:".rjust(lng), ("'" + S2 + "'")))
		print("-"*numl)
		
		# else rename
		os.rename(name, S2)
 
# END BIG changef function ---


# Check if anything to replace 
GL = ''.join(BL)
gr_sng = 0
for gr_el in ['(', ')', '[', ']', ':', ';', ' ', ',', '?', '&', '!', '#']:
	if gr_el in GL:
		gr_sng += 1
		
if gr_sng > 0:
	print("[ {} ] -- Replacing single chars, spaces ...".format(tms()))
else:
	print("[ {} ] -- NO single chars, spaces to replace ...".format(tms()))

# apply changef function to all filenames in list BL	
for S in BL:
	changef(S)
	


# Check if anything to replace	
GL2 = ''.join(os.listdir(gr_curdir))
gr_sng2 = 0
for gr_el2 in ['_-_', '-_','__']:
	if gr_el2 in GL2:
		gr_sng2 += 1
		
if gr_sng2 > 0:
	print()
	print("[ {} ] -- Replacing double underscores/hypens ...".format(tms()))
else:
	print("[ {} ] -- NO underscores/hypens to replace ...".format(tms()))

# replace duplicate hypen, inderscores and rename
for line in os.listdir(gr_curdir):
	lng, numl = crtice(line)
	line2 = line.replace('_-_', '-').replace('-_', '-').replace('__', '_')
	if line == line2:
		pass
	else:
		print("{} {}".format("Changing:".rjust(lng), ("'" + line + "'")))
		print("{} {}".format("To:".rjust(lng), ("'" + line2 + "'")))
		print("-"*numl)
		os.rename(line, line2)

print("[ {} ] -- Done.".format(tms()))

