#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# empty string
S = ''

# populate string S with numbers from 1 to 250
for NUM in range(1,251):
	S = S + str(NUM)

print("S = {}".format(S))


# total count of al numbers
print()
print("The count of each number:")
SKP = 0
for NMS in range(0,10):
	# counter for each number from 0 to 9
	cnt = 0
	for el in S:
		if el == str(NMS):
			cnt += 1
	
	# for each number from 0 to 9 print how many is in the S
	print("{} x {}".format(NMS, cnt))
	SKP += cnt

print("Total number of digits is: {} = Sum of calculated number of numbers: {}".format(len(S), SKP))

# print each two consecutiwe numbers that are the same
print()
print("All the pairs of the same numbers")
for i in range(0, len(S) - 1):
	if S[i] == S[i + 1]:
		print(S[i] + S[i + 1] + ", " , end = '')
print()
