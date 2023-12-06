#! /usr/bin/env python3

# string = "onetwo6sevenineight3four"
# string = "onetwo6drgttsevenineightiqhpfc3four"
string = "2onethree6twodrgttsevenineightiqhpfc3four"
word_nums = ['zero','one','two','three','four','five','six','seven','eight','nine']
nums = []


def get_nums_from_string(string):
    size = len(string)
    word = ""
    while size > 0:
        string = string[len(string) - size:]
        for char in string:
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
            break        # only executed if the inner loop DID break


        size -= 1
        word = ""
    return nums

def first_and_last_num(nums):
    num_digits = str(nums[0]) + str(nums[-1])
    return num_digits



if __name__ == "__main__":
    nums = get_nums_from_string(string)
    print("string:", string)
    print("digits:", nums)
    print("number:", first_and_last_num(nums))

