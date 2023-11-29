#! /usr/bin/env python3


def merge(L1, L2):
	n1 = len(L1)
	n2 = len(L2)
	FA = []
	
	i = 0
	j = 0

	while i < n1 and j < n2:
		if L1[i] <= L2[j]:
			FA.append(L1[i])
			i += 1
		else:
			FA.append(L2[j])
			j += 1

	
	while i < n1:
		FA.append(L1[i])
		i += 1

	
	while j < n2:
		FA.append(L2[j])
		j += 1

	return FA


Arr1 = [1, 3, 5, 7, 7, 9, 11]
Arr2 = [2, 4, 4, 4, 6, 8, 10, 10, 12]
FinalArray = merge(Arr1, Arr2)

print("Arr1:", Arr1)
print("Arr2:", Arr2)
	
print("\n" + "Number of elements in FinalArray = {}\n".format(len(FinalArray)))
	
print("Merged arrays:", FinalArray)

