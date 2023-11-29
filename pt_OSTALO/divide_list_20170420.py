#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import random

# S = [25]

# Real example with 25 items:
L = [x for x in range(1,51)]
print("Un-shuffled:\n", L)

random.shuffle(L)
print("Shuffled:\n", L, "\n")


"""
# Test if less than 2 items:
n = len(S)

if n < 2:
	print("List", S, "has less than 2 items, and is therefore already sorted.")
	sys.exit()

# Divide
mid = n // 2

S1 = S[0:mid]
S2 = S[mid:n]

print("First half - S1:\n", S1, "\n")
print("Second half - S2:\n", S2)
"""

# MERGE SORT RECURSIVE SORTING:
def merge(S1, S2, S):
	i = j = 0
	while i + j < len(S):
		if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
			S[i+j] = S1[i]
			i += 1
		else:
			S[i+j] = S2[j]
			j += 1

def merge_sort(S):
	n = len(S)
	if n < 2:
		return
	# Divide
	mid = n // 2

	S1 = S[0:mid]
	S2 = S[mid:n]
	print(S1)
	print()
	merge_sort(S1)
	merge_sort(S2)
	merge(S1, S2, S)
	print(S)

merge_sort(L)





