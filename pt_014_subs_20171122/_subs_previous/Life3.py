#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import time	 # only needed for backwards countown - test


file_in = 'Life.2017.720p.BluRay.x264-YTS.AG.srt'
file_out = 'Life_corrected.srt'

# create a list of lines, strip trailing '\n' off
L1 = []
with open(file_in, 'r') as fin:
	for line in fin.readlines():
		if line != '\n':
			# if line not newline strip off trailing newline
			L1.append(line.strip())
		else:
			L1.append(line)

# test
# print(L1)

# create output list: if not time string just copy it over from L1. If it is time string replace it with new
# time string from function ... current: just replace it with test new time string ...
L2 = []

# CHANGE: OUTPUT OF REAL CORRECTION FUNCTION OR CLASS:
NL = 0
for el in L1:
	if '-->' not in el:
		# if not time string: copy contents from L1
		L2.append(el)
	else:
		# current: test new time string -- later output of the correct function ...
		NL += 1
		L2.append('{}: changed_start_time --> changed_end_time'. format(NL))

# test
# print list L2 (check) and wait 5 seconds ...
print(L2)
print("\nWaiting 10 seconds to proceed ...")

# countdown - replace
for T in range(9,0,-1):
	print(" " + str(T), end= "\r")
	time.sleep(1)

# ------------------------------------------------------------------------------------------------------------
# PRINT OUT - CHECK
# for each elemnt in a list print sigle line
for el in L2:
	if el == '\n':
		# if element newline, print with aditional newline striped off
		print(el.strip())
	else:
		print(el)
# ------------------------------------------------------------------------------------------------------------


'''
# ACTUAL WRITE TO OUTPUT FILE !!! ----------------------------------------------------------------------------
with open(file_out, 'w') as fout:
	# for each elemnt in a list print sigle line
	for el in L2:
		if el == '\n':
			# if element newline, print with aditional newline striped off
			fout.write((el.strip()))
			fout.write('\n') # NEEDED OR ELSE: SINGLE STRING
		else:
			fout.write(el)
			fout.write('\n') # NEEDED OR ELSE: SINGLE STRING
'''
