#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
for loop trough list test


for loop trough list test, if - break condition test

"""



L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

for i in range(len(L)):
	print(L[i])
	if i >= 5:
		print("Ouch!")
		print("reached " + str(i+1) + "-th element ...")
		break

