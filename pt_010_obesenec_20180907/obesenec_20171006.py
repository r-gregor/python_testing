#! /usr/bin/env python3

import time


L1  =  "   +---+----+"
L2  =  "   |  /	 |"
L3  =  "   | /	 ---" 
L4  =  "   |/	  |_|"
L5  =  "   |		|"
L6  =  "   |	   /|\\"
L7  =  "   |	  / | \\"
L8  =  "   |	   / \\ "  
L9  =  "  /|\\	 /   \\"   
L10 =  "_/_|_\\_"

S = [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10]

for i in range(0,10):
	time.sleep(1)
	print(S[i])

