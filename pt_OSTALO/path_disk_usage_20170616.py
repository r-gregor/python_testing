#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os

def disk_usage(path):
	"""
	Return the number of bytes used by a file/folder and any descendents.
	"""
	
	total = os.path.getsize(path)					   # account for direct usage
	if os.path.isdir(path):							 # if this is a directory,
		for filename in os.listdir(path):			   # then for each child:
			childpath = os.path.join(path, filename)	# compose full path to child
			total += disk_usage(childpath)			  # add child’s usage to total
	
	print( "{0:<10}".format(total), path)				 # descriptive output (optional)
	return total

### pth = "/home/gregor.redelonghi/bin"
pth = "/home/gregor.redelonghi/majstaf/coding/PYTHON-en/PYTHON-en_testing"

DU = disk_usage(pth)
print("\nTOTAL disk usage for ALL files in path: ", DU)
