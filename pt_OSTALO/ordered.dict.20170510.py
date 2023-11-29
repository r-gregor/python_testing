#! /usr/bin/env python3
# -*- coding: utf-8 -*-



import operator
import os, sys

os.system('clear')

d = {"Januar":1, "Februar":2, "Marec":3, "April":4, "Maj":5, "Junij":6, "Julij":7, "Avgust":8, "September":9, "Oktober":10, "November":11, "December":12}
sorted_d = sorted(d.items(), key=operator.itemgetter(1))

print("Month of the year to number mapping dictionary (unsorted by design):")
print(d)

print()
print("Year dictionary sorted by 'value' (number):")
print(sorted_d)

print()
print("Formated print:")

for i in sorted_d:
	print('{:<12}{}'.format(i[0], i[1]))
	
print()
print("Enter [C]apitalized name of the month")
mnth = str(input("and the script will display its number: ____ "))
if mnth not in d.keys():
	print("Nonexistant month (mind capitalization!)!")
	sys.exit(1)

print()
print('{:<12}{}'.format('Mesec', 'St'))
print('-'*14)
print('{:<12}{}'.format(mnth, d[mnth]))

"""
Output:

Januar      1
Februar     2
Marec       3
April       4
Maj         5
Junij       6
Julij       7
Avgust      8
September   9
Oktober     10
November    11
December    12
"""
