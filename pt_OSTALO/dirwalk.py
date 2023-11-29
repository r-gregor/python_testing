#! /usr/bin/env python3
# -*- coding: utf-8 -*-


import os

fileslist = []


for root, dirs, files in os.walk("."):
	for name in dirs:							   # files or dirs
		full_path = os.path.join(root, name)
		fileslist.append(os.path.abspath(full_path))


for item in fileslist:
	print(item)


