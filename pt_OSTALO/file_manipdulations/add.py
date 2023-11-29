#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import time
import sys


insd = datetime.datetime.today().strftime('%Y%m%d')
inst = datetime.datetime.today().strftime('%H%M%S')

fajl = 'podatki.txt'

# input
name = str(input("Name:  ")) or 'N/A'
lname = str(input("Last name:  ")) or 'N/A'
addr = str(input("Address:  ")) or 'N/A'
twn = str(input("Town:  ")) or 'N/A'
eml_1 = str(input("E-mail /1:  ")) or 'N/A'
eml_2 = str(input("Email /2:  ")) or 'N/A'

# class def
class Member:
    def __init__(self, name, lname, addr, twn, eml_1, eml_2, insd, inst):
        self.name = name
        self.lname = lname
        self.addr = addr
        self.twn = twn
        self.eml_1 = eml_1
        self.eml_2 = eml_2
        self.insd = int(insd)
        self.inst = int(inst)

    def make_list(self):
        L = [self.name, self.lname, self.addr, self.twn, self.eml_1, self.eml_2, self.insd, self.inst]
        return L

# instantiate mem1
mem1 = Member(name, lname, addr, twn, eml_1, eml_2, insd, inst)

L1 = mem1.make_list()
print(L1)

# make string from list
ML1 = []
for M in L1:
    ML1.append(str(M))


S1 = ','.join(ML1)
print(S1)

with open(fajl, 'at') as fj:
    fj.write(S1 + "\n")

print('DONE!')

