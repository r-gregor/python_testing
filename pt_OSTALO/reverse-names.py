#! /usr/bin/env python3
"""
Script_name:	reverse_names.py
Author:		 RgregoR
Date:		   20171011
--------------------------------------------
Script that prints names and reversed names
from a given list of names.

Uses a class Me and a method of class to
print out the rsult

"""

# class Me definition
class Me:
	def __init__(self, namestring):
		self.nms = namestring
		
	def get_name(self):
		return self.nms
		
	def get_reversed_name(self):
		S = list(self.nms)
		RS = []
		for N in range(len(S)):
			RS.append(S.pop())
		return ''.join(RS)
	
	def print_rev_nms(self):
		print("{:<20} {}".format("My name is:", self.get_name()))

		print("{:<20} {}".format("My name REVERSED is:", self.get_reversed_name()))
		print("-"*60)

# execute only if run as standalone script:
if __name__ == "__main__":
	print()
	print("Using stack data structure to reverse the name string:")
	print("-"*60)

	for names in ["Gregor Redelonghi", "Tadeja Mali Redelonghi", "Zala Redelonghi", "Mark Redelonghi", "Špela Redelonghi"]:
		nm = Me(names)
		nm.print_rev_nms()
		nm = None
