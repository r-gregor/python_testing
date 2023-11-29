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
# print("[ {} ] -- Starting {} ...".format(tms(), sys.argv[0]))

'''
!! TECH !!
insert csv data into list of tuples:
https://stackoverflow.com/questions/18776370/converting-a-csv-file-into-a-list-of-tuples-with-python

import csv
with open('/tmp/test.csv') as f:
    data=[tuple(line) for line in csv.reader(f)]

print(data)
# OUTPUT
# [('Brand', ' Price', ' Weight', ' Type'), ..., ('brand2', ' 3.05', ' 2.2', ' plum')]

'''


# global vars
conv = 7.44				# HRK to EUR: 7.44 HRK = 1 EUR
dist_cesta = 528		# KM
bencin_na_100km = 10	# L / 100KM
bencin_cena = 10.330	# HRK

st_odrasli = 4
st_otroci = 1

# data lists
camp_L = [	('odr', 40, 50),
			('otr', 20, 25),
			('parc', 70, 80),
			('avto', 20, 20),
			('el', 20, 20) ]


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


# NOVO ##  NOVO ##  NOVO ##  NOVO ##  NOVO ##  NOVO ##  NOVO ##  NOVO ##  NOVO ##  NOVO ##  NOVO ##  NOVO ##
# dicts for camp prices nsez and vsez, and for numb of days in nsez and vsez:
c_nsez = {}
c_vsez = {}
d_nsez = {}
d_vsez = {}

for ln in camp_L:
	c_nsez[ln[0]] = ln[1]
	c_vsez[ln[0]] = ln[2]

for ln in dni_L:
	d_nsez[ln[0]] = ln[1]
	d_vsez[ln[0]] = ln[2]
# NOVO ##  NOVO ##  NOVO ##  NOVO ##  NOVO ##  NOVO ##  NOVO ##  NOVO ##  NOVO ##  NOVO ##  NOVO ##  NOVO ##

print()
print("AutoCamp NUDIST -- Vrboska/Hvar (camp 2018)")
print("{0:<13}{1:>12}{2:>12}".format('camp[HRK]', 'nsez', 'vsez'))
print("-"*37)
for el in ['odr', 'otr', 'parc', 'avto', 'el']:
	print("{0:<13}{1:>12.2f}{2:>12.2f}".format(el, c_nsez[el], c_vsez[el]))
print()

print()
print("{0:<13}{1:>12}{2:>12}".format('Ime', 'dni_nsez', 'dni_vsez'))
print("-"*37)
for nms in ['Gregor', 'Tadeja', 'Zala', 'Mark', 'Spela', 'parc_avt_el']:
	print("{0:<13}{1:>12}{2:>12}".format(nms, d_nsez[nms], d_vsez[nms]))
print()

print()
print("{0:<25}{1:>12}".format('Pot', 'cena[HRK]'))
print("-"*37)
for k, v in pot_D.items():
	print("{0:<25}{1:>12}".format(k, v))
print()

print()
input("Continue to Calculations?")
cls()


# IZRACUNI ## IZRACUNI ## IZRACUNI ## IZRACUNI ## IZRACUNI ## IZRACUNI ## IZRACUNI ## IZRACUNI ## IZRACUNI ##
# CAMP -------------------------------------------------------------------------------------------------------
st_dni_odr_nsez = d_nsez['Gregor'] + d_nsez['Tadeja'] + d_nsez['Zala'] + d_nsez['Mark']
st_dni_odr_vsez = d_vsez['Gregor'] + d_vsez['Tadeja'] + d_vsez['Zala'] + d_vsez['Mark']
st_dni_otr_nsez = d_nsez['Spela']
st_dni_otr_vsez = d_vsez['Spela']

skupaj_odr = (st_dni_odr_nsez * c_nsez['odr']) + (st_dni_odr_vsez * c_vsez['otr'])
skupaj_otr = (st_dni_otr_nsez * c_nsez['otr']) + (st_dni_otr_vsez * c_vsez['otr'])
skupaj_parc = (d_nsez['parc_avt_el'] * c_nsez['parc']) + (d_vsez['parc_avt_el'] * c_vsez['parc'])
skupaj_avto = (d_nsez['parc_avt_el'] * c_nsez['avto']) + (d_vsez['parc_avt_el'] * c_vsez['avto'])
skupaj_el = (d_nsez['parc_avt_el'] * c_nsez['el']) + (d_vsez['parc_avt_el'] * c_vsez['el'])

tabela = [	('Odrasli', skupaj_odr, skupaj_odr/conv),
			('Otroci', skupaj_otr, skupaj_otr/conv),
			('Parcela', skupaj_parc, skupaj_parc/conv),
			('Avto', skupaj_avto, skupaj_avto/conv),
			('Elektrika', skupaj_el, skupaj_el/conv)	]

skupaj_osebe = skupaj_odr + skupaj_otr
camp_total = skupaj_odr + skupaj_otr + skupaj_parc + skupaj_avto + skupaj_el
camp_total_EUR = camp_total/conv

print()
print("{0:<25}{1:>13}{2:>13}".format('Izracun - CAMP', 'znesek[HRK]', 'znesek[EUR]'))

for row in tabela:
	print("{0:<25}{1:>13.2f}{2:>13.2f}".format(row[0], row[1], row[2]))
print("-"*51)
print("{0:<25}{1:>13.2f}{2:>13.2f}".format('SKUPAJ:', camp_total, camp_total_EUR))
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
pot_total_EUR = pot_total/conv

pots = {}
pots['Bencin'] = pot_bnz
pots['Avtocesta'] = pot_hac
pots['Jadrolinija [tja]'] = pot1_jdrl
pots['Jadrolinija [nazaj]'] = pot2_jdrl

print()
print("{0:<25}{1:>13}{2:>13}".format('Izracun - POT', 'znesek[HRK]', 'znesek[EUR]'))
#print("-"*51)
for k, v in pots.items():
	print("{0:<25}{1:>13.2f}{2:>13.2f}".format(k, v, v/conv))
print("-"*51)
print("{0:<25}{1:>13.2f}{2:>13.2f}".format('SKUPAJ:', pot_total, pot_total_EUR))
# print("-"*51)
print()

# GRAND TOTAL ------------------------------------------------------------------------------------------------
print()
print("{0:<25}{1:>13}{2:>13}".format('Izracun - TOTAL', 'znesek[HRK]', 'znesek[EUR]'))
#print("-"*51)
print("{0:<25}{1:>13.2f}{2:>13.2f}".format("CAMP", camp_total, camp_total_EUR))
print("{0:<25}{1:>13.2f}{2:>13.2f}".format('POT', pot_total, pot_total_EUR))
print("-"*51)
print("{0:<25}{1:>13.2f}{2:>13.2f}".format('SKUPAJ:', camp_total + pot_total, camp_total_EUR + pot_total_EUR))
# print("-"*51)
