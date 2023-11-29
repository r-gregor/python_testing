#! /usr/bin/env python3
#-*- coding: utf-8 -*-

import sys

L1 = []
L2 = []

def multiples(num):
    intL = []
    times = 30 + 1
    for i in range(1, times + 1):
        S = num * i
        intL.append(S)
    print("{}: {}".format(num, intL))
    return intL

    # test
    # print("{}, {}: {}".format(num, times, intL))

if len(sys.argv) != 3:
    print("You must supply two positive integers!")
    sys.exit(1)
    
else:
    I1 = int(sys.argv[1])
    I2 = int(sys.argv[2])

if I1 > I2:
    I1, I2 = I2, I1

def compare(n1, n2):
    if n1 == n2:
        return True
    else:
        return False

def findLCM(n1, n2):
    result = 0
    S1 = n1
    S2 = n2

    L1.append(S1)
    L2.append(S2)

    # test
    # print("{}, {}". format(S1, S2))
    # input("Contnue?")
    
    while S1 != S2:
        while S1 <= S2:
            # test
            # print(S1, S2, "\n")
            # input("Go?")
            if compare(S1, S2):
                result = S1
                return result
            else:
                S1 = S1 + n1
                L1.append(S1)
        S2 = S2 + n2
        L2.append(S2)

lcm = findLCM(I1, I2)
print("{}: {}".format(I1, L1))
print("{}: {}".format(I2, L2))
print("LCM of {} and {} is: {}".format(I1, I2, lcm))

