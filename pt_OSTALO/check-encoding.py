#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os
import codecs

gr_ARGNUM = len(sys.argv)
if gr_ARGNUM == 2:
	gr_ANS = sys.argv[1]
else:
	gr_ANS = input("Supply the filename: ")

if (os.path.isfile(gr_ANS)):
	gr_FAJL = gr_ANS
else:
	print("File \"" + str(gr_ANS) + "\"is NOT here!")
	print("You should BE IN directory with file to check,")
	print("or supply exact FULL /path/to/file ...")
	print("Leaving!")
	exit()



encodings = ['utf-8', 'windows-1252', 'windows-1250']
for e in encodings:
	try:
		fh = codecs.open(gr_FAJL, 'r', encoding=e)
		fh.readlines()
		fh.seek(0)
	except UnicodeDecodeError:
		print('... got unicode error with %s , trying different encoding' % e)
	else:
		print('opening the file with encoding:  %s ' % e)
		break
