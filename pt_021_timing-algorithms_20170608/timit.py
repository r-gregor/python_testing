#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import time

def sum_of_n(n):
	start = time.time()
	
	the_sum = 0
	for i in range(1, n+1):
		the_sum += i

	end = time.time()
	return the_sum, end - start


for j in range (10):
	gr_NUM, gr_SCNDS = sum_of_n(100000)
	# print("The sum is %d, and it took %10.7f sedconds to calculate it" % sum_of_n(100000))
	### print("The sum is {0:d}, and it took {1:10.7f} sedconds to calculate it" .format(sum_of_n(100000))) # does not work???
	
	print("The sum is {0:d}, and it took {1:10.7f} sedconds to calculate it" .format(gr_NUM, gr_SCNDS))

# RECURSIVE FUCTION FOR GCD (greatest common divisor)
def GCD(a, b):
	if b == 0:
		return a
	else:
		return GCD(b, a % b)

a = 416
b = 108

print("Gratest common divizor of numbers", a, "and", b, "is:", GCD(a, b))


