import os, sys

L1 = []
L1 = ['file' + str(i) for i in range(1,11)]
print('First list', L1)

L2 =[]
L2 = ['file' + str(i) for i in range(12,21)]
print('Second list', L2)

L2[2] = 'file4'
L2[6] = 'file8'

for F in L1:
	if F in L2:
		print("File", F, "found in both lists!")

