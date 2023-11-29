#! /usr/bin/python
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

# Asks for a number.
# Prints if it is even or odd

print("Input [q] for exit.")

while True:
	inp = raw_input("Tell me a number: ")
	if inp == 'q':
		break
	# catch any resulting ValueError during the conversion to float
	try:
		number = float(inp)
	except ValueError:
		print('I said: Tell me a NUMBER!')
	else:
		test = number % 2
		if test == 0:
			print (int(number),"is even.")
		elif test == 1:
			print (int(number),"is odd.")
		else:
			print (number,"is very strange.")
