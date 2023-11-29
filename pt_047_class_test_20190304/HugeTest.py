#! /usr/bin/env python3
# -*- coding: utf-8 -*-

class Test:
	def __init__(self, name, sname, age):
		self.name = name
		self.sname = sname
		self.age = age
		
	def info(self):
		print("{0:<12}{1}".format("Name:", self.name))
		print("{0:<12}{1}".format("Surname:", self.sname))
		print("{0:<12}{1}".format("Age:", self.age))
		print()
		
T = Test("Tadeja", "Mali Redelonghi", 49)
G = Test("Gregor", "Redelonghi", 51)
Z = Test("Zala", "Redelonghi", 22)
M = Test("Mark", "Redelonghi", 19)
S = Test("Špela", "Redelonghi", 11)


if __name__ == "__main__":
	print("Data class: NOT meant to be used on its own!")
