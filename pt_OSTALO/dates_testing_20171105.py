#! /usr/bin/env python3
# -*- code: utf-8 -*-

L = [20170217, 20170202, 19680222, 19700119, 19960705, 19990417, 20080211, 19480218, 19111011]

def year(D):
    return str(D)[:4]

def month(D):
    return str(D)[4:6]

def day(D):
    return str(D)[6:]

print()
print('Dates that have 17 in year')
for D in L:
    if '17' in year(D):
        print(D)

print()
print('Dates that have 7 in month')
for D in L:
    if '7' in month(D):
        print(D)

print()
print('Dates that have 2 in day')
for D in L:
    if '2' in day(D):
        print(D)
