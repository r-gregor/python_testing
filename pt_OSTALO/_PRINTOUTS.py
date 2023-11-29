L = [	"ena", "dva", "tri",
		"štir", "pet", "šest",
		"sedem", "osem", "devet"
	]
	
for i in range(len(L)):
	if (i + 1) % 3 == 0:
		print(L[i])
	else:
		print(L[i], end = " ")

for N in range(1,22):
	if (N) % 3 == 0:
		print(str(N))
	else:
		print(str(N), end = " ")
		