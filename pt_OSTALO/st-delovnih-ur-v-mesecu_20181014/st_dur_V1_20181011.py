#! /usr/bin/env python3
'''
20181011:	V1
TO DO: 	classes with methods that return data:
		class mesec --> data number of days in month
					--> method to return number of days in month
					--> method to return number of workdays depending on the start day of the month
					--> method to print report from prevoius two methods
					
'''

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
	def __init__(self, mesec):
		self.mesec = mesec
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
		
	def displayUreNaMesecAll(self):
		"""
		function to print number of work hours per month given the
		start day
		"""
		# print("Mesec: {}, Stevilo dni: {}".format(self.mesec, dni_v_mescu[self.mesec],), end = ", ")
		print("Prvi dan: {}, Stevilo delovnih ur: {}".format(teden[self.getZacetek()], self.getUreNaMesec()))

		
	def displayAll(self):
		for item in mesci:
			m = mesec(item)
			print("Mesec: {}, dni na mesec: {}".format(m.getMesec(), m.getStDni()))
			for dan in range(0,7):
				m.setZacetek(dan)
				m.displayUreNaMesec()
			print("-"*80)
	# END class mesec


def displayAll():
	for item in mesci:
		m = mesec(item)
		print("Mesec: {}, dni na mesec: {}".format(m.getMesec(), m.getStDni()))
		for dan in range(0,7):
			m.setZacetek(dan)
			m.displayUreNaMesecAll()
		print("-"*80)			
	
m1 = mesec("Januar"); m1.setZacetek(3); m1.displayUreNaMesec()
m2 = mesec("Januar",); m2.displayUreNaMesec()
m3 = mesec("Februar"); m3.displayUreNaMesec()

displayAll();


'''
**************************************************************************************************************
OPTIONAL CONSTRUCTOR VALUES:

favorite
17
This question already has an answer here:

Least Astonishment and the Mutable Default Argument 31 answers
Somehow, in the Node class below, the wordList and adjacencyList variable is shared between all instances
of Node.

>>> class Node:
...     def __init__(self, wordList = [], adjacencyList = []):
...         self.wordList = wordList
...         self.adjacencyList = adjacencyList
... 
>>> a = Node()
>>> b = Node()
>>> a.wordList.append("hahaha")
>>> b.wordList
['hahaha']
>>> b.adjacencyList.append("hoho")
>>> a.adjacencyList
['hoho']
Is there any way I can keep using the default value (empty list in this case) for the constructor parameters
but to get both a and b to have their own wordList and adjacencyList variables?

I am using python 3.1.2.

python constructor default-value
Mutable default arguments don't generally do what you want. Instead, try this:

class Node:
     def __init__(self, wordList=None, adjacencyList=None):
        if wordList is None:
            self.wordList = []
        else:
             self.wordList = wordList 
        if adjacencyList is None:
            self.adjacencyList = []
        else:
             self.adjacencyList = adjacencyList
			 
**************************************************************************************************************
'''
