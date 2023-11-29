#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def fibn(n):
	if n <= 1: return n
	else: return fibn(n-1) + fibn(n-2)

def handle(st):
	n = int(st)

	output = []
	for i in range(1, n):
		output.append(str(fibn(i)))
	print(', '.join(output))

gr_NUM = input("Insert sequence number for Fibonaaci series (no bigger than 20) __ ")

if not gr_NUM:
	gr_NUM = 20

handle(gr_NUM)

