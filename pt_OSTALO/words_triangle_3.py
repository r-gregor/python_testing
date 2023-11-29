#! /usr/bin/env python3
# -*- coding: utf-8 -*-



"""
print string in list format two chars per line, add any sub line new two chars ...



"""

print("""print string in list format two chars per line, add any sub line new two chars ...
""")

L = ['G', 'r', 'e', 'g', 'o', 'r', ' ', 'R', 'e', 'd', 'e', 'l', 'o', 'n', 'g', 'h', 'i', ',',' ', 'T', 'a', 'd', 'e', 'j', 'a', ' ', 'M', 'a', 'l', 'i', ' ', 'R', 'e', 'd', 'e', 'l', 'o', 'n', 'g', 'h', 'i', ',',' ', 'Z', 'a', 'l', 'a', ' ', 'R', 'e', 'd', 'e', 'l', 'o', 'n', 'g', 'h', 'i']

STR = ''.join(L)
print('String: "' + str(STR) + '"\n')
print('Converted to list:')
print(L, "\n")



L1 = ""; i = 0
for i in range(1, len(L), 2):
		L1 = L1 + L[i-1] + L[i]
		print(L1)

"""Output:
$> python3 __today2.py
Gr
Greg
Gregor
Gregor R
Gregor Red
Gregor Redel
Gregor Redelon
Gregor Redelongh
Gregor Redelonghi,
Gregor Redelonghi, T
Gregor Redelonghi, Tad
Gregor Redelonghi, Tadej
Gregor Redelonghi, Tadeja
Gregor Redelonghi, Tadeja Ma
Gregor Redelonghi, Tadeja Mali
Gregor Redelonghi, Tadeja Mali R
Gregor Redelonghi, Tadeja Mali Red
Gregor Redelonghi, Tadeja Mali Redel
Gregor Redelonghi, Tadeja Mali Redelon
Gregor Redelonghi, Tadeja Mali Redelongh
Gregor Redelonghi, Tadeja Mali Redelonghi,
Gregor Redelonghi, Tadeja Mali Redelonghi, Z
Gregor Redelonghi, Tadeja Mali Redelonghi, Zal
Gregor Redelonghi, Tadeja Mali Redelonghi, Zala
Gregor Redelonghi, Tadeja Mali Redelonghi, Zala Re
Gregor Redelonghi, Tadeja Mali Redelonghi, Zala Rede
Gregor Redelonghi, Tadeja Mali Redelonghi, Zala Redelo
Gregor Redelonghi, Tadeja Mali Redelonghi, Zala Redelong
Gregor Redelonghi, Tadeja Mali Redelonghi, Zala Redelonghi
"""

