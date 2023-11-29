#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import random as rn


s_stop = "n"
s_num = rn.randint(1,20)
its = 0

while True:
	ans = input("Quess the number between 1 and 20, or enter q to quit: __ ")
	its += 1
	if ans == "q":
		break

	elif int(ans) == s_num:
		if its >= 5:
			print("\nYou guest it, but in " + str(its) + " tries. NOT so good!")
			break
		else:
			print("\nGood job! you guessed the number " + str(s_num) + " in " + str(its) + " tries!")
			break

	else:
		if int(ans) > s_num:
			print("Too high!")
		elif int(ans) < s_num:
			print("Too low!")


