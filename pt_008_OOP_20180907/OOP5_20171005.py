#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import os

os.system('clear')

# class judoka: rank and club are deafault values
class Judoka:
	def __init__(self, name, age, rank='brown', club = 'JK Šiška'):
		self.club = club
		self.name = name
		self.age = age
		self.rank = rank

	def get_name(self):
		return self.name
	
	def get_age(self):
		return self.age
	
	def get_rank(self):
		return self.rank
	
	def get_club(self):
		return self.club
	
	def set_rank(self, rank):
		self.rank = rank
		print("Rank for " + self.name + " is updatetd to: " + self.rank)
	
	def __str__(self):
		return "{0:25}{1:<5d}{2:15}{3}".format(self.name, self.age, self.rank, self.club)

# Instantiate object G (Gregor Redelonghi)
G = Judoka('Gregor Redelonghi', 49,)

# Print all properties of "G"
print('Judoka: ' + G.get_name())
print('Age : ' + str(G.get_age()))
print('Rank: ' + G.get_rank())
print('Club: ' + G.get_club())
print()

# Update rank from default to G's
print()
print("Updating rank for: " + G.get_name() + " ...")
G.set_rank('black')

# Instantiate other Judokas
print()
A = Judoka('Anja Dobovšek', 32, rank = 'black (DAN 4)')
R = Judoka('Gregor Rankel', 28, rank = 'black (DAN 3)')

# store h-line lenght in var L
#   L1   L2  L3   lenght of "Club Name"   
L = 25 + 5 + 15 + len("JK Šiška")

def LN():
	print("-"*L)

# print table
LN()
#		 L1	L2   L3 
print("{0:25}{1:5}{2:15}{3}".format("Judoka", "Age", "Rank", "Club"))
LN()
for J in G, R, A:
	print(J)
LN()


# Print all from above to ext file
print()
fname = "judokas.txt"
print("Printing to all of the above to " + fname + ".")

FF = open(fname, "wt")
FF.write('Judoka: ' + G.get_name() + "\n")
FF.write('Age : ' + str(G.get_age()) + '\n')
FF.write('Rank: ' + G.get_rank() + '\n')
FF.write('Club: ' + G.get_club() + '\n')

FF.write('')

FF.write("-"*L + "\n")
FF.write("{0:25}{1:5}{2:15}{3}\n".format("Judoka", "Age", "Rank", "Club"))
FF.write("-"*L + "\n")

for J in G, R, A:
	FF.write("{0:25}{1:5}{2:15}{3}\n".format(J.get_name(), str(J.get_age()), J.get_rank(), J.get_club()))
FF.write("-"*L + "\n\n--- \n")


FF.close()
