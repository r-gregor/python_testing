import sys
import math


def rearranged(num):
	predpone = ["", "K", "M", "G", "T", "P", "X", "Z", "Y"]

	pnames = {
		"K" : "Kilo",
		"M" : "Mega",
		"G" : "Giga",
		"T" : "Tera",
		"P" : "Peta",
		"X" : "Exa",
		"Z" : "Zetta",
		"Y" : "Yotta"
	}
	
	exp = int(math.log10(num))

	predp = exp // 3
	base = num / math.pow(1000,predp)
	predpona = predpone[predp]

	result = f"Result: {base:.2f}{predpona} ({pnames.get(predpona)})"
	return result

def run():
	if len(sys.argv) != 2:
		print(f"Usage: {sys.argv[0]} <number>")
		sys.exit(1)

	num = float(sys.argv[1])
	print(rearranged(num))

if __name__ == '__main__':
	run()
