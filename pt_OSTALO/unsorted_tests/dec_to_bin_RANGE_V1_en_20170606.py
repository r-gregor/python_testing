#! /usr/bin/env python3

import math as m
import os, sys

os.system('clear')

gr_ANS = int(input("Enter positive decimal integer to calculate binary representation of range: __ "))
print()

if gr_ANS < 0:
    print("Decimal integer MUST bE POSITIVE!")
    sys.exit(1)


if gr_ANS == 0:
    print("Number N =", N)
    gr_dignum = gr_ANS  + 1
    gr_BINNUM = gr_ANS
    print("Number of binary digits = ", gr_dignum)
    print("\nBinary number of decimal number " + str(N) + " is:\n" + str(gr_BINNUM))
    sys.exit(0)

gr_N1 = int(m.log(gr_ANS+1, 2)) + 1
gr_off0 = 8
gr_off1 = gr_N1 + 3

print("{}{}{}".format("Dec".ljust(gr_off0), "Bin".ljust(gr_off1), "digit-num"))
print("-"*(gr_off0 + gr_off1 + 9))
print("{}{}{}".format("0".ljust(gr_off0), "0".ljust(gr_off1), "1"))
gr_dignum_s = 1 # starting dignum to compaaer to new dignum - to draw a line between different dignums

for N in range(1, gr_ANS+1):
    LR = []
    gr_N = int(m.log(N,2))
    gr_dignum = gr_N + 1
    if gr_dignum > gr_dignum_s:     # compare new and old dignum
        print("-"*(gr_off0 + gr_off1 + 9))

    # print("Populating list LR with zeros ...")
    for j in range(0, gr_dignum):
        LR.insert(j,0)
    
    LR[gr_N] = 1
    gr_rest = 0
    gr_diff = N
    
    while gr_diff != 0:
        gr_rest = gr_rest + 2**(gr_N)
        gr_diff = N - gr_rest
        if gr_diff == 0:
            break
        gr_N = int(m.log(gr_diff,2))
        LR[gr_N] = 1
    
    L = LR[::-1]
    gr_BINNUM = ""
    gr_dignum_s = gr_dignum # set curr dignum to old dignum to compare
    for i in L:
        gr_BINNUM += str(i)
        
    print("{}{}{}".format(str(N).ljust(gr_off0) , gr_BINNUM.ljust(gr_off1), gr_dignum))

