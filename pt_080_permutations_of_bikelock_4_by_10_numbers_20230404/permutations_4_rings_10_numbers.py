import itertools as it

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result = [p for p in it.product(x, repeat=4)]

i = 0
for item in result:
	i += 1
	# if i % 500 == 0:
	#	  print(f"{i}\t {item}")

	print(f"{i}\t {item}")

print(f"\ndisplayed: Permutations of 4-rings with 10 numbers (0-9)")

