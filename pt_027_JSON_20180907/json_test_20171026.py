#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import json

fajl = 'my_json_data.txt'

# my data as dict:
my_data = { 'nm' : 'Gregor', 
'lnm' : 'Redelonghi', 
'addr' : 'Valvasorjeva ulica 5', 
'twn' : '1000 Ljubljana', 
'cntr' : 'Slovenia', 
'GSM' : '040/88-55-60', 
'eml_1' : 'gredelonghi@gmail.com', 
'eml_2' : 'gregor.redelonghi@energetika-lj.si', 
'insd' : '20171026', 
'inst' : '131000'
}


# print out (on screen) as disct:
print("print out (on screen) as disct:")
distro_json = json.dumps(my_data)
print(distro_json)

print()
# print out (on screen) as JSON formated:
print("print out (on screen) as JSON formated:")
distro_json = json.dumps(my_data, sort_keys=True, indent=4)
print(distro_json)

print()
# write it into external file ...
print('write it into external file ...')
with open(fajl, "w") as fj:
	json.dump(my_data, fj)

print("The contents of my_data succesfully exported to ", fajl)

print()
# export the contents of object to JSON file:
print('export the contents of object to JSON file:')
class Test:
	def __init__(self):
		self.a = 10
		self.b = 15
		self.c = 20

test1 = Test()

print(json.dumps(test1.__dict__))

