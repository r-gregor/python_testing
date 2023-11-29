#! /usr/bin/env python3

L1 = []
D1 = {}

with open("sources/2017/E2017.properties") as f:
	for line in f.readlines():
		L1.append(line.replace('\n', ''))

print(L1)

print()
for el in L1:
		if "08" in el:
			print(el)
			
print()
with open("sources/2017/E2017.properties") as f:
	for line in f.readlines():
		el = line.replace('\n', '')
		key, value = el.split("=")
		D1[key] = value

for k, v in D1.items():
	print("{} = {} EUR".format(k, v))

print("The expenses for month 08: {} EUR.".format(D1["E2017-08"]))
