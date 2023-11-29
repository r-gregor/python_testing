def Euler(n):
	return (1 + 1/n)**n
	
def print_E(start, stop, step):
	print("{:>6} {}".format(1, Euler(1)))
	
	for i in range (start, stop + 1, step):
		print("{:>6} {}".format(i, Euler(i)))
		
start = 100
stop = 1000000000
step = 1000000

print_E(start, stop, step)
