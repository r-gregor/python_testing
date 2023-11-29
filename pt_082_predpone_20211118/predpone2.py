import sys
import math

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

if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <number>")
        sys.exit(1)

num = float(sys.argv[1])

def exponent(n):
    exp = int(math.log10(n))
    return exp

exp = exponent(num)
predp = exp // 3
base = num / math.pow(1000,predp)
predpona = predpone[predp]

def printout(num):
	print(f"Number: {num}")
	print(f"Result: {base:.2f}{predpona} ({pnames.get(predpona)})")
	print("---")

printout(num)
