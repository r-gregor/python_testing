#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys

L1 = []
L2 = []

for root1, dirs1, files1 in os.walk('DIR1'):
	L1.extend(files1)
	break   # to stop desending to subdirs

for root2, dirs2, files1 in os.walk('DIR2'):
	L2.extend(files1)
	break	# to stop desending to subdirs

print("Test:")
print("List of files in DIR1:", L1)
print("List of files in DIR12", L2)
print()

for F in L1:
	if F in L2:
		print("File", F, "is duplicated (in both dirs)!")

