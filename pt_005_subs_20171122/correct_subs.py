#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# original: 20171120
# Script that corrects the srt file (shifts) times foeward or backward (+ / -)
# for a given time in seconds - provided by user, uniformly across whole file.
# When check for arguments (filename, time delay) are succesfull, ext module
# with correcting function is called. The output is another file.
# 
# 20171122: timing; backup copy of file (needed?)
# 

# IMPORTS
import time			 # only needed for backwards countown - test
import datetime as dt   # 20171122
import os
import sys
import shutil		   # copy file to backup
import m_correct_time

#FUNCTIONS
# function to create a backup of original srt file
def srtbekap(file_in):
	file_bkp = file_in + ".ORIGINAL"
	# test
	# print(file_bkp)

	if os.path.isfile(file_bkp):
		print("[ {} ] -- {} already exists!".format(tmstmp(), file_bkp))
	else:
		shutil.copyfile(file_in, file_bkp)

# timestamp function
def tmstmp():
	return dt.datetime.now().strftime('%Y%m%d_%H%M%S')

# Exeption message
msg = '''\
[ {0} ] -- Usage: {1} [ filename.srt] [time delay +- N in seconds]
[ {0} ] -- copy {1} to directory with filename.srt and run upper command! \
'''.format(tmstmp(), sys.argv[0])


# check if there are exactly two parameters to script
if len(sys.argv) < 3:
	print("[ {} ] -- Too few arguments".format(tmstmp()))
	print(msg)
	exit(1)

# argument 1: filename
file_in = sys.argv[1]

# argument 2: time difference in seconds (float)
t_d = sys.argv[2]

# Check if files exist:
if not os.path.isfile(file_in):
	print("[ {} ] -- There is no {}.".format(tmstmp(), file_in))
	print(msg)
	print("[ {} ] -- Exiting. Bye.".format(tmstmp()))
	sys.exit(1)
else:
	print("[ {} ] -- Correcting {} ...".format(tmstmp(), file_in))

# BEGIN THE REAL S**T:
startt = dt.datetime.now()


# Create a backup of srt file
srtbekap(file_in)

# output file
foutname, foutext = os.path.splitext(file_in)
file_out = foutname + "_crctd" + foutext
print("[ {} ] -- Output file: {} ...".format(tmstmp(), file_out))

# create a list of lines, strip trailing '\n' off
L1 = []
with open(file_in, 'r') as fin:
	for line in fin.readlines():
		if line != '\n':
			# if line not newline strip off trailing newline
			if '-->' not in line:
				L1.append(line.strip().split(','))
			else:
				L1.append(line.strip().split())

		else:
			L1.append(line.split())

# test
# print(L1)
# time.sleep(5)

# create output list: if not time string just copy it over from L1. If it is time string replace it with new
# time string from function ... 
L2 = []


for el in L1:
	if '-->' not in el:
		# if not time string: copy contents from L1
		L2.append(' '.join(el))
	else:
		# output of the correct function ...
		ct = m_correct_time.correct_time(el, t_d)
		L2.append(' '.join(ct.split()))

'''
# PRINT OUT - CHECK
# for each elemnt in a list print sigle line
for el in L2:
	if el == '':
		# if element newline, print with aditional newline striped off
		print(el.strip())
	else:
		print(el)
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

endt = dt.datetime.now()

difft = endt - startt
diffts = difft.total_seconds()

print("[ {} ] -- Done in {} seconds.".format(tmstmp(), diffts))

