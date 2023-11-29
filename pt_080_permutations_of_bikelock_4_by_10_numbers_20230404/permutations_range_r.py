import itertools as it

i = 0
for N in it.permutations(range(10), 4):
	print(f"{i}\t{N}")
	i += 1


