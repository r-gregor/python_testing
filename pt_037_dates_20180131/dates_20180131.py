#! /usr/bin/env python3

import sys
DTS = '2018-01-31'

# NOT GOOD!
# yr = DTS[:4]
# mnt = DTS[5:7]
# dy = DTS[-2:]
# what if len(yr) < 4 ?? --> DTS.split():

yr, mnt, dy = DTS.split('-')


def checkd(y, m ,d):
	if (
	int(y) not in range(1,2223)
	or
	len(y) > 4
	):
		print('Year {}: out of range 1000 - 2222'.format(y))
		sys.exit()
	
	if (
	int(m) not in range(1,13)
	or
	len(m) > 2
	):
		print('Month {}: out of range 1 - 12'.format(m))
		sys.exit()

	if (
	int(d) not in range(1,32)
	or
	len(d) > 2
	):
		print('Day {}: out of range 1 - 31'.format(d))
		sys.exit()
		

# check date format		
checkd(yr, mnt, dy)   
   
 


STDT = "{}.{}.{}".format(dy, mnt, yr)
print(STDT)
