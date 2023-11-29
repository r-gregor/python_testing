#! /usr/bin/env python3
# -*- coding: utf-8 -*-

### from web 20170327
### https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Longest_common_substring#Python_3
### explanation of the algorithm: http://www.ideserve.co.in/learn/longest-common-substring
### calculating the [L]ongest [C]ommon [S]ubstring from two strings ...

print("""
from web 20170327
https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Longest_common_substring#Python_3
explanation of the algorithm: http://www.ideserve.co.in/learn/longest-common-substring
calculating the [L]ongest [C]ommon [S]ubstring from two strings ...

""")


# Original:
def longest_common_substring(s1, s2):
   m = [[0] * (1 + len(s2)) for i in range(1 + len(s1))]
   longest, x_longest = 0, 0
   for x in range(1, 1 + len(s1)):
	   for y in range(1, 1 + len(s2)):
		   if s1[x - 1] == s2[y - 1]:
			   m[x][y] = m[x - 1][y - 1] + 1
			   if m[x][y] > longest:
				   longest = m[x][y]
				   x_longest = x
		   else:
			   m[x][y] = 0
   return s1[x_longest - longest: x_longest]


# Added by me:
string1 = input("enter first string --> ")
string2 = input("enter second string --> ")
print("Calculating the longest common substring ...")

LCS = longest_common_substring(string1, string2)

print("\nLongest Common Substring is:",LCS)
