#! /usr/bin/env python3
# -*- coding: utf8 -*-

import time as tm

def tms():
    return tm.strftime('%Y%m%d_%H%M%S')

def sum(X, Y):
    return X + Y

def diff(X, Y):
    return X - Y

def avg(X, Y):
    return (X + Y)/2



fjl = 'numbers.txt'

print("[ {} ] -- reading file ...".format(tms()))
with open(fjl, 'r') as fj:
    # fj.readlines() creates: ['AAA BBB\n', 'CCC DDD\n' ... ] --> NOT GOOD!
    # fj.read().splitlines() creates ['AAA BBB', 'CCC DDD', ... ] --> OK!
    lines = fj.read().splitlines()
    print(lines)


print("\n[ {} ] -- creating a list of (zs, X, Y) tuples ...".format(tms()))
nms = []
zs = 0
for num in lines:
    zs += 1
    X, Y = num.split(' ')
    nms.append((zs, X, Y))  # each element of list nms is tuple: (X, Y)

print(nms)

dct = {}
print("\n[ {} ] -- creating a dict count: X, Y sum(XY), diff(XY), avg(XY) ...".format(tms()))
for el in nms:
    zs = el[0]
    X = int(el[1])
    Y = int(el[2])
    dct[zs] = [X, Y, sum(X,Y), diff(X,Y), avg(X,Y)]

print(dct)


print("\n[ {} ] -- Printing out the contents for each dict element ...".format(tms()))
for i in range(1, len(dct) + 1):
    Z_ST = i
    Xi = dct[i][0]
    Yi = dct[i][1]
    SUMi = dct[i][2]
    DIFFi = dct[i][3]
    AVGi = dct[i][4]
    print("""{0}
X = {1}
Y = {2}
SUM = {3}
DIFF = {4}
AVG = {5}
---------------------------------------------""".format(Z_ST, Xi, Yi, SUMi, DIFFi, AVGi))

print("\n[ {} ] -- DONE!".format(tms()))

