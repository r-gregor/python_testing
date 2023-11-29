#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# MinHeap (lowest is root)

H = [1, 7, 13, 15, 19, 14, 28, 20, 44, 21, 22, 18, 16, 103, 33, 55, 23, 46]

print('\nNumbers heap H')
heap_H = '''
				   1
		   +---------------+
		   |			   |
		   7			   13
	   +-------+	   +-------+ 
	   |	   |	   |	   |
	   15	  19	  14	  28
	 +---+   +---+   +---+   +---+  
	 |   |   |   |   |   |   |   |   
	 20  44  21  22  18  16  103 33
	+--+  | 
	|  |  | 
	55 23 46
'''

print(heap_H)

print("\nNumbers heap:\n{}\n".format(H))
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
	print("Node index: {}".format(I))
	print("Numbers heap - node: {}.".format(H[I]))
	if I == 0:
		print("The ROOT node: NO PARENT!")
	else:
		print("The parent is: {}.".format(H[parent(I)]))
	
	if left_child(I) <= len(H) - 1 and right_child(I) <= len(H) - 1:
		print("The LEFT child is: {}.".format(H[left_child(I)]))
		print("The RIGHT child is: {}.".format(H[right_child(I)]))
		print()
	
	if left_child(I) > len(H) - 1:
		print("No child. Leaf node!")
		print()
	
	if left_child(I) <= len(H) - 1 and right_child(I) > len(H) - 1:
		print("The LEFT child is: {}.".format(H[left_child(I)]))
		print()
