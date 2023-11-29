#! /usr/bin/env python3
# -*- coding: utf-8 -*-

print('''A problem:
A function will take in two parameters consist of a string,
each string consists of the exclamation mark and the question mark.
Each exclamation mark weight is 2; Each question mark weight is 3.
Sum up all the character values that consist of a question mark and
exclamation mark on the left parameter and the right parameter,
if the left side is heavier, return “Left”; If the right side is
heavier, return “Right”; If they are balanced, return “Balance”.
''')

def balance(left, right):
 
	left_i = list(left)
	right_i = list(right)
	left_sum = calculate(left_i)
	right_sum = calculate(right_i)
 
	if(left_sum > right_sum):
		return "Left"
	elif(left_sum < right_sum):
		return "Right"
	else:
		return "Balance"
 
def calculate(a_list):
	sum = 0
	 
	for i in range(len(a_list)):
		if(a_list[i] == '!'):
			sum += 2
		elif(a_list[i] == '?'):
			sum += 3
	return sum

print("Test:")
leftw = "!word1?"
rightw = "??word2!"
print("Balance the words left=[" + leftw + "] and right=[" + rightw + "]:", balance(leftw, rightw))


print("\nLOOP:")
wrds = [	("!W1!", "?W2?"),
			("!?W1?!", "?!W2!?"),
			("!!W1??", "??W2!!"),
			("!W?1!", "?W?2!"),
			("!W?1??", "?W?2!"),
			("W1", "W2")]

for el in wrds:
	leftw = el[0]
	rightw = el[1]
	print("Balance the words left=[" + leftw + "] and right=[" + rightw + "]:", balance(leftw, rightw))