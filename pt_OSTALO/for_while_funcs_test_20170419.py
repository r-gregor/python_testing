#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
for, while loops, function ... tests


for, while loops, function ... tests


"""

## for, while loops, function ... tests
import os		# os module for clearing the screen ...
os.system('clear')

# List S:
S = [0, 1, 2, 3, 4, 6, 7, 8, 5.2, 9, 10, 16, 22, 5.1, 33]

print("****************************************")
print("* for, while loops, function ... tests *")
print("****************************************" + "\n")

# CONTEXT-1: (while loop)
# find index j of a number in a list S which gives: j * 3 = 15:
j = 0			# set the starting index
F = 15			# set the product
R = False		# set the control index for the final if --> print if no element found
while j < len(S):
	P = S[j] * 3
	if P == F:
		print("Item number " + str(j) + ": ", S[j], "multiplied by 3 is:", P)  
		R = True	# since element is found --> cntrol index R=True, so no finl print
		break		# break the loop and finish CONTEXT-1
	j += 1
if R == False:
	print("No argument multiplied by 3 gives", F)

"-------------------------------------------------------------------------------------------------------------"
# CONTEXT-2: (function)
def find_pr(lList, vVal):		# def a function
	"""function that takes the list object and product value as arguments and returns the product if right
	index in list is found, otherwise return -1"""
	j = 0
	while j < len(lList):
		P = lList[j] * 3
		if P == vVal:		# if index found
			return P	# return result
			break		# break out of loop
		j += 1			# increase index
	return -1			# return -1 if no indes found

print()
print("Serch through a list of products with function:")
print("===============================================")
for PRD in (15, 4, 66, 44, 99, 2, 103):					# run function for these products
	print("Searching list item that multiplied by 3 gives:", PRD)
	expr = find_pr(S, PRD)
	if expr != -1:
		print("The product of an element", int(PRD/3), "in list and 3 is:", expr, "\n")
	else:
		print("*** No luck there. No element multiplied by 3 gives:", PRD, "***\n")

"END"


