#! /usr/bin/env python3
# -*- coding: utf8 -*-

from operator import itemgetter as itmg

def crt(ch):
	''' draw a line of 80 "-" '''
	print(ch*80)


fjl = "TEXT.txt"
f = open(fjl)

L1 = f.readlines()
# outout: list of strings ['GREGOR,REDELONGHI,3,GOSPOD\n', 'TADEJA,REDELONGHI,1,GOSPA\n', ...
crt('-')
print("L1: outpud of file.readlines():")
print(L1)

# empty list to store list of tuples
L2 = []

for el in L1:
	# el.strip() --> remove leading endine newlines (el = string!)
	# tuple(el.strip().split(',')) --> create a list of elements delimited with ',' and turn it into tuple
	L2.append(tuple(el.strip().split(',')))
crt('-')
print("L2: list of tuples:")
print(L2)

# sorting on 3-rd field with lambda function
L3 = sorted(L2, key=lambda num: num[2])

crt('-')
print("L3 - sorted on 3-rd element with lamba function:")
for LN in L3:
	print(LN)
	
	
# sorting on 3-rd field with operator.itemgetter module
L4 = sorted(L2, key = itmg(2))
crt('-')
print("L4 - sorted on 3-rd element with operator.itemgetter module")
print("	 and print each element on it's own line:")
for LN in L4:
	print(LN)
	
	# print each element on it's oen line
	for el in LN:
		print(el)
		
	# Warning: number bigger than 3!
	if int(LN[2]) > 3:
		print("Num is bigger than 3!")			
	print("~~~~~~~~~~~~~~~~~~")

	

