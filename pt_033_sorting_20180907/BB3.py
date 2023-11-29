#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import time as t
import datetime

data = []
numd = 10000
gr_lst = 50



def time_disp():
	print("Start time =", startt)
	print("End time =", endt)
	timedef = endt - startt
	print("Time difference in seconds is:", timedef)
	timedefmili = timedef *1000

	print("Sorted list (Showing last", gr_lst, "items)")
	print(data[numd - gr_lst:])
	print("Sorted in", timedefmili, "miliseconds.")


# populate list with random numbers in range from 0 to numd (duplicates allowed)
for N in range(0,numd):
	data.append(random.randint(1,numd))

# display
print("Original list:", numd, "items (Showing last", gr_lst, "items)")
print(data[numd - gr_lst:])
print()


print("-"*110) # ----------------------------------------------------------------------------------------
print("A - BUBBLE SORT")

def bubble_sort(items):
	""" Implementation of bubble sort """
	
	
	for i in range(len(items)):
		for j in range(len(items)-1-i):
			if items[j] > items[j+1]:
				items[j], items[j+1] = items[j+1], items[j]	 # Swap!



# ACTION	
startt = t.time()
bubble_sort(data)
endt = t.time()

time_disp()





print("-"*110) # ----------------------------------------------------------------------------------------
print("A - INSERTION SORT")

def insertion_sort(items):
	""" Implementation of insertion sort """
		
	for i in range(1, len(items)):
		j = i
		while j > 0 and items[j] < items[j-1]:
			items[j], items[j-1] = items[j-1], items[j]
			j -= 1


# ACTION	
startt = t.time()
insertion_sort(data)
endt = t.time()

time_disp()



print("-"*110) # ----------------------------------------------------------------------------------------
print("A - MERGE SORT")

def merge_sort(items):
	""" Implementation of mergesort """

	
	if len(items) > 1:

		mid = int(len(items) / 2)		# Determine the midpoint and split
		left = items[0:mid]
		right = items[mid:]

		merge_sort(left)			# Sort left list in-place
		merge_sort(right)		   # Sort right list in-place

		l, r = 0, 0
		for i in range(len(items)):	 # Merging the left and right list

			lval = left[l] if l < len(left) else None
			rval = right[r] if r < len(right) else None

			if (lval and rval and lval < rval) or rval is None:
				items[i] = lval
				l += 1
			elif (lval and rval and lval >= rval) or lval is None:
				items[i] = rval
				r += 1
			else:
				raise Exception('Could not merge, sub arrays sizes do not match the main array')


# ACTION
startt = t.time()
merge_sort(data)
endt = t.time()

time_disp()



print("-"*110) # ----------------------------------------------------------------------------------------
print("A - QUICK SORT")


def quick_sort(items):
	""" Implementation of quick sort """
	if len(items) > 1:
		pivot_index = int(len(items) / 2)
		smaller_items = []
		larger_items = []

		for i, val in enumerate(items):
			if i != pivot_index:
				if val < items[pivot_index]:
					smaller_items.append(val)
				else:
					larger_items.append(val)

		quick_sort(smaller_items)
		quick_sort(larger_items)
		items[:] = smaller_items + [items[pivot_index]] + larger_items


startt = t.time()
quick_sort(data)
endt = t.time()

time_disp()



print("-"*110) # ----------------------------------------------------------------------------------------
print("A - HEAP SORT")

import heapq

def heap_sort(items):
	""" Implementation of heap sort """
	heapq.heapify(items)
	items[:] = [heapq.heappop(items) for i in range(len(items))]

startt = t.time()
heap_sort(data)
endt = t.time()

time_disp()


