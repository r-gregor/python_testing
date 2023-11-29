#! /uer/bin/env python3

def power_of_two(pwr):
	if pwr <=32:
		offset = 14
	else:
		offset = 26

	num = 2**pwr
	snum = str(int(num))
	# test
	# print(snum)
	rsnum = snum[::-1]

	rfinal = []
	digits = 1
	count = 0
	N = len(rsnum) - 1
	while N >= 0:
		if digits % 3 == 0 and N != 0:
			rfinal.append(rsnum[count])
			rfinal.append(".")
			count += 1
			digits += 1
			N -= 1
		else:
			rfinal.append(rsnum[count])
			digits += 1
			count += 1
			N -= 1
	print("2^{:<2} = ".format(pwr), end="")
	print(("".join(rfinal[::-1])).rjust(offset))

if __name__ == "__main__":
	for pwr in range(1,33):
		power_of_two(pwr)
	print("---------------------------------")

	power_of_two(8)
	power_of_two(16)
	power_of_two(32)

	print("---------------------------------")
	power_of_two(48)
	power_of_two(56)
	power_of_two(64)

