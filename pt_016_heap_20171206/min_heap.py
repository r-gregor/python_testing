#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# MinHeap (lowest is root)

H = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
HL = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']

print('\nNumbers heap H')
heap_H = '''
			   0
	   +---------------+
	   |			   |
	   1			   2
   +-------+	   +-------+ 
   |	   |	   |	   |
   3	   4	   5	   6
 +---+   +---+   +---+   +---+  
 |   |   |   |   |   |   |   |   
 7   8   9  10  11   12  13  14
'''

print(heap_H)

print('\nLetters heap H')
heap_HL = '''
			   A
	   +---------------+
	   |			   |
	   B			   C
   +-------+	   +-------+ 
   |	   |	   |	   |
   D	   E	   F	   G
 +---+   +---+   +---+   +---+  
 |   |   |   |   |   |   |   |   
 H   I   J   K   L   M   N   O
'''

print(heap_HL)

print("\nNumbers heap:\n{}\n".format(H))
print("Letters heap:\n{}".format(HL))
input("\nContinue?")

def parent(i):
	if i == 0:
		return 0
	else:
		return int((i-1)/2)

def left_child(i):
	return (i*2) + 1


def right_child(i):
	return (i*2) + 2

print()
for I in range(len(H)):
	print("Numbers heap - node: {}.".format(H[I]))
	if I == 0:
		print("The ROOT node: NO PARENT!")
	else:
		print("The parent is: {}.".format(H[parent(I)]))
		
	if left_child(I) > len(H) or right_child(I) > len(H):
		print("No child. Leaf node!")
		print()
	else:
		print("The LEFT child is: {}.".format(H[left_child(I)]))
		print("The RIGHT child is: {}.".format(H[right_child(I)]))
		print()
	
print()
for J in range(len(HL)):
	print("Letters heap - node: {}.".format(HL[J]))
	if J == 0:
		print("The ROOT node: NO PARENT!")
	else:
		print("The parent is: {}.".format(HL[parent(J)]))
		
	if left_child(J) > len(HL) - 1:
		print("No child. Leaf node!")
		print()
	else:
		print("The LEFT child is: {}.".format(HL[left_child(J)]))
		print("The RIGHT child is: {}.".format(HL[right_child(J)]))
		print()
