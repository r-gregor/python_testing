sum = 0.0

print("sum of 1/2 + 1/4 + 1/8 + 1/16 + 1/32 ...")
print(" "*12 + "sum = 0")
for N in range(1, 101):
	div = 2**N
	sum = sum + (1.0/div)
	print("({:-3d}) ... + 1/{:<33} = {}".format(N, div,str(sum)))

