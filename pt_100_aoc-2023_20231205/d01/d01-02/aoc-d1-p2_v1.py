#! /usr/bin/env python3

nums = []
lines = []
fname = 'example2.txt'
# fname = 'input'
with open(fname, 'r') as f:
    for line in f.readlines():
       lines.append(line.strip())

# test
print(lines)

word_nums = ['zero','one','two','three','four','five','six','seven','eight','nine','ten']

print("index of four:", word_nums.index('four'))

for line in lines:
    num_per_line = []
    word = ""
    for char in line[::]:
        if char.isdigit():
            num_per_line.append(int(char))
            word = ""
            continue
        else:
            word += char
            for num in word_nums:
                if word in num:
                    if word == num:
                        num_per_line.append(word_nums.index(word))
                        word = char
                        print(word)
                    else:
                        continue
                else:
                    print(word)
                    continue

    print(num_per_line)
    print("---")
#    for char in line[::-1]:
#        if char.isdigit():
#            num_per_line.append(char)
#            break
#    num = int(num_per_line[0] + num_per_line[1])
#    nums.append(num)

# print("nums: ", end="")
# for num in nums[:-1]:
#     print(num, end=", ")
# print(nums[-1])

# print("sum: ", sum(nums))

