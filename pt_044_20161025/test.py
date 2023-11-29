
#! /usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import sys

NUM=1

for ENTR in sys.stdin.readlines():
	ENTR=ENTR.strip()
	print("Line " + str(NUM) + " is: ", ENTR)
	NUM +=1
	

