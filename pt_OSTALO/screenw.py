#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import shutil

def screen_line(chr):
	'''draws a line of "chr" across the screen.
	   Add "import shutil" at the top of the script.
	   Supply "chr" parameter as string - between quotes.
	'''
	
	# get the columns (width) of terminal window (screen)
	gr_sw = shutil.get_terminal_size().columns
	
	# print a line oc chr across screen
	print(chr*gr_sw)


print("Printing a line across screen:")
screen_line("-")
screen_line(":")
screen_line("#")

sl = screen_line("~")
sl
