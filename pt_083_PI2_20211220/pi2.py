import math

def sum(N):
	sum = 1
	for i in range(2,N):
		sum += 1/i**2
	return sum

if __name__ == "__main__":

	print("Calculating PI using formulae: (PI^2)/6 = 1 + 1/2^2 + 1/3^2 + 1/4^2 + ...")

	iterations = int(1E8)
	print("{:.80f}".format(math.sqrt(sum(iterations)*6)))
