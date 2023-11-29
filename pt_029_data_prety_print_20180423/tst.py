#! /usr/bin/env python3

flds = ["Name", "S-name", "Address", "Mobile", "E-mail"]
_1st = ["Muad", "D'Ib", "Haarkonen Blwd 4850, Kiel", "+386(0)40-22-55-66", "muad.dib@yahoo.hk"]
_2nd = ["Gregor", "Redelonghi", "Valvasorjeva ulica 5, 1000 Ljubljana", "040/88-55-60", "gregor.redelonghi@gmail.com"]
_3rd = ["Tadeja", "Mali-Redelonghi", "Valvasorjeva ulica 5, 1000 Ljubljana", "041/654-241", "tadeja.malir@gmail.com"]

def crt():
	print("-"*(10+20+40+25+30+5))

crt()	
print("{}|{}|{}|{}|{}|".format(flds[0].rjust(10),flds[1].rjust(20),flds[2].rjust(40),flds[3].rjust(25),flds[4].rjust(30)))
crt()
for line in _1st, _2nd, _3rd:
	print("{}|{}|{}|{}|{}|".format(line[0].rjust(10),line[1].rjust(20),line[2].rjust(40),line[3].rjust(25),line[4].rjust(30)))
crt()
