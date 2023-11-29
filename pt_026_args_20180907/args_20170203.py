#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os

# os.system('clear')

gr_ARGL = len(sys.argv)

if gr_ARGL != 2:
	print("Usage:\n" + sys.argv[0] + " + [exactly 1(one) argument]")
	sys.exit(1)

print("Number of arguments:", gr_ARGL - 1)
print("Your script", sys.argv[0], "took exactly one argument:", sys.argv[1])
print("Well done!")

