#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys
os.system('clear')

"""
ToDo:
Take two lists, say for example these two:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:
Randomly generate two lists to test this
Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print("List a =", a)
print("List b =", b)


def overlap():
	print()
	print("A - just print the common list elements ...")
	for NA in a:
		if NA in b:
			print(NA)
	
	
	print()
	print("B - create a list of common elements without duplicates ...")
	L = []
	for RA in a:
		if RA in b and RA not in L:
			L.append(RA)
	
	print(L)

overlap()


print()
print("And now with custom lists ...")

a = []
b = []

gr_a_bound = input("Enter the number between 10 and 20: __ ")
gr_b_bound = input("Enter the number between 7 and 15 __ ")

a = [N for N in range(1, int(gr_a_bound) + 1)]
b = [R * (2*R - 1) for R in range(1, int(gr_b_bound) + 1)]

print("List a =", a)
print("List b =", b)

overlap()

