#! /usr/bin/env python3

# list of lists
LL = [['Gregor', 'Redelonghi', 'Mua-d_IB'],
['Tadeja', 'Mali', 'SABA'],
['Mark', 'Reeddeelloonngghhii', 'MM'],
['Spela', 'Redelonghi', 'JAH-1'],
['Zala', 'Redelonghi', 'JB-O']]

print('list of lists:')
print(LL)

# add hs chars between columns
hs = 2

# print sepparation line: char multiplied by num of chars + spaces
def printl(lenl):
	print("-"*lenl)

print()
# list of max lenghts of strins in inner list (each sublist)
bl = []
for el in LL:
	bl.append(len(max(el, key = len)))
print('Number of chars of longest word for each sublist:')
print(bl)

# line lengh len1 = sum of max lenghts
len1 = sum(bl) + len(bl)*hs


print()
print('Table print lines to columns:')
printl(len1) # ---------------------------------------------
'''
for each position (index) in each sublist print element right ajusted
to number of chars of longest word in sublist -- lines to columns

range(NUM) --> fixed number of columns => number of elements in each sublist!!
'''
for n in range(3): # where from 3 (no good!)
	for IL in LL:
		NN = len(max(IL, key=len)) + hs
		print(IL[n].rjust(NN), end = '')
	print()
printl(len1) # ---------------------------------------------




'''
for each element in sublist print element right ajusted to number of
chars of longest word in each column (index)

range(NUM) --> fixed number of columns => number of elements in each sublist!!
'''
print()

# create a list of lenghts of longest words foe each column (index)
lnghts = []
for index in range(3):
	TL = []
	for el in LL:
		TL.append(el[index])
		max_L = len(max(TL, key = len))
	lnghts.append(max_L)

print('Number of chars of longest word for each column (index):')
print(lnghts)

# line lengh len2 = sum of max lenghts
len2 = sum(lnghts) + len(lnghts)*hs

print()
print('Table print:')
printl(len2) # ---------------------------------------------
for el in LL:
	for index in range(3):
		print(el[index].rjust(lnghts[index] + 2), end = '')
	print()
printl(len2) # ---------------------------------------------
