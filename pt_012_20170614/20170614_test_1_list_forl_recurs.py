#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys

# CLEAR the screen:
gr_cl = os.system('clear')

def gr_ln(n):
	print("-" * n)

gr_cl

gr_ln(70) # -------------------------------------
print("Calculating the sum of all elements (SAE) in the list")

# initial ORDERED list
L0 = [1, 3, 5, 7, 9]
print("Initial list L0:", (L0))

gr_ln(70) # -------------------------------------
# sum of elements (SAE) - first method:
print("First method --> (SAE1) For loop:")
def list_sum_1(num_list):
	the_sum = 0
	for i in L0:
		the_sum = the_sum + i
	return the_sum

print("SAE1 = ", list_sum_1(L0))

gr_ln(70) # -------------------------------------

# sum of elements (SAE) - second method:
print("Second method --> (SAE2) Recursion:")
def list_sum_2(num_list):
	if len(num_list) == 1:
		the_sum2 = num_list[0]
		return the_sum2
	else:
		the_sum2 = num_list[0] + list_sum_2(num_list[1:])
		return the_sum2

print("SAE2 =", list_sum_2(L0))

gr_ln(70) # -------------------------------------


