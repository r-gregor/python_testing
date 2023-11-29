import math

nums = [12345678, 123456789, 223355, 11221122, 9999999999, 12000021, 1000000999000001]
def num_and_sum(_num):
	num_of_digits = 0
	sum_of_digits = 0

	while not _num < 1:
		num_of_digits += 1
		sum_of_digits += int(_num % 10)
		_num = _num/10
		
	return (num_of_digits, sum_of_digits)

def display_num_and_sum(_num):
	num1, sum1 = num_and_sum(_num)
	print(f"Num of digits in {_num} is: {num1}")
	print(f"Sum of digits in {_num} is: {sum1}")
	print("---")


if __name__ == "__main__":
	for i in nums:
		display_num_and_sum(i)
