#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys
import stack

numb1 = int(input("Insert integer I > 0:  ... "))
base1 = int(input("Input base: 2, 10 or 16: ... "))

if numb1 <= 0:
	print("Wrong input!")
	sys.exit(1)
 
if base1 not in [2, 10, 16]:
	print("Wrong input!")
	sys.exit(2)


s = stack.Stack()

def to_str(n, base):
	convert_string = "0123456789ABCDEF"
	while n > 0:
		if n < base:
			s.push(convert_string[n])
		else:
			s.push(convert_string[n % base])
		
		n = n // base
	
	res = ""

	while not s.is_empty():
		res = res + str(s.pop())

	return res

print(to_str(numb1, base1))

