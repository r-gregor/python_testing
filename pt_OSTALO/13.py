#! /usr/bin/env python3
# -*- coding: utf-8 -*-


print("Numbers from 1000 to 2000 that are divisible by 13")

def Int13Multiplicators1():
	nums = []
	for NUM in range(1000, 2001):
		if NUM % 3 == 0:
			nums.append(NUM)
	return nums

def Str13Multiplicators1():
	nums = []
	for NUM in range(1000, 2001):
		if NUM % 3 == 0:
			nums.append(str(NUM))
	return nums




print("\n" + "Results added to list as integers:")
print(", ".join([str(num) for num in Int13Multiplicators1()]))
print("Done.")

print("\n" + "Results added to list as strings:")
print(", ".join([num for num in Str13Multiplicators1()]))
print("Done.")
