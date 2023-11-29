#! /usr/bin/python
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

import os.path

name1="youtubedl_list-of-sites.txt"
name2="wrong_youtubedl_list-of-sites.txt"

if os.path.isfile(name1):
	empty=" "
	print("Yes!\n\t%50s exists!" % name1)
else:
	print("Sorry! No luck There. Bye.\n")

if os.path.isfile(name2):
	print("Yes! ", name2 ," exists!\n")
else:
	print("Sorry! No luck There. There is no ",name2," file. Bye.\n")



