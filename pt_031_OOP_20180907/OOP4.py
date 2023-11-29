#! /usr/bin/env python3
# -*- coding: utf-8 -*-


class rediji:
	lname = "Redelonghi"
	addr = "Valvasorjeva ulica 5, 1000 Ljubljana"


class f_mem(rediji):
	def __init__(self, fname, age, hobbies):
		self.fname = fname
		self.age = age
		self.hobbies = hobbies


class family(rediji):
	car = "FORD S-max, Trendline, 1.6"
	flat_num = 87
	

z = f_mem("Zala", 21, "Dancing, Arts, Drawing")
m = f_mem("Mark", 18, "Dancig, Acrobatics, Snow boarding, Guitar")
t = f_mem("Tadeja", 47, "Dancing, Hiking")
t.lname = "Mali Redelonghi"

s = f_mem("Špela", 9, "Dancing, Hiking, Reading")
g = f_mem("Gregor", 49, "Judo, Dancing, Hiking, Guitar, ...")


for NM in z, m, t, s, g:
	print("{0:15}{1}".format("Name:", NM.fname))
	print("{0:15}{1}".format("Last name:", NM.lname))
	print("{0:15}{1}".format("Age:", NM.age))
	print("{0:15}{1}".format("Hobbies:", NM.hobbies))
	print("{0:15}{1}".format("Address:", NM.addr))
	print("------------------------------------------------")



F = family()

print("{0:20}{1}".format("Family name: ", F.lname))
print("{0:20}{1}".format("Family address: ", F.addr))
print("{0:20}{1}".format("Family car: ", F.car))
print("{0:20}{1}".format("Flat number: ", str(F.flat_num)))

