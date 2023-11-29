#! /usr/bin/env python3
# -*- coding: utf-8 -*-

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

# timestamp
def tms():
	return dt.datetime.now().strftime('%Y%m%d_%H%M%S')
	
# function for declaring today
def grf_today():
	return dt.date.today()

# CLEAR THE SCREEN	
os.system('clear')

# MESSAGE:
print()
print("[ {} ] -- Starting {} ...".format(tms(), sys.argv[0]))


L = []
with open('test.txt' ,'r') as f:
	for LN in f.readlines():
		L.append(LN.strip('\n'))
# TEST
# print(L)

gr_today = grf_today()
n_hyp = 80

print("="*n_hyp)
print("{} | {} | {} | {} | {} | {} ".format("ID".ljust(7), "W".ljust(3), "START".ljust(10), "END".ljust(10), "DIFF".ljust(10), "WHAT"))
print("-"*n_hyp)

for EL in L:
	ELL = EL.split(';')
	endt = EL.split(';')[3]
	endtf = dt.datetime.strptime(endt, "%Y-%m-%d").date()
	tdif = (endtf - gr_today).days
	# print("-"*110)
	def cmd1():
		print("{} | {} | {} | {} | {} | {} ".format(ELL[0], ELL[1].ljust(3), ELL[2], ELL[3], (str(tdif) + " day(s)").ljust(10), ELL[4]))
	
	def cmdr():
		print("{}{} | {} | {} | {} | {} | {}{} ".format(bred, ELL[0], ELL[1].ljust(3), ELL[2], ELL[3], (str(tdif) + " day(s)").ljust(10), ELL[4], norm))
	
	def cmdg():
		print("{}{} | {} | {} | {} | {} | {}{} ".format(bgreen, ELL[0], ELL[1].ljust(3), ELL[2], ELL[3], (str(tdif) + " day(s)").ljust(10), ELL[4], norm))
		
	def cmdd():
		print("{}{} | {} | {} | {} | {} | {}{} ".format(ccyn, ELL[0], ELL[1].ljust(3), ELL[2], ELL[3], (str(tdif) + " day(s)").ljust(10), ELL[4], norm))
	
	
	if tdif < 0:
		cmdd()
	elif tdif <= 7:
		cmdr()
	elif 7 < tdif < 14:
		cmdg()
	else:		
		cmd1()

print("="*n_hyp)
print("[{}{}{}] - 7 or less days, [{}{}{}] - 8 to 14 days, [no color] - more than 14 days". format(bred, "   ", norm, bgreen, "   ", norm))
print("S - Spela, M - Mark, Z - Zala, T - Tadeja, G - Gregor")
