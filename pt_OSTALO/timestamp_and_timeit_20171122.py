#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# #######################################
#
# 20171122: timeit and timestamp
# all print expressions are in format:
#   [ yyyymmdd_HHMMSS ] -- text ... 
#
# #######################################

# import time		   -- only for time.sleep(N), and such ...
import datetime as dtt

def tmstmp():
	return dtt.datetime.now().strftime('%Y%m%d_%H%M%S')

print("[ {} ] --  START ...".format(tmstmp()))

# BEGIN THE REAL S**T:

# start timing main program
startt = dtt.datetime.now()

# main code ---------------------------------------------------------

'''
REAL CODE ...

'''

# main code ---------------------------------------------------------

# end timing main program
endt = dtt.datetime.now()

# calculating time difference in seconds (float)
difft = endt - startt
diffts = difft.total_seconds()

# print out time difference ...
print("[ {} ] -- Done in {} seconds.".format(tmstmp(), diffts))

