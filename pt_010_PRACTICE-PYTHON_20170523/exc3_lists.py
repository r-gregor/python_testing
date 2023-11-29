#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys
os.system('clear')


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

gr_NUM = input("Enter a number from 1 ro 89 (must be an integer!) __ ")

if ',' in gr_NUM:
	print("Float with comma")

	gr_INT, gr_DEC = gr_NUM.split(',')
	print("Integer part:", gr_INT)
	print("Decimal part - cut off:", gr_DEC)
	gr_NUM = gr_INT


elif '.' in gr_NUM:
	print("Float with dot")

	gr_INT, gr_DEC = gr_NUM.split('.')
	print("Integer part:", gr_INT)
	print("Decimal part - cut off:", gr_DEC)
	gr_NUM = gr_INT


gr_NUM = int(gr_NUM)

print()
print("Initial list a:", a)

# test if number entered is in the range of a list ...
print()
if gr_NUM <= 1:
	print("There are NO numbers smaller than 1!")
	exit()
elif gr_NUM > 98:
	print("Number is too big!")
	exit()

# in case float number is enterede ...
gr_NUM = int(gr_NUM)


print()
print("Excersize A: Print all numbers from list \"a\" that are smaller than", gr_NUM)

for N in a:
	if N < gr_NUM:
		print(N)


print()
print("Excersize B: Print a list \"B\" tha contains all numbers that are smaller than", gr_NUM)
B = []
for N in a:
	if N < gr_NUM:
		B.append(N)

print(B)




