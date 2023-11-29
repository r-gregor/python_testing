#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Greatest Common Divizor -- gcd
# (največji skupni imenovalec)


import sys

gcd = 1
k = 2

if len(sys.argv) != 3:
	n1 = 48052
	n2 = 1616
else:
	n1 = int(sys.argv[1])
	n2 = int(sys.argv[2])

# dokler k ni enak kateremu koli številu ki ju primerjamo, za vsak k, ki je deltelj obeh števil
# brez ostanka določimo da je: gcd = k (prepišem prejšnjo vrednost).
while k <= n1 and k <= n2:
	if n1 % k == 0 and n2 % k == 0:
		gcd = k
		
	k += 1

print("Greatest common divizor fo nums {} and {} is: {}.\n".format(n1, n2, gcd))
