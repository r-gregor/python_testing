#! /usr/bin/env python3

D = {	"k1": "ADA",
		"k2": "MADA",
		"k3": "NADA",
		"k4": "ADA",
		"k5": "GREG",
		"k6": "MOJIVA",
		"k7": "KUREJ",
		"k8": "GREG",
		"k9": "JADA",
		"k10": "ADA" }
		
# print(D)

tm = "ADA"
cnt = 0
pairs = []

for k, v in D.items():
	if v == tm:
		cnt += 1
		pairs.append((k, v))

print(pairs)

if cnt == 1:
	print("A key {} holds a value: {}".format(pairs[0][0], pairs[0][1]))
else:
	L = []
	for el in pairs:
		L.append(el[0])
	print("Keys {} hold a value: {}.".format(", ".join(L), tm))
		
