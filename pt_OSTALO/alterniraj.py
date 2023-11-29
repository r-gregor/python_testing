#! /usr/bin/env python3

seznam = [3, 4, -1, 1, -5, -2, -1, 7, -8]
print("Start list =", seznam, "\n")

def alterniraj(szn):

	i = 0
	while i < len(szn) - 1:
		if (szn[i + 1] > 0 and szn[i] > 0) or (szn[i] < 0 and szn[i + 1] < 0):
			prz = True
		else:
			prz = False
		
		if prz == True:
			print("{} and {} both have same sign ...".format(szn[i + 1], szn[i]))
			print("Removing {} from the list.\n".format(szn[i + 1]))
			el = szn[i]
			del szn[i + 1]
			i = szn.index(el)
						
		else:
			print("{} and {} are of different sign ...".format(szn[i + 1], szn[i]))
			print("Keeping {} in the list.\n".format(szn[i]))
			i += 1
						
			
	
alterniraj(seznam)
print("Final list =", seznam)


print("\n===================================================================================================")
print("(Brez vmesnih printov)")
print()

seznam = [3, 4, -1, 1, -5, -2, -1, 7, -8]
print(">>> seznam =", seznam)

def alterniraj(szn):

	i = 0
	while i < len(szn) - 1:
		if (szn[i + 1] > 0 and szn[i] > 0) or (szn[i] < 0 and szn[i + 1] < 0):
			prz = True
		else:
			prz = False
		
		if prz == True:
			el = szn[i]
			del szn[i + 1]
			i = szn.index(el)
						
		else:
			i += 1

print(">>> alterniraj(seznam)")
alterniraj(seznam)

print(">>> seznam")
print(seznam)

