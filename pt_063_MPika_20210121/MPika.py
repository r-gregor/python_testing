#! /usr/bin/env python3

import sys

# [R]azredi
R1 = (250, 5)
R2 = (1250, 50)
R3 = (3500, 210)

pike = 900.0
znesek = 0.0
razlika = 0.0

def usage():
	print("""
		Usage: MPika.py [št. pik]
	""")

def info(pike, razred, vkratnik, nznesek):
	global znesek
	global razlika
	print("razred: {}, vrednost: {} EUR".format( razred[0], razred[1]))
	print("pike: " + str(pike))
	if vkratnik != 0:
		print("razlika: {} - ({} * {}) = {}".format(pike, vkratnik, razred[0], razlika))
		print("dodatek: {} * {} EUR = {} EUR".format(vkratnik, razred[1], nznesek))
		print("znesek: " + str(znesek) + " EUR")
		print("---")
	else:
		print("dodatek: " + str(nznesek))
		print("znesek: " + str(znesek) + " EUR")
		print("---")

def izracunPik(pike, razred):
	global znesek
	global razlika
	vkratnik = int(pike / razred[0])
	ostanek = pike % razred[0]
	
	if vkratnik >= 1:
		nznesek = vkratnik * razred[1]
		znesek += nznesek
		razlika = ostanek
	else:
		nznesek = 0
		razlika = pike
	info(pike, razred, vkratnik, nznesek)

def koncniZnesek():
		pike = int(sys.argv[1])
		izracunPik(pike, R3)
		izracunPik(razlika, R2)
		izracunPik(razlika, R1)
		print("Končni znesek: " + str(znesek) + " EUR")

# MAIN
if __name__ == "__main__":

	if len(sys.argv) != 2:
		usage()
		sys.exit
	else:
		koncniZnesek()

