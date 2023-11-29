#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import HugeTest as ht

print("first: locally declared mem info:")
K1 = ht.Test("Conan", "The Destroyer", 69)
K1.info()

K2 = ht.Test("Ivana", "D'Orleans", 151)
K2.info()


print("second: Getting info from imported class:")
for fmem in ht.G, ht.T, ht.Z, ht.M, ht.S:
	fmem.info()


