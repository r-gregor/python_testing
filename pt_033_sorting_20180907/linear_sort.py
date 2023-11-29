#! /usr/bin/env python3
# -*- coding: utf-8 -*-



# linear sort algorithm

A = [15, 5, 2, 4, 6, 1, 3, 20, 7, 10, 8, 9]
A_lenght = len(A)

print("List A (unsorted):", A)
print("Number of elements in A:", A_lenght)
print("Continue ...")
ITRR = 1
print("Entering the main for loop ...")
print("for j in range(1, A_lenght)")
for j in range(1,  A_lenght):
	print("-----------------------------------\nThis is iteration:", ITRR)
	ITRR += 1
	key = A[j]
	print("key = A[j] = A[" + str(j) + "] =", key)
	# Insert A[j] into the sorted sequence A[1 .. j-1]
	i = j-1
	print("i = j-1 =", i)
	### BRISI?? print("i =", i, "; key = A[i] = A[" + str(i) + "] =", key)
	while i >= 0 and A[i] > key:
		print("In the while loop ...")
		print("\ti =", i, "\n\tA[i] =", A[i], "\n\tkey =", key)
		print("i >= 0 and A[i] > key, so still in the while loop ...")
		A[i+1] = A[i]
		print("A[i+1] = A[i] =", A[i])
		i = i - 1
		print("i = i-1 = ", i)
	if (i < 0):
		print("i < 0, going out ...")
	if (A[i] <= key):
		print("A[i] !> key, going out ...")

	A[i+1] = key
	print("Outside the while loop ...")
	print("A[i+1] = A[" + str(i+1) + "] = key =", key)
	print("Partially sorted list A:", A)

print("========================================================================")
print("Finally: outside the main for loop ...")
print("Fully sorted List (array) A:", A)
print("End.")

