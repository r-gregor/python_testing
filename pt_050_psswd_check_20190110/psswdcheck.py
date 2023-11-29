import string

'''
from: http://codingdirectional.info/2019/01/02/create-a-strong-password-for-a-website-account-with-python/
'''
 
def checkio(data):
 
	digit_count = 0
	lower_count = 0
	upper_count = 0
	str_list = list(str(data))
	
	print(str_list)
 
	if(str_list.__len__() < 10):
		print("%d is Not enough characters!" % len(str_list))
		return False
	else:
		print("%d IS enough characters!" % len(str_list))
		
 
	for i in range(len(str_list)):
		if(str_list[i] in list(string.ascii_lowercase)):
			lower_count += 1
		elif(str_list[i] in list(string.ascii_uppercase)):
			upper_count += 1
		elif(str_list[i] in list(string.digits)):
			digit_count += 1
		else:
			# return False
			# print("False")
			continue
			
	print("lower_count: {}\nupper_count: {}\ndigit_count: {}". format(lower_count, upper_count, digit_count))
	
	if(digit_count > 0 and lower_count > 0 and upper_count > 0):
 
		# return True
		print("OK!")
 
	else:
 
		# return False
		print("False!")

checkio("Gredelonghi.1968")
