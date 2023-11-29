import os, sys
import math

predpone = ["", "K", "M", "G", "T"]

'''
if len(sys.argv != 2):
        print("Usage: {} <number>".format(sys.argv[0]))
        sys.exit
'''

# num = float(sys.argv[1]
num = 123456789

def exponent(n):
    potenca = int(math.log10(n))
    return potenca

exponent = exponent(num)

predpona = exponent // 3
print("Predpona:", predpona)

print("Exponent = " + str(exponent))

divizor = 1/math.pow(10, exponent)

print("Result: {:.2f}{}".format(num*divizor, predpone[predpona]))