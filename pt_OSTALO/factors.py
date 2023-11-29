#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def fctrs(n):
	for k in range(1, n+1):
		if n % k == 0:
			yield k


print("Calculating factors for number 100 ...")

FF = fctrs(100)


print(next(FF))
print(next(FF))
print(next(FF))
print(next(FF))
print(next(FF))
print(next(FF))
print(next(FF))
print(next(FF))
print(next(FF))
print(next(FF))
