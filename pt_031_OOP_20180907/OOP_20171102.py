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
		
	def get_last_name(self):
		return self.lname
		
	def get_age(self):
		return self.age
	
	def whoami(self):
		print("My name is: {}. My last name is {}. I am {} years old.".format(self.name, self.lname, self.age))

G = Person('Gregor', 'Redelonghi', 49)
print("{0}{1}\n{2}{3}\n{4}{5}".format("NAME:".ljust(12), G.get_name(), "LAST NAME:".ljust(12), G.get_last_name(), "AGE:".ljust(12), G.get_age()))


print()
print("Adding a 'sport = JUDO' property to G object")
G.sport = 'JUDO'

print()
print("Runing a 'whoami' method:")
G.whoami()

print()
print("Displaying added 'sport' property:")
nm = G.get_name()
print("{}'s main sport is {}!".format(nm, G.sport))

print()
print(run_fast(G.get_last_name()))
print(run_fast(nm, 8.2))

'''
OUTPUT:

$> gregor.redelonghi@cygwin-en [/home/gregor.redelonghi/_BIN_PYTHON_en_testing]
$> ./OOP_20171102.py
NAME:	   Gregor
LAST NAME:  Redelonghi
AGE:		49

Adding a 'sport = JUDO' property to G object

Runing a 'whoami' method:
My name is: Gregor. My last name is Redelonghi. I am 49 years old.

Displaying added 'sport' property:
Gregor's main sport is JUDO!

Redelonghi runs at 3.6 meters per second!
Gregor runs at 8.2 meters per second!

'''



