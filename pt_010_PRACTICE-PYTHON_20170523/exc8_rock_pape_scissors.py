#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys
os.system('clear')

"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
compare them, print out a message of congratulations to the winner,
and ask if the players want to start a new game)

Remember the rules:
	Rock beats scissors
	Scissors beats paper
	Paper beats rock
"""
while True:
	elements = ["ROCK", "SCISSORS", "PAPER", "QUIT"] 
   
	WIN1 = """
+----------------+
| PLAYER-1 wins! |
+----------------+
"""
	WIN2 = """
+----------------+
| PLAYER-2 wins! |
+----------------+
"""
	 
	print()
	print("This is Rock, Paper, Scissors game. To exit enter: quit")
	ans1 = input("PLAYER-1: enter Rock, Paper or Scissors: __ ")
	ans1 = str(ans1.upper())
	
	ans2 = input("PLAYER-2: enter Rock, Paper or Scissors: __ ")
	ans2 = str(ans2.upper())

	if ans1 == "QUIT" or ans2 == "QUIT":
		 print("You chouse to QUIT. Bye!")
		 break

	if ans1 not in elements or ans2 not in elements:
		print("Wrong input!")
		break


#	 print("PLAYER-1:", ans1)
#	 print("PLAYER-2:", ans2)


	def compare(ans1, ans2): 
		if ans1 == ans2:
			return("ITS A TIE!")

		if ans1 == "ROCK":
			if ans2 == "SCISSORS":
				return(WIN1)
			else:
				return(WIN2)
		
		if ans1 == "PAPER":
			if ans2 == "SCISSORS":
				return(WIN2)
			else:
				return(WIN1)

		if ans1 == "SCISSORS":
			if ans2 == "ROCK":
				return(WIN2)
			else:
				return(WIN1)
	
	print(compare(ans1, ans2))

