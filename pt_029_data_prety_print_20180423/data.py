#! /usr/bin/env python3

import tabulate as tb
import csv

with open('data.csv') as f:
	reader = csv.reader(f, delimiter=';')
 
	TAB = []

	for row in reader:
		TAB.append(row)

header = TAB[0]


TAB2 = []
for row in TAB:
	if 'edel' in ",".join(row):
		TAB2.append(row)

TAB2.insert(0, header)

print(tb.tabulate(TAB2, headers="firstrow"))

print()
print("Whole table:")
print(tb.tabulate(TAB, headers="firstrow"))
