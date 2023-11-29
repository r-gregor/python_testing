#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def addTwoNums(n1, n2):
	return n1 + n2


def subtractTwoNums(n1, n2):
	return n1 - n2

def multiplyTwoNums(n1, n2):
	return n1 * n2

def divideTwoNums(n1, n2):
	if n2 == 0:
		print("Cannot divide by 0!")
		# sys.exit(1)
	else:
		return n1 / n2

def fstToThePowerOfScnd(n1, n2):
	if n2 > 10:
		print("Exponent is to high (10 oe lower)")
		# sys.exit(1)
	else:
		return n1 ** n2

