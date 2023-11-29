#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys
import time as tt
import datetime as dt
from dateutil import relativedelta as rlt

# timestamp
def tms():
	return dt.datetime.now().strftime('%Y%m%d_%H%M%S')
	
# function for declaring today
def grf_today():
	return dt.date.today()

# MESSAGE:
print("[ {} ] -- Starting {} ...".format(tms(), sys.argv[0]))
print()


# storing today in var
gr_today = grf_today()

# end day (> today)
gr_endd = '2019-02-22'

# formatting end date
gr_enddf = dt.datetime.strptime(gr_endd, "%Y-%m-%d").date()

# calculatind difference between dates
gr_ddif = gr_enddf - gr_today

# printing ...
print("{:<14}{}".format('Today:', gr_today))
print("{:<14}{}".format('End Date:', gr_endd))
print("{:<14}{}".format('Days between:', gr_ddif.days)) # ".days" to display days only

# ============================================================================================================
print("\n" + "="*110) # separator

# insert end date2 in dd.mm.yyyy format
Ld = input("Enter Date2 in format: dd.mm.yyyy\n").strip().split('.')
gr_d = int(Ld[0])
gr_m = int(Ld[1])
gr_Y = int(Ld[2])
date2 = dt.date(gr_Y, gr_m, gr_d)
gr_difd = (date2 - gr_today).days # ".days" to display days only

print()
print("{:<23}{}".format('Today:', gr_today))
print("{:<23}{}".format('Date2:', date2))
print("{:<23}{} days.".format('From today till Date2:', gr_difd)) # ".days" to display days only

# ============================================================================================================
print("\n" + "="*110) # separator

#This will find the difference between the two dates
ddiff = rlt.relativedelta(date2, gr_today)

years = ddiff.years
months = ddiff.months
days = ddiff.days
# hours = ddiff.hours
# minutes = ddiff.minutes

print("Difference is {} year, {} months, {} days.".format(years, months, days))


# ============================================================================================================
print("\n" + "="*110) # separator

# external file
gr_fjl = 'test.txt'

# number of lines in a file
nlines = sum(1 for line in open('test.txt'))
print("Number of lines in '{}' is: {}".format(gr_fjl, nlines))

# ============================================================================================================
print("\n" + "="*110) # separator


def lastnum(fjl):
	L = []
	with open('test.txt', 'r') as f:
		for LN in f.readlines():
				L.append(LN.strip('\n'))
	return L[-1].split(';')[0]

gr_lstn = lastnum(gr_fjl)
print("ID of last line: {}".format(gr_lstn))

nY =  str(dt.date.today().year)
nnm = gr_lstn[4:]
nN = str(int(nnm) + 1).zfill(3)

gr_nwn = nY + nN
print("ID of NEW line: {}".format(gr_nwn))






