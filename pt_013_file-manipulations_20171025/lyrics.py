#! /usr/bin/env python3
# -*- coding: utf-8 -*-

fajl = 'lyrics2.txt'
L = []						  # initialize empty list

f = open(fajl, 'rt')

f.seek(0)					   # move pointer to start of file (just in case)

for LN in f.readlines():		# for each line in file
	for W in LN.split(' '):	 # for each Word in line
		L.append(W)			 # append Word to list L

f.close()					   # CLOSE file!

print(L)

print()
print('The number of words in list L is:', len(L))
