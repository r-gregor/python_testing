#! /usr/bin/env python3

import os, sys
import datetime as dt

# timestamp
def tms():
    return dt.datetime.now().strftime('%Y%m%d_%H%M%S')

# clear
def cls():
	os.system('clear')


cls()
# START MESSAGE:
print("[ {} ] -- Starting {} ...\n".format(tms(), sys.argv[0]))

vrst = 92
cy = 2018
benz_poraba_L_100km = 10
benz_cena_L = 10
HRK_to_EUR = 7.44
HAC_tja = 318
HAC_nazaj = HAC_tja
st_family = 5
 
Mark = {"name":"Mark", "age":cy - 1999, "dni_ls":1, "dni_hs":11}
Zala = {"name":"Zala", "age":cy - 1996, "dni_ls":1, "dni_hs":11}
Spela = {"name":"Spela", "age":cy - 2008, "dni_ls":1, "dni_hs":19}
Tadeja = {"name":"Tadeja", "age":cy - 1971, "dni_ls":1, "dni_hs":19}
Gregor = {"name":"Gregor", "age":cy - 1968, "dni_ls":1, "dni_hs":19}

Camp_ls = {"ODR":40, "OTR":20, "parcela":70, "avto":20, "elektrika":20, "dni_ls":1}
Camp_hs = {"ODR":50, "OTR":25, "parcela":80, "avto":20, "elektrika":20, "dni_hs":19}

Trajekt = {"ODR":65, "OTR":40, "avto":318, "prikolica":20}

def get_stevilo_ODR():
	ODR = 5
	for names in [Mark, Zala, Spela, Tadeja, Gregor]:
		if names["age"] <= 12:
			ODR =- 1
	return ODR

st_ODR = get_stevilo_ODR()
st_OTR = st_family - st_ODR

def get_camp_cena():
	st_dni_skupaj = Gregor["dni_ls"] + Gregor["dni_hs"]
	camp_cena = 0
	camp_cena_SKUPAJ = 0
	osebe_cena = 0

	
	for names in [Mark, Zala, Spela, Tadeja, Gregor]:
		if names["age"] <= 12:
			print("OTROCI: {}, dni hs/ls: {}/{};".format(names["name"], names["dni_ls"], names["dni_hs"]), end=" ")
			osebe_plus = ( (Camp_ls["OTR"] * names["dni_ls"]) + (Camp_hs["OTR"] * names["dni_hs"]) )
			osebe_cena += osebe_plus
			print("{} HRK x {} dni + {} HRK x {} dni".format(Camp_ls["OTR"], names["dni_ls"], Camp_hs["OTR"], names["dni_hs"]), end=" = ")
			print("{} HRK / {:.3f} EUR".format(osebe_plus, osebe_plus/HRK_to_EUR))
		else:
			print("ODRASLI: {}, dni hs/ls: {}/{};".format(names["name"], names["dni_ls"], names["dni_hs"]), end=" ")
			osebe_plus = ( (Camp_ls["ODR"] * names["dni_ls"]) + (Camp_hs["ODR"] * names["dni_hs"]) )
			osebe_cena += osebe_plus
			print("{} HRK x {} dni + {} HRK x {} dni ".format(Camp_ls["ODR"], names["dni_ls"], Camp_hs["ODR"], names["dni_hs"]), end=" = ")
			print("{} HRK / {:.3f} EUR".format(osebe_plus, osebe_plus/HRK_to_EUR))
	
	print("-"*vrst)
	print("Osebe SKUPAJ: {} HRK / {:3f} EUR".format(osebe_cena, osebe_cena/HRK_to_EUR))
	
	print()
	for item in ["parcela", "avto", "elektrika"]:
		camp_plus = Camp_ls["dni_ls"] * Camp_ls[item] + Camp_hs["dni_hs"] * Camp_hs[item]
		camp_cena += camp_plus
		print("{}: {} dni x {} HRK + {} dni x {} HRK".format(item, Camp_ls["dni_ls"], Camp_ls[item], Camp_hs["dni_hs"], Camp_hs[item] ), end=" = ")
		print("{} HRK / {:.3f} EUR".format(camp_plus, camp_plus/HRK_to_EUR))

	print("-"*vrst)
	print("Camp: {} HRK / {:.3f} EUR".format(camp_cena, camp_cena/HRK_to_EUR))
	
	print()
	camp_cena_SKUPAJ = camp_cena + osebe_cena
	print("="*vrst)
	print("Camp + osebe: {} HRK / {:.3f} EUR".format(camp_cena_SKUPAJ, camp_cena_SKUPAJ/HRK_to_EUR))
	print("="*vrst)

get_camp_cena()

	
	