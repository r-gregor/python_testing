#! /usr/bin/python3
# -*- coding: utf-8 -*-

### print string in list format one char per line, add any sub line new char ...

S = "abcdefghijklmnoprstuvz.ABCDEFGHIJKLMNOPRSTUVZ.0123456789"
print("String S = " + S)

print("\nConverting string S to list ...")
L = list(S)
print("List L =", L)

print("\nFor each letter in list print a letter and add the next one ...")
L1 = ""
# print(L1)
for i in range(0, len(L)):
	L1 = L1 + L[i]
	print(L1)

	
"""
Output:
For each letter in list print a letter and add the next one ...
a
ab
abc
abcd
abcde
abcdef
abcdefg
abcdefgh
abcdefghi
abcdefghij
abcdefghijk
abcdefghijkl
abcdefghijklm
abcdefghijklmn
abcdefghijklmno
abcdefghijklmnop
abcdefghijklmnopr
abcdefghijklmnoprs
abcdefghijklmnoprst
abcdefghijklmnoprstu
abcdefghijklmnoprstuv
abcdefghijklmnoprstuvz
abcdefghijklmnoprstuvz.
abcdefghijklmnoprstuvz.A
abcdefghijklmnoprstuvz.AB
abcdefghijklmnoprstuvz.ABC
abcdefghijklmnoprstuvz.ABCD
abcdefghijklmnoprstuvz.ABCDE
abcdefghijklmnoprstuvz.ABCDEF
abcdefghijklmnoprstuvz.ABCDEFG
abcdefghijklmnoprstuvz.ABCDEFGH
abcdefghijklmnoprstuvz.ABCDEFGHI
abcdefghijklmnoprstuvz.ABCDEFGHIJ
abcdefghijklmnoprstuvz.ABCDEFGHIJK
abcdefghijklmnoprstuvz.ABCDEFGHIJKL
abcdefghijklmnoprstuvz.ABCDEFGHIJKLM
abcdefghijklmnoprstuvz.ABCDEFGHIJKLMN
abcdefghijklmnoprstuvz.ABCDEFGHIJKLMNO
abcdefghijklmnoprstuvz.ABCDEFGHIJKLMNOP
abcdefghijklmnoprstuvz.ABCDEFGHIJKLMNOPR
abcdefghijklmnoprstuvz.ABCDEFGHIJKLMNOPRS
abcdefghijklmnoprstuvz.ABCDEFGHIJKLMNOPRST
abcdefghijklmnoprstuvz.ABCDEFGHIJKLMNOPRSTU
abcdefghijklmnoprstuvz.ABCDEFGHIJKLMNOPRSTUV
abcdefghijklmnoprstuvz.ABCDEFGHIJKLMNOPRSTUVZ
abcdefghijklmnoprstuvz.ABCDEFGHIJKLMNOPRSTUVZ.
abcdefghijklmnoprstuvz.ABCDEFGHIJKLMNOPRSTUVZ.0
abcdefghijklmnoprstuvz.ABCDEFGHIJKLMNOPRSTUVZ.01
abcdefghijklmnoprstuvz.ABCDEFGHIJKLMNOPRSTUVZ.012
abcdefghijklmnoprstuvz.ABCDEFGHIJKLMNOPRSTUVZ.0123
abcdefghijklmnoprstuvz.ABCDEFGHIJKLMNOPRSTUVZ.01234
abcdefghijklmnoprstuvz.ABCDEFGHIJKLMNOPRSTUVZ.012345
abcdefghijklmnoprstuvz.ABCDEFGHIJKLMNOPRSTUVZ.0123456
abcdefghijklmnoprstuvz.ABCDEFGHIJKLMNOPRSTUVZ.01234567
abcdefghijklmnoprstuvz.ABCDEFGHIJKLMNOPRSTUVZ.012345678
abcdefghijklmnoprstuvz.ABCDEFGHIJKLMNOPRSTUVZ.0123456789
"""
