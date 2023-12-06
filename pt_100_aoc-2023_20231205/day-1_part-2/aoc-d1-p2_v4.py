#! /usr/bin/env python3

word_nums = ['zero','one','two','three','four','five','six','seven','eight','nine']
lines = []
nums_sum = 0

# fname = 'example2.txt'
fname = 'input'


def get_nums_from_string(string):
    size = len(string)
    word = ""
    while size > 0:
        string = string[len(string) - size:]
        for char in string:

            if char == " ":
                continue

            word += char
            # print("string:", string)
            # print("word:", word)

            if word.isdigit():
                nums.append(int(word))
                word=""
                break

            for num in word_nums:
                if word == num:
                    nums.append(word_nums.index(num))
                    break
            else:
                continue # only executed if the inner loop did NOT break
            break         # only executed if the inner loop DID break


        size -= 1
        word = ""
    return nums

def first_and_last_num(nums):
    num_digits = str(nums[0]) + str(nums[-1])
    return num_digits

# MAIN ------------------------------------------------------------------
if __name__ == "__main__":

    with open(fname, 'r') as f:
        for line in f.readlines():
            lines.append(line.strip())

    # test
    # print(lines)

    for line in lines:
        nums = []
        nums = get_nums_from_string(line)
        # print("nums in line:", nums)
        num_from_line = int(first_and_last_num(nums))
        # print("1st & last:  ", num_from_line)
        nums_sum += num_from_line
        # print("---")

    print("Sum of all 2-digit numbers:", nums_sum)

