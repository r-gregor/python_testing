# imports
import sys
import time

# globals
gr_author = 'RgregoR'
gr_date = '2017'


def line(c, n):
	print(c*n)

def tmpstmp():
	return time.strftime('%Y%m%d_%H%M%S')

def currtm():
	return time.strftime('%H%M%S')

def currdt():
	return time.strftime('%Y%m%d')

def info():
	print("{}{}".format("Scriptname:".ljust(15),sys.argv[0]))
	print("{}{}".format("Author:".ljust(15), gr_author))
	print("{}{}".format("Date:".ljust(15), gr_date))

