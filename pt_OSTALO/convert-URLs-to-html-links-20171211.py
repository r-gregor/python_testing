#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# startup variables
gr_FJLIN = "samostojni-URL-naslovi_BoB_20171211.txt"
gr_FJLOUT = "BoB_html_povrzave_20171211.txt"
gr_BoBL = []

# Open source file and read lines
fji = open(gr_FJLIN, 'r')

# for each row in source file: 
for LN in fji.readlines():
	LN = LN.strip('/\n')

	# header, address
	gr_H, gr_A = LN.split('//')
	
	# append tuple (header, address) to list
	gr_BoBL.append((gr_H, gr_A))
	
fji.close()

# Open destination file
fjo = open(gr_FJLOUT, 'w')

# for each element (tuple) in a list:
for E in gr_BoBL:
	# test print
	# print("<a href=\"{}\">{}</a>".format('//'.join(E), E[1]))
	
	# print final line to destination file
	fjo.write("<li><a href=\"{}\">{}</a></li>\n".format('//'.join(E), E[1]))

fjo.close()
print("DONE!")
