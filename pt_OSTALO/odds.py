#! /usr/bin/env python3
# -*- coding: utf-8 -*-


llength = 5 + 8 + 8 + 8 + 9
crta = '-'*llength


print("\n" + "Proof that product of 2 odd numbers is always an odd number: product/2 -> remainder:")

print(crta)
print('{0:<5}{1:<8}{2:<8}{3:<8}{4:<8}'.format('#', "odd-1", "odd-2", "product", "remainder"))
print(crta)
for N in range(1, 101):
	M = 2*N-1
	Z = 2*N+1
	P = M*Z
	D = P % 2
	# print('{:<5}'.format(str(N) + ":"), M, Z, P, D)
	print('{0:<5}{1:<8}{2:<8}{3:<8}{4:<8}'.format(str(N), M, Z, P, D))
print(crta)


"""
Result:
$> gregor.redelonghi@cygwin-en [/home/gregor.redelonghi/majstaf/coding/testing-en/PYTHON-en_testing]
$> python3 odds.py
1:	1 3 3 1
2:	3 5 15 1
3:	5 7 35 1
4:	7 9 63 1
5:	9 11 99 1
6:	11 13 143 1
7:	13 15 195 1
8:	15 17 255 1
9:	17 19 323 1
10:   19 21 399 1
11:   21 23 483 1
12:   23 25 575 1
13:   25 27 675 1
14:   27 29 783 1
15:   29 31 899 1
...
50:   99 101 9999 1
...
100:  199 201 39999 1
"""

