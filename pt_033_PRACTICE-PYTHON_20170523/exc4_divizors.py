#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import os
os.system('clear')

print("Excersize 4: print all numbers thar are divizors of a given number")
print()
gr_NUM = int(input("Enter the positive integer number: __ "))
for N in range(1, gr_NUM):
	if gr_NUM % N == 0:
		print(N)

