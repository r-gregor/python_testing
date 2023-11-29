#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
filename:	   LLists_en_V3_20180425.py
description:	script that loads a csv data (list), file (';' as separator) and displays data in formated table.
				It creates a header out of first row, and checks if all data rows have the same number of
				fields.

created by:	 RgregoR
date:		   20180424

UPDATED 20180425:   - Get external csv data file as argument, check if it exists and asign it as a data source
					variable.
					- Set hs (spaces num between records in a row) according to chars num in hsd (chars num in
					delimiter between records in a row) even if hsd is ""!
					
UPDATED 20180426:   - Resolve utf-8 can't decode error: codecs -- ignore ...	 
					- delimiter = "," !! (as in normal csv files, spaces betveen ""!!)
					
'''

# IMPORTS
import sys
import csv
import sys
import os
import codecs # update 20180426

# FILE LOADING
# ------------------------------------------------------------------------------------------------------------
# UPDATED 20180425
# getting filenames ...
if len(sys.argv) != 2:
	print("ERROR: There should be exactly one filename as argumet to {}".format(sys.argv[0]))
	print("Leaving ... Bye!")	
	sys.exit(1)

def curdir(file):
	if '/' not in file:
		file = os.getcwd() + "/" + file
	return file


# Check if files exist:
FILE = sys.argv[1]
FILE = curdir(FILE)
	
if not os.path.isfile(FILE):
	print("ERROR: There is no {}".format(FILE))
	print("Leaving ... Bye!")
	sys.exit(1)
# ------------------------------------------------------------------------------------------------------------

# main data source
# UPDATED 20180425
data = FILE

# function: returns a list of row lists from main data
def olist(data):
	# update 20180426
	# with open(data) as f:
	with codecs.open(data, "r", encoding='utf-8', errors='ignore') as f:
		reader = csv.reader(f, delimiter=',')
		olist = []
		for row in reader:
			olist.append(row)
	return olist

# get data into "main" list
main_L = olist(data)

# replace empty elemts with "sign"
sign = '/'

for line in main_L:
	for index in range(len(line)):
		if line[index] == '':
			line[index] = sign
 

# add hs chars and hsd delimiter between columns
hsd = "|" # "", "|", " |", ...

if hsd != '':
	hs = 2
else:
	hs = 3


# header and the rest
header = main_L[0]
rest = main_L[1:]

# number of columns:
nc = len(header)


# for each column determin the longest word:
maxl = []
for index in range(nc):
	TL = []
	for el in main_L:
		TL.append(el[index])
		max_L = len(max(TL, key = len))
		
	maxl.append(max_L)

# line lengh len2 = sum of max lenghts
len2 = sum(maxl) + len(maxl)*(hs + len(hsd))	

def printl(lenl):
	'''
	print line length: lenl
	'''
	print("-"*lenl)

def h_print(header, col_n):
	'''
	print header
	'''
	for index in range(col_n):
		print(header[index].rjust(maxl[index] + hs) + hsd, end = '')
	print()
	
def r_print(list, col_n):
	'''
	print everything after the header
	'''
	for el in rest:
		for index in range(col_n):
			print(el[index].rjust(maxl[index] + hs) + hsd, end = '')
		print()
		
def L_print(list, col_n):
	'''
	print all lines --> separate list of parameter queue
	'''
	for el in list:
		for index in range(col_n):
			print(el[index].rjust(maxl[index] + hs) + hsd, end = '')
		print()

def t_test(list, c_num):
	for el in list:
		# test print
		# print(len(el), el)
		if len(el) != c_num:
			print("Records have different number of columns!")
			print("Exit!")
			sys.exit()

def print_T(printf, nc):
	printl(len2) # ---------------------------------------------
	# header
	h_print(header, nc)
	printl(len2) # ---------------------------------------------
	
	if printf == 'r_print':
		list = rest
		r_print(list, nc)
		printl(len2) # ---------------------------------------------
		
	elif printf == 'L_print':
		list = Mlist
		L_print(list, nc)
		printl(len2) # ---------------------------------------------

# test the list consistency
t_test(main_L, nc)

# print complete table
print_T('r_print', nc)


'''
# TEST
# ============================================================================================================
# print only those lines with pattern
test_ptn = ['Gregor', 'Spela']

Mlist = []
for el in main_L:
	for name in test_ptn:
		if name in el:
			Mlist.append(el)

			
print()
print('Table print for: "' + ' or '.join(test_ptn) + '"')
print_T('L_print', nc)
'''
