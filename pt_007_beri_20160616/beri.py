#! /usr/bin/env python3
# -*- coding: utf-8 -*-

gr_FJL = 'seznam.txt'
print("Reading files list from", gr_FJL, "...")
with open(gr_FJL) as f:
	lines = f.read().splitlines()
print("... Done. \n")

print("Iterating trough members of", gr_FJL, "to show contents of each line ..." )
for i in range(len(lines)):
	print("Vrsta", i+1, "je:", lines[i])

## OTHER way:
print("\nOTHER way:")
print("""
for L in open("seznam.txt", "rt").readlines():
	print(L, end ='')

---
RESULT:
""")

for L in open(gr_FJL, "rt").readlines():
	print(L, end ='')

