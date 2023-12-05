#! /usr/bin/env python3

string = "onetwosevenineightfour"
word_nums = ['zero','one','two','three','four','five','six','seven','eight','nine']

word = ""
nums = []
count = 0
for char in string:
    word += char
    count += 1
    for num in word_nums:
        print("string", string)
        print("word:", word)

# WORKS kinda ...
#         if word == num:
#             index = word_nums.index(word)
#             print(index)
#             nums.append(index)
#             word = ""
#             string = string[len(num):]
#             break
#         else:
#             continue

        if word == num:
            index = word_nums.index(word)
            print(index)
            nums.append(index)
            string = string[1:]
            word = ""
            break
        else:
            continue






print(nums)
