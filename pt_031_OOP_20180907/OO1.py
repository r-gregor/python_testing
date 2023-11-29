#! /usr/bin/env python3
# -*- coding: utf-8 -*-

### [O]bject [O]riented script - TEST

class FamilyGrp():
	def __init__(self, surname, address):
		self.surname = surname
		self.address = address

class FamilyMem(FamilyGrp):
	def __init__(self, name, age, gender):
		self.name = name
		self.age = age
		self.gender = gender

def hline():
	print("-"*56)


rdj = FamilyGrp('Redelonghi', 'Valvasorjeva ulica 5, 1000 Ljubljana')

hci1 = FamilyMem('Zala', 21, 'female')
hci2 = FamilyMem('Spela', 9, 'female')
sin = FamilyMem('Mark', 18, 'male')
mami = FamilyMem('Tadeja', 47, 'female')
oci = FamilyMem('Gregor', 49, 'male')

mems = [hci1, hci2, sin, mami, oci]
smems = ["hci1", "hci2", "sin", "mami", "oci"]
i = 0
for MEM in mems:
	hline()
	# print('Family member: ', smems[i])
	print('{0:16s}{1:}'.format('Family member:', smems[i]))
	i = i+1
	print('{0:16s}{1:s}\n{2:16s}{3:s}\n{4:16s}{5:d}\n{6:16s}{7:s}\n{8:16s}{9:s}'
	.format("Ime:", MEM.name, "Priimek:", MEM.surname, "Starost:", MEM.age, "Spol:", MEM.gender, "Address:", MEM.address))
hline()



