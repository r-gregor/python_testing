#! /usr/bin/env python3
# -*- coding: utf-8 -*-


import time
import sys


# time delay:
# time.sleep(5)

# timestamp
def tms():
    return time.strftime('%Y%m%d_%H%M%S')

# startup variables
gr_FJLIN = "samostojni-URL-naslovi_BoB_20171211.txt"
gr_FJLOUT = "BoB_html_povezave_20171211.txt"
gr_BoBL = []

print("[ {} ] -- Starting {} ...".format(tms(), sys.argv[0]))
# Open source file and read lines

print("[ {} ] -- Opening file: {} ...".format(tms(), gr_FJLIN))
fji = open(gr_FJLIN, 'r')

# for each row in source file:
print("[ {} ] -- Reading lines ...".format(tms()))

for LN in fji.readlines():
    LN = LN.strip('/\n')

    # header, address
    gr_H, gr_A = LN.split('//')

    # append tuple (header, address) to list
    gr_BoBL.append((gr_H, gr_A))

print("[ {} ] -- Closing file: {} ...".format(tms(), gr_FJLIN))
fji.close()

# Open destination file
print("[ {} ] -- Opening file: {} ...".format(tms(), gr_FJLOUT))
fjo = open(gr_FJLOUT, 'w')

# for each element (tuple) in a list:
print("[ {} ] -- Writting html links into file: {} ...".format(tms(), gr_FJLOUT))
for E in gr_BoBL:
    # test print
    # print("<a href=\"{}\">{}</a>".format('//'.join(E), E[1]))

    # print final line to destination file
    fjo.write("<li><a href=\"{}\">{}</a></li>\n".format('//'.join(E), E[1]))

print("[ {} ] -- Closing file: {} ...".format(tms(), gr_FJLOUT))
fjo.close()

print("[ {} ] -- DONE!".format(tms()))
