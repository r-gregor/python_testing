#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# substring_recursive_test_v4.py
# 20231208_04 (en)

string = "onetllthreee  eee4sevenineig htcoolsix5four8 five"
word_nums = ["zero", "one", "two",  "three", "four", "five", "six", "seven", "eight", "nine"]
nums = []

def print_num_from_string_rec(string, nums):
	result=""
	for sub in string:
		if sub == " ":
			break

		result += sub
		for wnum in word_nums:
			if result.isdigit():
				nums.append(int(result))
				result=""
				break

			if result == wnum:
				nums.append(word_nums.index(result))
				result=""
				break
		else:
			continue
		break

	if len(string) <= 1:
		print(nums)
		return
	else:
		string = string[1:]
		print_num_from_string_rec(string, nums)

# MAIN -----------------------------------------
if __name__ == "__main__":
	print(f"string: {string}")
	print_num_from_string_rec(string, nums)

