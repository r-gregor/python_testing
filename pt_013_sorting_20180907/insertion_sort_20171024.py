#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import time
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
	startt = datetime.datetime.now()
	for i in range(1, len(dt)):
		currval = dt[i]
		pos = i
		while pos > 0 and dt[pos-1] > currval:
			dt[pos] = dt[pos-1]
			pos = pos - 1
		dt[pos] = currval

	endt = datetime.datetime.now()
	timedef = endt - startt
	timedefmicro = timedef.microseconds

	print("Sorted list (Showing last", gr_lst, "items)")
	print(dt[numd - gr_lst:])
	print("Sorted in " + str(timedefmicro/1000) + " miliseconds.")

inssort(data)
