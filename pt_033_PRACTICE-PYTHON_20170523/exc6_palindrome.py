#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys
os.system('clear')

"""
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
"""

gr_NM = str(input("Enter the name ___ "))
gr_NMU1 = gr_NM.upper()			 # convert all letters to uppercase
gr_NMU = gr_NMU1.replace(' ','')	# remove all spaces (sentences, or full names)

L1 = list(gr_NMU)
L2 = []
for i in range(len(L1)):
	 L2.append(L1[-(i+1)])

print("With the lists ...")
print("The lists are:")
print(L1)
print(L2)

if L1 == L2:
	print("Name " + gr_NMU + " is a Palindrome ...")
	print(''.join(L1), " is the same as ", ''.join(L2))
else:
	print("Nope. The name", gr_NMU, "is NOT the Palindrome.")

print()
print("Without the lists ...")
gr_UMN = gr_NMU[::-1]
if  gr_NMU == gr_UMN:
	print("Name " + gr_NMU + " is a Palindrome ...")
	print(gr_NMU, " is the same as ", gr_UMN)
else:
	print("Nope. The name", gr_NMU, "is NOT the Palindrome.")



