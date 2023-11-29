#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import time
import datetime

data = []
numd = 2000
gr_lst = 50



def time_disp(sortm):
	startt = datetime.datetime.now()				

	# ACTION
	sortm

	endt = datetime.datetime.now()
	timedef = endt - startt
	timedefmicro = timedef.microseconds

	print("Sorted list (Showing last", gr_lst, "items)")
	print(data[numd - gr_lst:])
	print("Sorted in " + str(timedefmicro/1000) + " miliseconds.")


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
time_disp(bubble_sort(data))



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
time_disp(insertion_sort(data))



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
time_disp(merge_sort(data))


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


time_disp(quick_sort(data))

print("-"*110) # ----------------------------------------------------------------------------------------
print("A - HEAP SORT")

import heapq

def heap_sort(items):
	""" Implementation of heap sort """
	heapq.heapify(items)
	items[:] = [heapq.heappop(items) for i in range(len(items))]

time_disp(heap_sort(data))



			
			