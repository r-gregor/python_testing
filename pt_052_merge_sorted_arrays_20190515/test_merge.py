FA = []

L1 = [1, 3, 5, 5, 7, 9, 11, 13]
L2 = [2, 4, 6, 8, 10, 12, 12, 12]
L3 = []

i = 0
j = 0

while i < len(L1) and j < len(L2):
	if L1[i] <= L2[j]:
		L3.append(L1[i])
		i += 1
	else:
		L3.append(L2[j])
		j += 1

while i < len(L1):
	L3.append(L1[i])
	i += 1
		
while j < len(L2):
	L3.append(L2[j])
	j += 1
	
print(L3)
