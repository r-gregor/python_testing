#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# V2_20180116;

import os, sys
import time as tt
import datetime as dt
from dateutil import relativedelta as rlt

# colors
import my_textcolors as myc
ccyn = myc.c_CYAN
bred = myc.b_REDB
bgreen = myc.b_GREENB
norm = myc.NN


# FUNCTIONS ==================================================================================================
def add_diff(my_list0):
	'''
	function that reads start and end dates in from initial list, calculates the difference in days
	and returns a new base list with added date difference as field[4]
	
	'''
	TL0 = []
	def grf_today():
		return dt.date.today()
  
	# function for declaring today
	def grf_today():
		return dt.date.today()
	
	gr_today = grf_today()
	
	for EL in my_list0:
		ELL = EL.split(';')
		endt = ELL[3]
		endtf = dt.datetime.strptime(endt, "%Y-%m-%d").date()
		tdif = (endtf - gr_today).days
		NEWL = ELL[0] +';'+ ELL[1] +';'+ ELL[2] +';'+ ELL[3] +';'+ str(tdif) +';'+ ELL[4]
		TL0.append(NEWL)
	return(TL0)

def readf_in(gr_file):
	'''
	function that reads lines from ext file into initial list
	'''
	L0 = []
	with open(gr_file ,'r') as f:
		for LN in f.readlines():
			L0.append(LN.strip('\n'))
	return(L0)

# 1 - read in file
LA = readf_in('AAA.txt')

# 2 - add days diff to base list
L1 = add_diff(LA)


def print_table(my_list):
	'''
	function that displays a table from a list created by external command
	that calls this script as a module.
	'''
	# number of dashes in a dividr line
	n_hyp = 80

	# table header
	print("="*n_hyp)
	print("{} | {} | {} | {} | {} | {} ".format("ID".ljust(7), "W", "START".ljust(10), "END".ljust(10), "DIFF".ljust(11), "WHAT"))
	print("-"*n_hyp)
	
	
	# table lines
	for EL in my_list:
		ELL = EL.split(';')
		tdif = int(ELL[4])
				
		def cmd1():
			print("{} | {} | {} | {} | {} | {} ".format(ELL[0], ELL[1], ELL[2], ELL[3], (ELL[4] + " day(s)").ljust(11), ELL[5]))
		
		def cmdr():
			print("{}{} | {} | {} | {} | {} | {}{} ".format(bred, ELL[0], ELL[1], ELL[2], ELL[3], (ELL[4] + " day(s)").ljust(11), ELL[5], norm))
		
		def cmdg():
			print("{}{} | {} | {} | {} | {} | {}{} ".format(bgreen, ELL[0], ELL[1], ELL[2], ELL[3], (ELL[4] + " day(s)").ljust(11), ELL[5], norm))
			
		def cmdd():
			print("{}{} | {} | {} | {} | {} | {}{} ".format(ccyn, ELL[0], ELL[1], ELL[2], ELL[3], (ELL[4] + " day(s)").ljust(11), ELL[5], norm))
		
		
		if tdif < 0:
			cmdd()
		elif tdif <= 7:
			cmdr()
		elif 7 < tdif < 14:
			cmdg()
		else:		
			cmd1()

	# table footer
	print("="*n_hyp)
	print("[{}{}{}] - 7 or less days, [{}{}{}] - 8 to 14 days, [no color] - more than 14 days". format(bred, "   ", norm, bgreen, "   ", norm))
	print("S - Spela, M - Mark, Z - Zala, T - Tadeja, G - Gregor")
	
	
# print full base table
def print_full_table():
	print_table(L1)

	
def more_days(tdif):
	'''
	function that dislays all entries from list L, where days diff is bigger than argument
	'''
	print()
	dy = tdif
	print("All entries which have Tdiff > {}".format(dy))
	L3 = []
	for el3 in L1:
		diff = el3.split(';')[4]
		if abs(int(diff)) > dy:
			L3.append(el3)
	print_table(L3)

	
def less_days(tdif):
	'''
	function that dislays all entries from list L, where days diff is smaller than argument
	'''
	print()
	dy = tdif
	print("All entries which have Tdiff < {}".format(dy))
	L3 = []
	for el3 in L1:
		diff = el3.split(';')[4]
		if abs(int(diff)) < dy:
			L3.append(el3)
	print_table(L3)
	
	
def is_not_in(patt):
	'''
	function that dislays all entries from list L, where argument is NOT in the string
	'''
	print()
	print("All entries where '{}' is NOT in".format(patt))
	L2 = []
	for el2 in L1:
		if str(patt) not in el2:
			L2.append(el2)
	print_table(L2)
	
	
def is_in(patt):
	'''
	function that dislays all entries from list L, where argument is in the string
	'''
	print()
	print("All entries where '{}' IS in".format(patt))
	L2 = []
	for el2 in L1:
		if str(patt) in el2:
			L2.append(el2)
	print_table(L2)


