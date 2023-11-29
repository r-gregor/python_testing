#! /usr/bin/env python3
# -*- coding: utf8 -*-

# vars
print('01: fajl = "AMD.txt"')
fajl = "AMD.txt"


# open f
print('02: Opening fajl ...')
fj = open(fajl, 'rt')

# create a list of lines
print('03: fl = list(fj) ... creating a list fl of lines from file')
fl = list(fj)

# print lines 44 to 54
print('''
04: Print lines 44 to 54:
	for ln in range(44,54):
		print(fl[ln], end='')

RESULT:
''')

for ln in range(44,54):
	print(fl[ln], end='')



print('''
05: READS WHOLE FILE IN AND CREATES A LIST OF ALL WORDS
	print('wrds = fj.read().split()')
''')
	
# READS WHOLE FILE IN AND CREATES A LIST OF ALL WORDS
print('wrds = fj.read().split()')

# goto start of the file
fj.seek(0)

# create a list of all words
# reads lines into strings
# splits words from string into list of words
wrds = fj.read().split()

fj.close()  # closing file

print(wrds)

print()
# find all "driver" words and count them

print('06: Finding all "driver" words and counting them ...')
wrd = 'driver'
if wrd in wrds:
	cnt = 1
	for ww in wrds:
		if ww == wrd:
			print('"' + wrd + '"', 'nr:', cnt)
			cnt +=1

  

	