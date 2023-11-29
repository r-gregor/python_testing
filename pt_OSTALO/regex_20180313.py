#! /usr/bin/env python3
# -*- coding: utf-8 -*-


import re

S = '''Gregor Redelonghi
Valvasorjeva ulica 5
1000 Ljubljana

TEL: (01) 426 33 82
GSM: (040) 88-55-60
EML: gredelonghi@gmail.com'''


print("\nString:")

print("="*80)
print(S)
print("="*80)

rgx1 = re.compile(r'\(\d*\)')
# rgx2 = re.compile(r'g.*@.*')
rgx2 = re.compile(r'\w+@\w+')
rgx3 = re.compile(r'R\w+')
rgx4 = re.compile(r'\d+-\d+-\d+')



for NN in range(1,5):
	expNN = 'rgx' + str(NN)
	var = eval(expNN)
	print('regex ' + str(NN) + ': ' + expNN)
	print(var)
	print(var.search(S).group())
	print("-"*80)

rgx5 = re.compile(r'\(\d+\)')
expr = rgx5.findall(S)
print(expr)

rgx6 = re.compile(r'\w*redelon\w*', re.I)
expr = rgx6.findall(S)
print(expr)

