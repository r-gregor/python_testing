#! /usr/bin/env python3

string = "onetwosevenineightfour"
word_nums = ['zero','one','two','three','four','five','six','seven','eight','nine']
nums = []
size = len(string)
word = ""

print("string:", string)

while size > 0:
    string = string[len(string) - size:]
    for char in string:
        word += char
        print("string:", string)
        print("word:", word)

        for num in word_nums:
            if word == num:
                nums.append(word_nums.index(num))
                break
        else:
            continue # only executed if the inner loop did NOT break
        break        # only executed if the inner loop DID break


    size -= 1
    word = ""
print(nums)
