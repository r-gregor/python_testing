#! /usr/bin/env python3
# -*- coding: utf-8 -*-

class GetInfo:
	def __init__(self, name, lname):
		self.name = name
		self.lname = lname
	
	def get_name(self):
		return self.name
		
	def get_lname(self):
		return self.lname*5
		
class Person:
	def __init__(self, first_name, last_name, age, status):
		self.nm = first_name
		self.lnm = last_name
		self.age = age
		self.status = status
		self.info = GetInfo(first_name, last_name)

	def my_info(self):
		print("My info:")
		print("My name: ", self.info.get_name())
		print("My last name: ", self.lnm)
		print("I am {} years old.".format(self.age))
		print("And I am {}.".format(self.status))

P1 = Person('Gregor', 'Redelonghi', 49, 'Maried')
P1.my_info()

print("Indirect (last name * 5): ", P1.info.get_lname())


		