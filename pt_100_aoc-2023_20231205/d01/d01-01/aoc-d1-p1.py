#! /usr/bin/env python3

nums = []
lines = []
# fname = 'example-01.txt'
fname = 'input'
with open(fname, 'r') as f:
	for line in f.readlines():
	   lines.append(line)

# test
# print(lines)

for line in lines:
	num_per_line = []
	for char in line[::]:
		if char.isdigit():
			num_per_line.append(char)

			break
	for char in line[::-1]:
		if char.isdigit():
			num_per_line.append(char)
			break
	num = int(num_per_line[0] + num_per_line[1])
	nums.append(num)

print("nums: ", end="")
for num in nums[:-1]:
	print(num, end=", ")
print(nums[-1])

print("sum: ", sum(nums))

