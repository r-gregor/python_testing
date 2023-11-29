#! /usr/bin/env python3

# data lists
camp_L = [	('camp_odr', 40, 50),
			('camp_otr', 20, 25),
			('camp_parc', 70, 80),
			('camp_avto', 20, 20),
			('camp_el', 20, 20) ]


dni_L = [	('Gregor', 1, 19),
			('Tadeja', 1, 19),
			('Zala', 1, 11),
			('Mark', 1, 11),
			('Spela', 1, 19),
			('parc_avt_el', 1, 19) ]


pot_D =  {	'Avtocesta' : 318,
			'Jadrolinija - odrasli' : 47,
			'Jadrolinija - otroci' : 23.5,
			'Jadrolinija - avto' : 310,
			'Jadrolinija - prikolica' : 200 }

c_nsez = {}
c_vsez = {}
d_nsez = {}
d_vsez = {}

for ln in camp_L:
	c_nsez[ln[0] + "_nsez"] = ln[1]
	c_vsez[ln[0] + "_vsez"] = ln[2]

for ln in dni_L:
	d_nsez[ln[0] + "_dni_nsez"] = ln[1]
	d_vsez[ln[0] + "_dni_vsez"] = ln[2]

print(c_nsez)
print(c_vsez)
print(d_nsez)
print(d_vsez)



