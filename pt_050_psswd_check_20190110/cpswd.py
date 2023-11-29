import string

'''
from: http://codingdirectional.info/2019/01/02/create-a-strong-password-for-a-website-account-with-python/
'''
 
def checkio(data: str):
 
	digit_count = 0
	lower_count = 0
	upper_count = 0
	# str_list = list(str) --> str is a type not a variable!!
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
			# return False -->  doesn't work!
			continue		  # added to WORK!
			
	if(digit_count > 0 and lower_count > 0 and upper_count > 0):
		print("OK!")	# added test print
		return True
 
	else:
		print("False")  # added test print
		return False
		
checkio("Gredelonghi.1968")