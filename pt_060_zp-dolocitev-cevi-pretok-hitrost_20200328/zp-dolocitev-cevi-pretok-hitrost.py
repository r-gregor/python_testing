#! /usr/bin/env python3

import sys

#usage
usage = """
	Usage:
	zp-dolocitev-cevi-pretok-hitrost.py [Qd] [maxw]

		Qd ..... dejanski pretok [m3/h]
		maxw ... max hitrost ZP  [m/s]

"""

# izračun hitrosti glede na pretok in presek
def hitrost(Qd, A):
	w = Qd / (A * 3600)
	return w

# izračun preseka glede na dimenzije cevi
def povrsina(Dz, S):
	Dn = Dz - 2*S
	Ac = (3.1415927 * Dn**2)/4
	return Ac


cevi = {	'33.7': ["DN25", 3.25, 3.6],
			'42.4': ["DN40", 3.25, 3.6],
			'60.3': ["DN50", 3.2, 3.6, 4.0, 4.5],
			'88.9': ["DN80", 3.2, 3.6, 4.0, 4.5],
			'114.3': ["DN100", 3.6, 4.0, 4.5, 5.0],
			"168.3": ["DN150", 3.6, 4.0, 4.5, 5.0],
			'219.1': ["DN200", 4.0, 4.5, 5.0, 5.6],
			'273.0': ["DN250", 4.0, 4.5, 5.0, 5.6],
			'323.9': ["DN300", 4.0, 4.5, 5.0, 5.6]
		}

def izracun(pretok, maxw):
	Qd = pretok
	razlika = maxw
	zmagovalec = ""

	for k, v in cevi.items():
		for ds in v[1:]:
			A = povrsina(float(k), ds)
			Am = A/(1000**2)
			w = hitrost(Qd, Am)
			if w < maxw:
				# izbere tistega znagovalca pri katerem je razlika najmanša!
				if (maxw - w) < razlika:
					razlika =  maxw - w
					zmagovalec = "--> Izbrana cev: " + str(k) +"x"+ str(ds) + " (" + v[0] + "), hitrost: " + str("{:.3f}".format(w)) + " m/s"
				else:
					break

	print("{:22}{}".format("Max hitrost: {} m/s".format(maxw), zmagovalec))


if len(sys.argv) == 1:
	Qd = 288.22
	print("Pretok: {:.2f} m3/h".format(Qd))
	for maxw in [2, 3, 4, 5, 6, 8, 9, 11, 13, 20]:
		izracun(Qd, maxw)

elif len(sys.argv) == 3:
	Qd = float(sys.argv[1])
	maxw = float(sys.argv[2])

	print("Pretok: {:.2f} m3/h".format(Qd))
	izracun(Qd, maxw)

else:
	print("Wrong number of parameters.")
	print(usage)
	sys.exit
