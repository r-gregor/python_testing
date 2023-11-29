#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Print chars of names in triangle - each next line with one char more ...




Names in list as list of single chars and spaces.
Print each char in separate line, and add each nex char in next line.


"""

L = ['G', 'r', 'e', 'g', 'o', 'r', ' ', 'R', 'e', 'd', 'e', 'l', 'o', 'n', 'g', 'h', 'i', ',', 'T', 'a', 'd', 'e', 'j', 'a', ' ', 'M', 'a', 'l', 'i', ' ', 'R', 'e', 'd', 'e', 'l', 'o', 'n', 'g', 'h', 'i', ',', 'Z', 'a', 'l', 'a', ' ', 'R', 'e', 'd', 'e', 'l', 'o', 'n', 'g', 'h', 'i']

L1 = ""; i = 0
for i in range(1, len(L), 2):
	L1 = L1 + L[i-1] + L[i]
	print(L1)



