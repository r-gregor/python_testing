#! /usr/bin/env python3

cy = 2019
Mark = {"name":"Mark", "age":cy - 1999, "dni_ls":1, "dni_hs":11}
Zala = {"name":"Zala", "age":cy - 1996, "dni_ls":1, "dni_hs":11}
Spela = {"name":"Spela", "age":cy - 2008, "dni_ls":1, "dni_hs":19}
Tadeja = {"name":"Tadeja", "age":cy - 1970, "dni_ls":1, "dni_hs":19}
Gregor = {"name":"Gregor", "age":cy - 1968, "dni_ls":1, "dni_hs":19}

for name in [Mark, Zala, Spela, Tadeja, Gregor]:
	if name["age"] <= 12:
		st = "OTROK"
	else:
		st = "ODRASEL"
	
	print("Ime: {:<10} {:<10} {} ".format(name["name"], "<" + st + ">", name["age"]))
