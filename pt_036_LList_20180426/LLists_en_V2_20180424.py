#! /usr/bin/env python3

# IMPORTS
import sys
import csv

# main data source
data = 'data.csv'

# function: returns a list of row lists from main data
def olist(data):
	with open(data) as f:
		reader = csv.reader(f, delimiter=';')
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
 

# add hs chars between columns
hs = 2

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
len2 = sum(maxl) + len(maxl)*(hs + 2)	
	
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
		print(header[index].rjust(maxl[index] + hs) + " |", end = '')
	print()
	
def r_print(list, col_n):
	'''
	print everything after the header
	'''
	for el in rest:
		for index in range(col_n):
			print(el[index].rjust(maxl[index] + hs) + " |", end = '')
		print()
		
def L_print(list, col_n):
	'''
	print all lines --> separate list of parameter queue
	'''
	for el in list:
		for index in range(col_n):
			print(el[index].rjust(maxl[index] + hs) + " |", end = '')
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



# ============================================================================================================
# print only those lines with pattern
test_ptn = ['Gregor', 'Marko', 'Spela', 'Ragnar']

Mlist = []
for el in main_L:
	for name in test_ptn:
		if name in el:
			Mlist.append(el)

			
print()
print('Table print for: "' + ' or '.join(test_ptn) + '"')
print_T('L_print', nc)
