#! /usr/bin/env python3

'''
20181011:	V3:	if argument to script only month --> display all 7 possible
				weekday starts --> new method
20181012:	V4:	final if statement printout according to number of argument suplied
20181013:	V5:	dni_v_mescu dict keys all to lowercase --> PARAMETER TO FUNCTION to lowercase, so eny way
				a month is entered it is converted to lowercase.

20181014:	V6:	add clear-screen and start tms func
				if both arguments month and day in a week supplied: only print line with number of work hours


'''

import os
import sys
import datetime as dt


def cls():
	os.system('clear')

# timestamp
def tms():
    return dt.datetime.now().strftime('%Y%m%d_%H%M%S')

# MESSAGE:
cls()
print("[ {} ] -- Starting {} ...\n".format(tms(), sys.argv[0]))



usage1 = "\nUSAGE:\t{} [month name] [day in a week]".format(sys.argv[0])
usage2 ="""
	- month name in SLO: januar, februar, marec, ..., December (any Case)
	- day in a week must be a number:
		1 - Monday
		2 - Tuesday
		...
		7 - Sunday

	If no argument supplied:
	- month = januar
	- day in a week = 1 (Monday)
"""
usage = usage1 + usage2

teden = ['PO', 'TO', 'SR', 'CE', 'PE', 'SO', 'NE']
dni_v_mescu = 	{	'januar': 31,
					'februar': 28,
					'marec': 31,
					'april': 30,
					'maj': 31,
					'junij': 30,
					'julij': 31,
					'avgust': 31,
					'september': 30,
					'oktober': 31,
					'november': 30,
					'december': 31
				}

mesci = list(dni_v_mescu.keys())

# START class mesec
class mesec:
	def __init__(self, mesec = None, zacetek = None):

		if mesec is not None:
			self.mesec = mesec.lower()
		else:
			self.mesec = "januar"

		if zacetek is not None:
			self.zacetek = zacetek
		else:
			self.zacetek = 0


	def setZacetek(self, start):
		self.zacetek = start

	def getMesec(self):
		return self.mesec

	def getZacetek(self):
		return self.zacetek

	def getStDni(self):
		dni = dni_v_mescu[self.mesec]
		return dni

	def getUreNaMesec(self):
		start = self.zacetek
		k = 1
		DD = 0
		dni = dni_v_mescu[self.mesec]
		while k < dni:
			if start > len(teden) - 1:
				start = 0

			if teden[start] != 'SO' and teden[start] != 'NE':
				DD +=1

			start += 1
			k += 1
		st_ur = DD * 8
		return st_ur

	def displayUreNaMesec(self):
		"""
		function to print number of work hours per month given the
		start day
		"""
		print("Mesec: {}, Stevilo dni: {}".format(self.mesec, dni_v_mescu[self.mesec],), end = ", ")
		print("Prvi dan: {}, Stevilo delovnih ur: {}".format(teden[self.getZacetek()], self.getUreNaMesec()))


	def displayUreNaMesec_2(self):
		"""
		function to print number of work hours per month given the
		start day
		"""
		# print("Mesec: {}, Stevilo dni: {}".format(self.mesec, dni_v_mescu[self.mesec],), end = ", ")
		print("Prvi dan: {}, Stevilo delovnih ur: {}".format(teden[self.getZacetek()], self.getUreNaMesec()))


	def displayUreNaMesecAll(self):
		"""
		function to print number of work hours per month given the
		start day
		"""
		print("Prvi dan: {}, Stevilo delovnih ur: {}".format(teden[self.getZacetek()], self.getUreNaMesec()))


	def displayMesec(self, mesec):
		self.mesec = mesec.lower()
		print("-"*80)
		print("Mesec: {}, dni na mesec: {}".format(self.getMesec(), self.getStDni()))
		for dan in range(0,7):
			self.setZacetek(dan)
			self.displayUreNaMesec_2()
		print("-"*80)



	def displayAll(self):
		for item in mesci:
			m = mesec(item)
			print("Mesec: {}, dni na mesec: {}".format(m.getMesec(), m.getStDni()))
			for dan in range(0,7):
				m.setZacetek(dan)
				m.displayUreNaMesec_2()
			print("-"*80)

# END class mesec

if len(sys.argv) == 3:
	try:
		my_month = sys.argv[1]
		my_startDay = int(sys.argv[2]) - 1
		m1 = mesec(my_month); m1.setZacetek(my_startDay); m1.displayUreNaMesec()
		# m1.displayMesec(my_month)
	except:
		print("Inapropriate value!")
		print(usage)

elif len(sys.argv) == 2:
	try:
		my_month = sys.argv[1]
		my_startDay = 0
		m2 = mesec(my_month, my_startDay); m2.displayUreNaMesec()
		m2.displayMesec(my_month)
	except:
		print("Inapropriate value!")
		print(usage)

else:
	print(usage)
	my_month = "januar"
	my_startDay = 0
	try:
		m3 = mesec(my_month); m3.displayMesec(my_month)
	except:
		print("Inapropriate value!")

# m = mesec()
# m.displayAll()
