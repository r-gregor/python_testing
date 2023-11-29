#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os

def draw_line(tick_length, tick_label='' ):
	"""draw one line with given tick length (followed by optional label)."""
	line = '-' * tick_length
	if tick_label:
		line += ' ' + tick_label
	print(line)

def draw_interval(center_length):
	"""draw tick interval based upon a central tick length."""
	if center_length > 0: # stop when length drops to 0
		draw_interval(center_length - 1) # recursively draw top ticks
		draw_line(center_length) # draw center tick
		draw_interval(center_length - 1) # recursively draw bottom ticks

def draw_ruler(num_inches, major_length):
	"""draw English ruler with given number of inches, major tick length."""
	draw_line(major_length, '0' ) # draw inch 0 line
	for j in range(1, 1 + num_inches):
		draw_interval(major_length - 1) # draw interior ticks for inch
		draw_line(major_length, str(j)) # draw inch j line and label


n_inch = input("Number of inches (big lines with labels): " + "\n")
n_blines = input("""Length of big line - defines how many levels of divisions per inch -
N --> 1st   2nd   3rd   4th   5tf  ...
5 --> 1/1   1/2   1/4   1/8   1/16 ...
(less == shorter): """)

n_inch_para = int(n_inch)
n_blines_para = int(n_blines)

os.system('clear')
print("Drawing ruler of", n_inch, "inches in length, with", n_blines, "levels of divisions:")
draw_ruler(n_inch_para, n_blines_para)


