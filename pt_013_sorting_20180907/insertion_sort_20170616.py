#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# ORIGINAL:
# insertion sort
L = [54, 2, 59, 4, 103, 1]
print("Initial list L =", L)

def insertion_sort(s):
	for i in range(1, len(s)):
		val = s[i]
		j = i - 1
		while (j >= 0) and (s[j] > val):
			s[j+1] = s[j]
			j = j - 1
		s[j+1] = val

	return L

LS = insertion_sort(L)
print("Sorted list LS =", LS)
"""


# insertion sort
L = [54, 2, 59, 4, 103, 1]
print("Initial list L =", L)

def insertion_sort(s):
	for i in range(1, len(s)):
		print("-"*78)
		val = s[i]
		j = i - 1
		print("i =", i)
		print("j = i - 1 =", j)
		print("val = s[i] = S["+str(i)+"] =", val)
		
		while (j >= 0) and (s[j] > val):
			s[j+1] = s[j]
			print("s[j+1] = s[j] --> s["+str(j+1)+"] = s["+str(j)+"] =", s[j+1])
			 
			j = j - 1
			print("j = j - 1 =", j)

		s[j+1] = val
		print("s[j+1] = s["+str(j+1)+"] = val =", val)

	return L

LS = insertion_sort(L)
print("Sorted list LS =", LS)

