#! /usr/bin/env python3

import math

cevi = {0.0889: 20, 0.1683: 22, 0.2191: 30}

cnt = 1
As = 0.0

for d, L in cevi.items():
    Ac = (math.pi * d) * L
    As += Ac
    print("\n{} - Površina cevi {} na dolžini {} znaša {} m2.".format(cnt, d, L, Ac))
    print("\tSkupna površina znaša {} m2.".format(As))
    cnt +=1
