#! /usr/bin/env python3

T = ('prvi', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'zadnji')
prv, (*vmsn), zdnj = T

print(prv)
print(vmsn)
print(zdnj)

for e in vmsn:
	print(e, end = ' ')

print('Done!')

peti_osmi = T[5:9]
print(peti_osmi)

def eight():
	if 8 not in peti_osmi:
		return True
	else:
		return False
'''
ans = eight()
print(ans)
'''

print(eight())

print(T[::-2])