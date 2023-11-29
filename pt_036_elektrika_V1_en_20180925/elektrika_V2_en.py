#! /usr/bin/env python3

import sys

D1 = {}
sfile = "sources/2017/E2017.properties"
prfx = "E2017-"

def num_string(n):
	if int(n) < 10:
		num = "0" + n
	else:
		num = n
	
	return num
	


print()
with open(sfile) as sf:
	for line in sf.readlines():
		el = line.replace('\n', '')
		key, value = el.split("=")
		D1[key] = value

'''
# test print
for k, v in D1.items():
	print("{} = {} EUR".format(k, v))
'''

if len(sys.argv) == 1:
		print("No args --> usage {} [num args]".format(sys.argv[0]))
		print("Printing all months:")
		for k, v in D1.items():
			print("{} = {} EUR".format(k, v))
else:
	for el in sys.argv[1:]:
		if int(el) > 12 or int(el) < 0:
			continue
		sfx = num_string(el)
		key = prfx + str(sfx)
		print("Expenses for {} are: {}".format(key, D1[key]))




