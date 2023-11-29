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
HRK_to_EUR = 7.44
HAC_tja = 318
HAC_nazaj = HAC_tja
st_family = 5

dist_cesta = 528		# KM
bencin_na_100km = 10	# L / 100KM
bencin_cena = 10.330	# HRK
 
Mark = {"name":"Mark", "age":cy - 1999, "dni_ls":1, "dni_hs":11}
Zala = {"name":"Zala", "age":cy - 1996, "dni_ls":1, "dni_hs":11}
Spela = {"name":"Spela", "age":cy - 2008, "dni_ls":1, "dni_hs":19}
Tadeja = {"name":"Tadeja", "age":cy - 1971, "dni_ls":1, "dni_hs":19}
Gregor = {"name":"Gregor", "age":cy - 1968, "dni_ls":1, "dni_hs":19}

Camp_ls = {"Odrasli":40, "Otroci":20, "parcela":70, "avto":20, "elektrika":20, "dni_ls":1}
Camp_hs = {"Odrasli":50, "Otroci":25, "parcela":80, "avto":20, "elektrika":20, "dni_hs":19}

# Trajekt = {"Odrasli":65, "Otroci":40, "avto":318, "prikolica":20}

pot_D =  {	'Avtocesta' : 318,
			'Jadrolinija - odrasli' : 47,
			'Jadrolinija - otroci' : 23.5,
			'Jadrolinija - avto' : 310,
			'Jadrolinija - prikolica' : 200 }

def get_stevilo_Odrasli():
	Odrasli = 5
	for names in [Mark, Zala, Spela, Tadeja, Gregor]:
		if names["age"] <= 12:
			Odrasli =- 1
	return Odrasli

st_Odrasli = get_stevilo_Odrasli()
st_Otroci = st_family - st_Odrasli

def get_camp_cena():
	st_dni_skupaj = Gregor["dni_ls"] + Gregor["dni_hs"]
	camp_cena = 0
	camp_cena_SKUPAJ = 0
	osebe_cena = 0
	

	print()
	print("AutoCamp NUDIST -- Vrboska/Hvar (camp 2018)")
	print("{0:<13}{1:>12}{2:>12}".format('camp[HRK]', 'nsez', 'vsez'))
	print("-"*37)
	for el in ["Odrasli", "Otroci", "parcela", "avto", "elektrika"]:
		print("{0:<13}{1:>12}{2:>12}".format(el, Camp_ls[el], Camp_hs[el]))
	print()
	
	print()
	print("{0:<13}{1:>12}{2:>12}".format('Ime', 'dni_nsez', 'dni_vsez'))
	print("-"*37)
	for nms in [Gregor, Tadeja, Zala, Mark, Spela]:
		print("{0:<13}{1:>12}{2:>12}".format(nms["name"], nms["dni_ls"], nms["dni_hs"]))
	print()

	print()
	print("{0:<25}{1:>12}".format('Pot', 'cena[HRK]'))
	print("-"*37)
	for k, v in pot_D.items():
		print("{0:<25}{1:>12}".format(k, v))
	print()

	input("Continue to Calculations?")
	cls()
	

	
	for names in [Mark, Zala, Spela, Tadeja, Gregor]:
		if names["age"] <= 12:
			print("Otroci: {}, dni hs/ls: {}/{};".format(names["name"], names["dni_ls"], names["dni_hs"]), end=" ")
			osebe_plus = ( (Camp_ls["Otroci"] * names["dni_ls"]) + (Camp_hs["Otroci"] * names["dni_hs"]) )
			osebe_cena += osebe_plus
			print("{} HRK x {} dni + {} HRK x {} dni".format(Camp_ls["Otroci"], names["dni_ls"], Camp_hs["Otroci"], names["dni_hs"]), end=" = ")
			print("{} HRK / {:.3f} EUR".format(osebe_plus, osebe_plus/HRK_to_EUR))
		else:
			print("Odrasli: {}, dni hs/ls: {}/{};".format(names["name"], names["dni_ls"], names["dni_hs"]), end=" ")
			osebe_plus = ( (Camp_ls["Odrasli"] * names["dni_ls"]) + (Camp_hs["Odrasli"] * names["dni_hs"]) )
			osebe_cena += osebe_plus
			print("{} HRK x {} dni + {} HRK x {} dni ".format(Camp_ls["Odrasli"], names["dni_ls"], Camp_hs["Odrasli"], names["dni_hs"]), end=" = ")
			print("{} HRK / {:.3f} EUR".format(osebe_plus, osebe_plus/HRK_to_EUR))
	
	print("-"*vrst)
	print("Osebe: {} HRK / {:3f} EUR".format(osebe_cena, osebe_cena/HRK_to_EUR))
	
	print()
	for item in ["parcela", "avto", "elektrika"]:
		camp_plus = Camp_ls["dni_ls"] * Camp_ls[item] + Camp_hs["dni_hs"] * Camp_hs[item]
		camp_cena += camp_plus
		print("{}: {} dni x {} HRK + {} dni x {} HRK".format(item, Camp_ls["dni_ls"], Camp_ls[item], Camp_hs["dni_hs"], Camp_hs[item] ), end=" = ")
		print("{} HRK / {:.3f} EUR".format(camp_plus, camp_plus/HRK_to_EUR))

	print("-"*vrst)
	print("Camp: {} HRK / {:.3f} EUR".format(camp_cena, camp_cena/HRK_to_EUR))
	
	'''
	print()
	camp_cena_SKUPAJ = camp_cena + osebe_cena
	print("-"*vrst)
	print("Camp - SKUPAJ: {} HRK / {:.3f} EUR".format(camp_cena_SKUPAJ, camp_cena_SKUPAJ/HRK_to_EUR))
	'''
	
	
	print()
	camp_cena_SKUPAJ = camp_cena + osebe_cena
	camp_total = camp_cena_SKUPAJ
	print("{0:<25}{1:>13}{2:>13}".format('Izracun - CAMP', 'znesek[HRK]', 'znesek[EUR]'))
	print("-"*51)
	print("{0:<25}{1:>13.2f}{2:>13.2f}".format('CAMP - SKUPAJ:', camp_cena_SKUPAJ, camp_cena_SKUPAJ/HRK_to_EUR))
	print()
	
	# POT --------------------------------------------------------------------------------------------------------
	pot_bnz = 	(dist_cesta * (bencin_na_100km/100)) * bencin_cena
	pot_hac = 	pot_D['Avtocesta']
	pot1_jdrl = (pot_D['Jadrolinija - odrasli'] * 4) + (pot_D['Jadrolinija - otroci'] * 1) + \
				pot_D['Jadrolinija - avto'] + \
				pot_D['Jadrolinija - prikolica']
	
	pot2_jdrl = (pot_D['Jadrolinija - odrasli'] * 2) + (pot_D['Jadrolinija - otroci'] * 1) + \
				pot_D['Jadrolinija - avto'] + \
				pot_D['Jadrolinija - prikolica']
	
	pot_tja_total = pot_bnz + pot_hac + pot1_jdrl
	pot_nazaj_total = pot_bnz + pot_hac + pot2_jdrl
	pot_total = pot_tja_total + pot_nazaj_total
	
	pots = {}
	pots['Bencin'] = pot_bnz
	pots['Avtocesta'] = pot_hac
	pots['Jadrolinija [tja]'] = pot1_jdrl
	pots['Jadrolinija [nazaj]'] = pot2_jdrl
	
	print()
	print("{0:<25}{1:>13}{2:>13}".format('Izracun - POT', 'znesek[HRK]', 'znesek[EUR]'))
	#print("-"*51)
	for k, v in pots.items():
		print("{0:<25}{1:>13.2f}{2:>13.2f}".format(k, v, v/HRK_to_EUR))
	print("-"*51)
	print("{0:<25}{1:>13.2f}{2:>13.2f}".format('POT - SKUPAJ:', pot_total, pot_total/HRK_to_EUR))
	# print("-"*51)
	print()
	
	# GRAND TOTAL ------------------------------------------------------------------------------------------------
	print()
	print("{0:<25}{1:>13}{2:>13}".format('Izracun - TOTAL', 'znesek[HRK]', 'znesek[EUR]'))
	#print("-"*51)
	print("{0:<25}{1:>13.2f}{2:>13.2f}".format("CAMP", camp_total, camp_total/HRK_to_EUR))
	print("{0:<25}{1:>13.2f}{2:>13.2f}".format('POT', pot_total, pot_total/HRK_to_EUR))
	print("-"*51)
	print("{0:<25}{1:>13.2f}{2:>13.2f}".format('SKUPAJ:', camp_total + pot_total, camp_total/HRK_to_EUR + pot_total/HRK_to_EUR))
	# print("-"*51)

get_camp_cena()

	
	