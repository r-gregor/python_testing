#! /usr/bin/env python3

L1 = [1, 3, 5, 7, 9, 13, 15, 17, 19, 21]
L2 = [2, 4, 6, 8, 10]

print("Initial lists are\n", L1, "\n", L2,)

LK = []

while len(L1) > 0 and len(L2) > 0:  # while there are are elements in both lists ...
	if L1[0] < L2[0]:			   # compare first elements
		LK.append(L1.pop(0))		# remove from L1 if elemnt 0 smaller and add to final list LK
	else:
		LK.append(L2.pop(0))		# remove from L2 if elemnt 0 smaller and add to final list LK

LK.extend(L1 + L2)				  # after one list is empty, simply add the other to the final list

print("\nFinal - merged - list:\n",LK)

