#! /usr/bin/env python3
"""
Triplet and duplet combinations of cards, whose sum produces blackjack = 21
Create separate lists of cardnames and values to display combinations with
cardnames.
Create dictionary of cardnames and coresponding values with zipping the two
previous lists.
L = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11, 1]
							  J   Q   K   A  A

"""

print("Print triplet and duplet combinations of BLACK-JACK cards that produce sum of \"21\"")

print()
L = list(range(2,11))
L.extend([10,10,11,1])

BJ = [  "C_2",
		"C_3",
		"C_4",
		"C_5",
		"C_6",
		"C_7",
		"C_8",
		"C_9",
		"C_J",
		"C_Q",
		"C_K",
		"C_A-h",
		"C_A-l"
]

BJC = dict(zip(BJ, L))

print("The list of cards: ", BJC)


blackjack = 21

NM = 1
print()
print("--- TRIPLETS ---")
for i in range(len(L)):
	for j in range(i+1, len(L)):
		for k in range(j+1, len(L)):
			if L[i] + L[j] + L[k] == blackjack:
				print("The combination", NM, "is:", BJ[i], "+", BJ[j], "+", BJ[k], "=", blackjack)
				NM +=1

NM2 = 1
print()				
print("--- DUPLETS ---")
for i in range(len(L)):
	for j in range(i+1, len(L)):
			if L[i] + L[j] == blackjack:
				print("The combination", NM2, "is:", BJ[i], "+", BJ[j], "=", blackjack)
				NM2 +=1
