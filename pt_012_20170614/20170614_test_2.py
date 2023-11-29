#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys

# CLEAR the screen:
gr_cl = os.system('clear')

def to_str(n, base):
	convert_string = "0123456789ABCDEF"
	if n < base:
		return convert_string[n]
	else:
		return to_str(n // base, base) + convert_string[n % base]

print("to_str(93, 16):", to_str(93, 16))

print("to_str(765, 10):", to_str(765, 10))

print("to_str(25, 2):", to_str(25, 2))

