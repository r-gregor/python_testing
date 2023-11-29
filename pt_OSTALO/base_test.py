#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# imports -------------------
import basem as bm

# globals -------------------
gr_lnw = 80


# funcs ----------------------
def lns():
	bm.line("-", gr_lnw)

def lnd():
	bm.line("=", gr_lnw)

# main -----------------------
lns()
T = bm.tmpstmp()
print("Printing timestamp: {}".format(T))

lns()
bm.info()

lns()
print("Current date: {}".format(bm.currdt()))
print("Current time: {}".format(bm.currtm()))
lnd()


