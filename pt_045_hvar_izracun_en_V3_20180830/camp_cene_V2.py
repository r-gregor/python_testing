#! /usr/bin/env python3
from tabulate import tabulate # Installed from PyPi!!
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


# camp in EUR from camp_L list in[HRK]
camp_L_EUR = []
for row in camp_L:
	nt = (row[0], row[1]/conv, row[2]/conv)
	camp_L_EUR.append(nt)


# vars from data lists
camp_odr, camp_odr_nsez, camp_odr_vsez = camp_L[0]
camp_otr, camp_otr_nsez, camp_otr_vsez = camp_L[1]
camp_parc, camp_parc_nsez, camp_parc_vsez = camp_L[2]
camp_avto, camp_avto_nsez, camp_avto_vsez = camp_L[3]
camp_el, camp_el_nsez, camp_el_vsez = camp_L[4]


print()
print("AutoCamp NUDIST -- Vrboska/Hvar (camp 2018)")
print("{0:<13}{1:>12}{2:>12}".format('camp[HRK]', 'nsez', 'vsez'))
print("-"*37)
for nms in ['odr', 'otr', 'parc', 'avto', 'el']:
	print("{0:<13}{1:>12.2f}{2:>12.2f}".format(eval('camp_'+nms), eval('camp_'+nms+'_nsez'), eval('camp_'+nms+'_vsez')))
print()

gregor, gregor_dni_nsez, gregor_dni_vsez = dni_L[0]
tadeja, tadeja_dni_nsez, tadeja_dni_vsez = dni_L[1]
zala, zala_dni_nsez, zala_dni_vsez = dni_L[2]
mark, mark_dni_nsez, mark_dni_vsez = dni_L[3]
spela, spela_dni_nsez, spela_dni_vsez = dni_L[4]
parc_avt_el, parc_avt_el_dni_nsez, parc_avt_el_dni_vsez = dni_L[5]


print()
print("{0:<13}{1:>12}{2:>12}".format('Ime', 'dni_nsez', 'dni_vsez'))
print("-"*37)
for nms in ['gregor', 'tadeja', 'zala', 'mark', 'spela', 'parc_avt_el']:
	print("{0:<13}{1:>12}{2:>12}".format(nms, eval(nms+'_dni_nsez'), eval(nms+'_dni_vsez')))
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
st_dni_odr_nsez = gregor_dni_nsez + tadeja_dni_nsez + zala_dni_nsez + mark_dni_nsez
st_dni_odr_vsez = gregor_dni_vsez + tadeja_dni_vsez + zala_dni_vsez + mark_dni_vsez
st_dni_otr_nsez = spela_dni_nsez
st_dni_otr_vsez = spela_dni_vsez

skupaj_odr = (st_dni_odr_nsez * camp_odr_nsez) + (st_dni_odr_vsez * camp_odr_vsez)
skupaj_otr = (st_dni_otr_nsez * camp_otr_nsez) + (st_dni_otr_vsez * camp_otr_vsez)
skupaj_parc = (parc_avt_el_dni_nsez * camp_parc_nsez) + (parc_avt_el_dni_vsez * camp_parc_vsez)
skupaj_avto = (parc_avt_el_dni_nsez * camp_avto_nsez) + (parc_avt_el_dni_vsez * camp_avto_vsez)
skupaj_el = (parc_avt_el_dni_nsez * camp_el_nsez) + (parc_avt_el_dni_vsez * camp_el_vsez)

tabela = [	('Odrasli', skupaj_odr, skupaj_odr/conv),
			('Otroci', skupaj_otr, skupaj_otr/conv),
			('Parcela', skupaj_parc, skupaj_parc/conv),
			('Avto', skupaj_avto, skupaj_avto/conv),
			('Elektrika', skupaj_el, skupaj_el/conv)	]

skupaj_osebe = skupaj_odr + skupaj_otr
camp_total = skupaj_odr + skupaj_otr + skupaj_parc + skupaj_avto + skupaj_el
camp_total_EUR = skupaj_odr/conv + skupaj_otr/conv + skupaj_parc/conv + skupaj_avto/conv + skupaj_el/conv

print()
print("{0:<25}{1:>13}{2:>13}".format('Izracun - CAMP', 'znesek[HRK]', 'znesek[EUR]'))
#print("-"*51)
for row in tabela:
	print("{0:<25}{1:>13.2f}{2:>13.2f}".format(row[0], row[1], row[2]))
print("-"*51)
print("{0:<25}{1:>13.2f}{2:>13.2f}".format('SKUPAJ:', camp_total, camp_total_EUR))
# print("-"*51)
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
pots['Jadrolinija'] = pot1_jdrl + pot2_jdrl

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

# TEST PRINTS ------------------------------------------------------------------------------------------------
'''
print()
input("Continue?")

print()
print("{0:<10}{1:>10}{2:>10}".format('camp[HRK]', 'n_sez', 'v_sez'))
print("-"*30)
for row in camp_L:
	print("{0:<10}{1:>10}{2:>10}".format(row[0], row[1], row[2]))
"""
OUTPUT:
camp[HRK]	  n_sez	 v_sez
------------------------------
camp_odr		  40		50
camp_otr		  20		25
camp_parc		 70		80
camp_avto		 20		20
camp_el		   20		20
"""


print()
print(tabulate(camp_L, headers=['camp[HRK]', 'n_sez', 'v_sez']))
"""
OUTPUT:
camp[HRK]	  n_sez	v_sez
-----------  -------  -------
camp_odr		  40	   50
camp_otr		  20	   25
camp_parc		 70	   80
camp_avto		 20	   20
camp_el		   20	   20
"""

print()
print(tabulate(camp_L, headers=['camp[HRK]', 'n_sez', 'v_sez'], tablefmt='psql'))
"""
OUTPUT:
+-------------+---------+---------+
| camp[HRK]   |   n_sez |   v_sez |
|-------------+---------+---------|
| camp_odr	|	  40 |	  50 |
| camp_otr	|	  20 |	  25 |
| camp_parc   |	  70 |	  80 |
| camp_avto   |	  20 |	  20 |
| camp_el	 |	  20 |	  20 |
+-------------+---------+---------+
"""

print()
print("--- In EUR-os --------------------------------------------------------------------------\n")

print("{0:<10}{1:>10}{2:>10}".format('camp[EUR]', 'n_sez', 'v_sez'))
print("-"*30)
for row in camp_L:
	print("{0:<10}{1:>10.2f}{2:>10.2f}".format(row[0], row[1]/conv, row[2]/conv))
"""
OUTPUT:
camp[EUR]	  n_sez	 v_sez
------------------------------
camp_odr		5.38	  6.72
camp_otr		2.69	  3.36
camp_parc	   9.41	 10.75
camp_avto	   2.69	  2.69
camp_el		 2.69	  2.69
"""

print()
print(tabulate(camp_L_EUR, headers=['campEUR', 'n_sez', 'v_sez']))
"""
OUTPUT:
campEUR	  n_sez	 v_sez
------------  -------  --------
camp_odr	  5.37634   6.72043
camp_otr	  2.68817   3.36022
camp_parc	 9.4086   10.7527
camp_avto	 2.68817   2.68817
camp_el	   2.68817   2.68817
"""

print()
print(tabulate(camp_L_EUR, headers=['campEUR', 'n_sez', 'v_sez'], tablefmt='psql'))
"""
OUTPUT:
+--------------+---------+----------+
| campEUR   |   n_sez |	v_sez |
|--------------+---------+----------|
| camp_odr	 | 5.37634 |  6.72043 |
| camp_otr	 | 2.68817 |  3.36022 |
| camp_parc	| 9.4086  | 10.7527  |
| camp_avto	| 2.68817 |  2.68817 |
| camp_el	  | 2.68817 |  2.68817 |
+--------------+---------+----------+
"""
'''
# TEST PRINTS ------------------------------------------------------------------------------------------------
