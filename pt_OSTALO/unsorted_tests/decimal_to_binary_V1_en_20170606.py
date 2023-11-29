#! /usr/bin/env python3

import math as m
import os, sys

os.system('clear')

gr_ANS = int(input("Enter positive decimal integer to calculate binary representation __ "))

if gr_ANS < 0:
    print("Decimal integer MUST bE POSITIVE!")
    sys.exit(1)

N = gr_ANS
LR = []

if N == 0:
    print("Number N =", N)
    gr_dignum = N + 1
    gr_BINNUM = N
    print("Number of binary digits = ", gr_dignum)
    print("\nBinary number of decimal number " + str(N) + " is:\n" + str(gr_BINNUM))
    sys.exit(0)


print("Number N =", N)
gr_N = int(m.log(N,2))
gr_dignum = gr_N + 1
print("Number of binary digits = ", gr_dignum)

# print("Populating list LR with zeros ...")
for j in range(0, gr_dignum):
    LR.insert(j,0)

# print("Initialised list LR =", LR)

# print("Entering the first binary ONE digit to " + str(gr_N+1) + "-th place")
LR[gr_N] = 1
# print(LR)
gr_rest = 0
gr_diff = N

while gr_diff != 0:
    gr_rest = gr_rest + 2**(gr_N)
    gr_diff = N - gr_rest
    if gr_diff == 0:
        break
    gr_N = int(m.log(gr_diff,2))
    LR[gr_N] = 1
    # print(LR)

L = LR[::-1]
# print(L)

gr_BINNUM=""
for i in L:
    gr_BINNUM += str(i)

print("\nBinary number of decimal number " + str(N) + " is:\n" + gr_BINNUM)

