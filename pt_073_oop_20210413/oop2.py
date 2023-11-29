#! /usr/bin/env python3
# -*- coding: utf-8 -*-

class Person:
	def __init__(self, name, lname, age, address):
		self.name = name
		self.lname = lname
		self.age = age
		self.address = address

	def get_full_info(self):
		line = f"Name: {self.name} {self.lname}, Age: {self.age}\nAddress: {self.address}"
		return line
	
	def show_just_name(self):
		print(f"{self.name} {self.lname}")

print("loading 1st person ... ", end="")
P1 = Person("Gregor", "Redelonghi", 53, "Valvasorjeva ulica 5, 1000 Ljubljana")
print("[OK]")

print("loading 2nd person ... ", end="")
P2 = Person("Špela", "Redelonghi", 13, "Valvasorjeva ulica 5, 1000 Ljubljana")
print("[OK]")

L1 = P1.get_full_info()
print("\n" + f"Printing returned line:\n{L1}")

print("\n" + "Just a name of 2nd person:")
P2.show_just_name()

