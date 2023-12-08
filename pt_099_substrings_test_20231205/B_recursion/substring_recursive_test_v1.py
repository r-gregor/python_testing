#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# substring_recursive_test_v1.py
# 20231208_01 (en)

string = "onetwothree4sevenineightsix5four8five"

def print_rec_descending(string):
	print(string)
	if len(string) <= 0:
		return
	else:
		string = string[1:]
		print_rec_descending(string)

def print_ascending(string):
	result=""
	for sub in string:
		result += sub
		print(result)

def print_substring_descending_rec(string):
	result=""
	for sub in string:
		result += sub
		print(f"curent substring: {result}")
	print("---")
	if len(string) <= 1:
		return
	else:
		string = string[1:]
		print_substring_descending_rec(string)


# MAIN -----------------------------------------
if __name__ == "__main__":
	print(f"string: {string}")
	# print_rec_descending(string)
	# print_ascending(string)
	print_substring_descending_rec(string)

