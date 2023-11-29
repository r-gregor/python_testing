#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import time


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

# print list L1 (check) and wait 5 seconds ...
print(L1)
print("\nWaiting 10 seconds to proceed ...")

# countdown - replace
for T in range(9,0,-1):
	print(" " + str(T), end= "\r")
	time.sleep(1)

# ------------------------------------------------------------------------------------------------------------
# PRINT OUT - CHECK
# for each elemnt in a list print sigle line
for el in L1:
	if el == '\n':
		# if element newline, print with aditional newline striped off
		print(el.strip())
	else:
		print(el)
# ------------------------------------------------------------------------------------------------------------


'''
# ### FUNCTION THAT CORRECTS TIMES <--
# RETURNS NEW LIST L2:
L2 = L1[:]  # for now just copy the list L1 to L2:


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
