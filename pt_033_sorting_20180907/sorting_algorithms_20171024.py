#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import time as t
import datetime

data = []
numd = 1000
gr_lst = 50

for N in range(0,numd):
	data.append(random.randint(1,numd))

print("Original list:", numd, "items (Showing last", gr_lst, "items)")
print(data[numd - gr_lst:])
print()


print("-"*110) # ----------------------------------------------------------------------------------------
print("A - INSERTION SORT")

def inssort(dt):
	startti = datetime.datetime.now()
	for i in range(1, len(dt)):
		currval = dt[i]
		pos = i
		while pos > 0 and dt[pos-1] > currval:
			dt[pos] = dt[pos-1]
			pos = pos - 1
		dt[pos] = currval

	endti = datetime.datetime.now()
	timedefi = endti - startti
	timedefmicroi = timedefi.microseconds

	print("Sorted list (Showing last", gr_lst, "items)")
	print(dt[numd - gr_lst:])
	print("Sorted in " + str(timedefmicroi/1000) + " miliseconds.")

inssort(data)

print("-"*110) # ----------------------------------------------------------------------------------------
print("A - BUBBLE SORT")

# copy values from original list to new list
bbdata = data

# sorting algorithm function
def bubbles(d):
	# record start time
	# starttb = datetime.datetime.now()
	starttb = t.time()
	
	data_b = d
	for i in range(0, len(data_b)):
		for j in range(0, len(data_b) - 1):
			if data_b[j] > data_b[j + 1]:
				tmpb = data_b[j]
				data_b[j] = data_b[j + 1]
				data_b[j+1] = tmpb
				
	# record end time
	# endtb = datetime.datetime.now()
	endtb = t.time()
	timedefb = endtb - starttb

	print("Sorted list (Showing last", gr_lst, "items)")
	print(data_b[numd - gr_lst:])
	print("Sorted in " + str(timedefb*1000) + " miliseconds.")

bubbles(bbdata)
