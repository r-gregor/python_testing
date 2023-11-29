#! /usr/bin/env python3

'''
20181011:	V3:	if argument to script only month --> display all 7 possible
				weekday starts --> new method


'''


import sys


teden = ['PO', 'TO', 'SR', 'CE', 'PE', 'SO', 'NE']
dni_v_mescu = 	{	'Januar': 31,
					'Februar': 28,
					'Marec': 31,
					'April': 30,
					'Maj': 31,
					'Junij': 30,
					'Julij': 31,
					'Avgust': 31,
					'September': 30,
					'Oktober': 31,
					'November': 30,
					'December': 31
				}

mesci = list(dni_v_mescu.keys())

# START class mesec
class mesec:
	def __init__(self, mesec = None, zacetek = None):

		if mesec is not None:
			self.mesec = mesec
		else:
			self.mesec = "Januar"

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
		self.mesec = mesec
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
	my_month = sys.argv[1]
	my_startDay = int(sys.argv[2]) - 1
	m1 = mesec(my_month); m1.setZacetek(my_startDay); m1.displayUreNaMesec()
	m1.displayMesec(my_month)
elif len(sys.argv) == 2:
	my_month = sys.argv[1]
	my_startDay = 0
	m2 = mesec(my_month, my_startDay); m2.displayUreNaMesec()
	m2.displayMesec(my_month)
else:
	my_month = "Januar"
	my_startDay = 0
	m3 = mesec(my_month); m3.displayMesec(my_month)



# m = mesec()
# m.displayAll()
