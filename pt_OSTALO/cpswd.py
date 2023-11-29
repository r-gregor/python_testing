import string
 
def checkio(data: str):
 
	digit_count = 0
	lower_count = 0
	upper_count = 0
	str_list = list(data)
 
	if(str_list.__len__() < 10):
		return False
 
	for i in range(len(str_list)):
 
		if(str_list[i] in list(string.ascii_lowercase)): 
			lower_count += 1
		elif(str_list[i] in list(string.ascii_uppercase)):
			upper_count += 1
		elif(str_list[i] in list(string.digits)):
			digit_count += 1
		else:
			# return False
			continue
			
	if(digit_count > 0 and lower_count > 0 and upper_count > 0):
		print("OK!")
		return True
 
	else:
		print("False")
		return False
		
checkio("Gredelonghi.1968")