#! /usr/bin/env python3

# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def show_time(rdd):
	'''
	function that prints time difference for each time segment:
		- years
		- months
		- days
		- hours
	'''
	for time in 'years', 'months', 'days', 'hours', 'minutes':
		dlt = eval(str(rdd) + "." + time)
		if dlt != 0:
			print(time + ": " + str(dlt))
		


old_D = datetime(1968, 2, 22, 18, 10)
fut_D = datetime(2028, 2, 22, 20, 0)
now_D = datetime.today()


old_D_date = old_D.strftime("%d.%m.%Y")
fut_D_date = fut_D.strftime("%d.%m.%Y")
now_D_date = now_D.strftime("%d.%m.%Y")

print("My birthdate:", old_D_date)

# time difference today : BD
rdd_today = relativedelta(now_D, old_D)

# test print
# print(rdd_today)

print("Difference from now " + now_D_date + " back to my BD: " + old_D_date)
show_time(rdd_today)

print("-"*80) # ----------------------------------------------

# time difference future : BD
rdd_fut = relativedelta(fut_D, old_D)

# test print
# print(rdd_fut)
show_time(rdd_fut)	

print("-"*80) # ----------------------------------------------	   
		
mydate = input("Insert date in format YYYY-mm-dd: ")
my_D = datetime.strptime(mydate, "%Y-%m-%d")
rdd_myd = relativedelta(my_D, old_D)
show_time(rdd_myd)

