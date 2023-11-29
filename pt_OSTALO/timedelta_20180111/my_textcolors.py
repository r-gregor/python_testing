#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
# test
C1 = ['BLACK', 'RED', 'GREEN', 'YELLOW', 'BLUE', 'MAGENTA', 'CYAN', 'WHITE']
'''

c_RED = "\x1b[31m"
c_REDB = "\x1b[31;1m"
c_BLACK = "\x1b[30m"
c_BLACKB = "\x1b[30;1m"
c_GREEN = "\x1b[32m"
c_GREENB = "\x1b[32;1m"
c_YELLOW = "\x1b[33m"
c_YELLOWB = "\x1b[33;1m"
c_BLUE = "\x1b[34m"
c_BLUEB = "\x1b[34;1m"
c_MAGENTA = "\x1b[35m"
c_MAGENTAB = "\x1b[35;1m"
c_CYAN = "\x1b[36m"
c_CYANB = "\x1b[36;1m"
c_WHITE = "\x1b[37m"
c_WHITEB = "\x1b[37;1m"


b_RED = "\x1b[41m"
b_REDB = "\x1b[41;1m"
b_BLACK = "\x1b[40m"
b_BLACKB = "\x1b[40;1m"
b_GREEN = "\x1b[42m"
b_GREENB = "\x1b[42;1m"
b_YELLOW = "\x1b[43m"
b_YELLOWB = "\x1b[43;1m"
b_BLUE = "\x1b[44m"
b_BLUEB = "\x1b[44;1m"
b_MAGENTA = "\x1b[45m"
b_MAGENTAB = "\x1b[45;1m"
b_CYAN = "\x1b[46m"
b_CYANB = "\x1b[46;1m"
b_WHITE = "\x1b[47m"
b_WHITEB = "\x1b[47;1m"

NN = "\x1b[0m"
REV = "\x1b[7m"
UNDRL = "\x1b[7m"

'''
# printout
def prntclr(CLR):
    print("{0}{1}{2}{3}".format("Text color:".ljust(30), eval("c_" + CLR), CLR, NN))
    print("{0}{1}{2}{3}".format("Bright text color:".ljust(30), eval("c_" + CLR + "B"), CLR, NN))
    print("{0}{1}{2}{3}".format("Background color:".ljust(30), eval("b_" + CLR), CLR, NN))
    print("{0}{1}{2}{3}".format("Bright background text color:".ljust(30), eval("b_" + CLR + "B"), CLR, NN))
    print("{0}{1}{2}{3}{4}".format("Text color - REVERSED:".ljust(30), eval("c_" + CLR), REV, CLR, NN))
    print("---")

for CLRS in C1:
    prntclr(CLRS)
'''

