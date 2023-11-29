#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import time
import datetime

data = []
numd = 1000
gr_lst = 50

# populate list with random numbers in range from 0 to numd (duplicates allowed)
for N in range(0,numd):
    data.append(random.randint(1,numd))

# display
print("Original list:", numd, "items (Showing last", gr_lst, "items)")
print(data[numd - gr_lst:])
print()

print("-"*110) # ----------------------------------------------------------------------------------------
print("A - BUBBLE SORT")

# copy values from original list to new list
bbdata = data

# sorting algorithm function
def bubbles(d):
    data_b = d
    
    # record start time
    startt = datetime.datetime.now()
        
    for i in range(0, len(data_b)):
        for j in range(0, len(data_b) - 1):
            if data_b[j] > data_b[j + 1]:
                tmpb = data_b[j]
                data_b[j] = data_b[j + 1]
                data_b[j+1] = tmpb
                
    # record end time
    endt = datetime.datetime.now()
    timedef = endt - startt
    timedefmicro = timedef.microseconds

    print("Sorted list (Showing last", gr_lst, "items)")
    print(data_b[numd - gr_lst:])
    print("Sorted in " + str(timedefmicro/1000) + " miliseconds.")

bubbles(bbdata)
