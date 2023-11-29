#! /usr/bin/env python3

D = {}
D["Tadeja"] = {"priimek": "Redelonghi", "naslov": "Valvasorjeva ulica 5"}
D["Gregor"] = {"hobi": ["judo", "hribolazenje"], "visina": 185, "sluzba": "ENERGETIKA LJUBLJANA, d.o.o."}

print(D)
print()

def display():
	for k, v in D.items():
		print("{}".format("[" + k + "]"))
		for k1, v1 in v.items():
			print("{:<10}{}".format(k1 + ":", v1))
		print()
	print("-------------------------------------------")

display()

D["Mark"] = {"Faks": "FRI", "group": "GoBreakers", "hobi": "kolesajenje"}
print(D)
print()

display()

print("[Hobiji]")
for k, v in D.items():
	if "hobi" in v:
		if isinstance(v["hobi"], (list,)):
			print("{:<10}{}".format(k + ":", ", ".join(v["hobi"])))
		else:
			print("{:<10}{}".format(k + ":", v["hobi"]))
