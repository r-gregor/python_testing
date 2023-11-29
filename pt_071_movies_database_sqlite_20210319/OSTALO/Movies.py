#! /usr/bin/env python3
# -*- coding: utf-8 -*-

fname="movies-list.txt"


def printMoviesList(dict):
	for nm, yr in dict.items():
		print(f'Movie: {nm} {yr}')


mvs = {}

with open(fname) as f:
	# lines = f.readlines()	# includes empty lines (between and at the end!!)
	lines = [l for l in (line.strip() for line in f) if l]	# strip off empty lines and trailing space


	for el in lines:
		line = el.split()
		mname = " ".join(line[:-1])
		myr = line[-1]
		mvs[mname] = myr

print(mvs)
printMoviesList(mvs)


