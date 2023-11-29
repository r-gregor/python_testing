#! /usr/bin/env python3
# -*- coding: utf-8 -*-


FJL = {'201605010830': 'fajl-100.txt', '201601192000': 'Tadejin.fajl.txt', '201605010915': 'fajl-2.txt', '201605031000': 'fajl_20150503.txt'}

print("Data: " + str(FJL) + "\n")
a = "201605"

print("OUTPUT:")
print("Records whose KEY includes \"" + a + "\":")
for key in FJL:
	#if key.startswith(a):
	if a in key:
		print(key, FJL[key])

# output
# 201605010830 fajl-100.txt
# 201605010915 fajl-2.txt

b = "Tadej"

print("\nRecords whose value includes \"" + b + "\":")
for value in FJL.values():
	if b in value:
		print("Value that contains \"" + b + " is: \"" + value + "\"")
		
