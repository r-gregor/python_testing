#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def run_fast(name, speed = 3.6):
	return "{} runs at {} meters per second!".format(name, speed)

class Person:
	def __init__(self, name, lname, age):
		self.name = name
		self.lname = lname
		self.age = age
	
	def get_name(self):
		return self.name
		
	def get_lname(self):
		return self.lname
		
	def get_age(self):
		return self.age
	
	def whoami(self):
		print("My name is: {}. My last name is {}. I am {} years old.".format(self.name, self.lname, self.age))

"""
CLI USE:

>>> import OOP_20171103 as P
>>> G = P.Person('Gregor', 'Redelonghi', 49)
>>> G.get_name()
'Gregor'
>>> G.sport = 'JUDO'
>>> print("{}'s favorite sport is {}!".format(G.get_name() + " " + G.get_lname(), G.sport))
Gregor Redelonghi's favorite sport is JUDO!
>>> M = P.Person('Mark', 'Redelonghi', 18)
>>> M.whoami()
My name is: Mark. My last name is Redelonghi. I am 18 years old.
>>> G.whoami()
My name is: Gregor. My last name is Redelonghi. I am 49 years old.
>>> P.run_fast(M.get_name(), 3.6)
'Mark runs at 3.6 meters per second!'
>>> M_fname = '{} {}'.format(M.get_name(), M.get_lname())
>>> M_fname
'Mark Redelonghi'
>>> P.run_fast(M_fname, 3.6)
'Mark Redelonghi runs at 3.6 meters per second!'
>>>


"""