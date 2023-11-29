#! /usr/bin/env python3
# -*- coding: utf-8 -*-



gr_NUM = int(input("Enter the number to calculate the factorial: ") or "5")

def fact(n):
	if n == 0:
		return 1
	else:
		return n * fact(n - 1)

print("Factorial of num", gr_NUM,  "is:", fact(gr_NUM))

