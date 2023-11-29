#! /usr/bin/env python3


seznam = [3, 4, -1, 1, -5, -2, -1, 7, -8]
print("seznam = ", seznam, "\n")

def alterniraj(szn):
	i = 1
	
	while i <= len(szn) - 1:
		if szn[i - 1] > 0 and szn[i] > 0:
			print("{} and {} are both positive ...".format(szn[i], szn[i - 1]))
			print("Removing {} from the list.\n".format(szn[i]))
			del szn[i]
			i = 1
					
		elif szn[i - 1] < 0 and szn[i] < 0:
			print("{} and {} are both negative ...".format(szn[i], szn[i - 1]))
			print("Removing {} from the list.\n".format(szn[i]))
			del szn[i]
			
			i = 1  
		
		else:
			print("{} and {} are of different sign ...".format(szn[i], szn[i - 1]))
			print("Keeping {} in the list.\n".format(szn[i]))
			pass
			 
		i += 1
			
alterniraj(seznam)
print(seznam)


'''
seznam = [3, 4, -1, 1, -5, -2, -1, 7, -8]
print("seznam =", seznam)

def alterniraj(szn):
	i = 1
	
	while i <= len(szn) - 1:
		if szn[i - 1] > 0 and szn[i] > 0:
			# print("{} and {} are both positive ...".format(szn[i], szn[i - 1]))
			# print("Removing {} from the list.\n".format(szn[i]))
			del szn[i]
			# print(szn)
			i = 1
					
		elif szn[i - 1] < 0 and szn[i] < 0:
			# print("{} and {} are both negative ...".format(szn[i], szn[i - 1]))
			# print("Removing {} from the list.\n".format(szn[i]))
			del szn[i]
			# print(szn)
			i = 1  
		
		else:
			# print("{} and {} are of different sign ...".format(szn[i], szn[i - 1]))
			# print("Keeping {} in the list.\n".format(szn[i]))
			pass
			 
		i += 1
			
alterniraj(seznam)
print(seznam)
'''