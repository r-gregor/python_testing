#! /usr/bin/env python3
# -*- coding = utf-8 -*-

from operator import itemgetter

D = {'A' : 16, 'B' : 25, 'C' : 75, 'D' : 100, 'E': 5, 'F' : 55, 'G' : 98}

for k, v in sorted(D.items(), key = itemgetter(1)):
	print(k + " --> " + str(v))
	
print()

for k, v in sorted(D.items(), key = itemgetter(1)):
	print(k, "|" + "="*v + ' '*(100-v) + "|")
	
print()

for k, v in sorted(D.items(), key = itemgetter(1)):
	print(k, "[" + "="*v + '.'*(100-v) + "]")
	
print()

for k, v in sorted(D.items(), key = itemgetter(1)):
	print(k, "[" + "+"*v + '.'*(100-v) + "]")
	
print()

for k, v in sorted(D.items(), key = itemgetter(1)):
	print(k, "[" + "#"*v + '.'*(100-v) + "]")
