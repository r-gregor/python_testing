#! /usr/bin/env python3

def merge(L1, L2):
	n1 = len(L1)
	n2 = len(L2)
	FA = [None] * (n1 + n2) # !! CRITICAL !! Will NOT work othervise !!
	'''
	You cannot assign to a list like lst[i] = something, unless the list already is initialized
	with at least i+1 elements. You need to use append to add elements to the end of the list:
	lst.append(something) --> it appends an elemnt to the end of the list.
	
			# Creating an empty list:
			>>> l = [None] * 10
			>>> l
			[None, None, None, None, None, None, None, None, None, None]

			# Assigning a value to an existing element of the above list:
			>>> l[1] = 5
			>>> l
			[None, 5, None, None, None, None, None, None, None, None]
	'''
	
	i = 0
	j = 0
	k = 0

	while i < n1 and j < n2:
		if L1[i] <= L2[j]:
			FA[k] =L1[i]
			i += 1
			k += 1
		else:
			FA[k] = L2[j]
			j += 1
			k += 1
	
	while i < n1:
		FA[k] =L1[i]
		i += 1
		k += 1

	
	while j < n2:
		FA[k] = L2[j]
		j += 1
		k += 1

	return FA


Arr1 = [1, 3, 5, 7, 7, 9, 11]
Arr2 = [2, 4, 4, 4, 6, 8, 10, 10, 12]
FinalArray = merge(Arr1, Arr2)

print("Arr1:", Arr1)
print("Arr2:", Arr2)
	
print("\n" + "Number of elements in FinalArray = {}\n".format(len(FinalArray)))
	
print("Merged arrays:", FinalArray)

