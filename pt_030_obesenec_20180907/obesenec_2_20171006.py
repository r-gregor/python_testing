#! /usr/bin/env python3

import time
import os

slika1 = """
   +---+----+
   |  /
   | / 
   |/ 
   |
   |
   |
   |
  /|\\
_/_|_\\_
"""

slika2 = """
   +---+----+
   |  /	 |
   | /
   |/
   |
   |
   |
   |
  /|\\
_/_|_\\_
"""

slika3 = """
   +---+----+
   |  /	 |
   | /	 --- 
   |/	  |_|
   |
   |
   |
   |
  /|\\
_/_|_\\_
"""

slika4 = """
   +---+----+
   |  /	 |
   | /	 --- 
   |/	  |_|
   |		|
   |		|
   |		|
   |
  /|\\
_/_|_\\_
"""

slika5 = """
   +---+----+
   |  /	 |
   | /	 --- 
   |/	  |_|
   |		|
   |	   /|\\
   |	  / | \\
   |
  /|\\
_/_|_\\_
"""

slika6 = """
   +---+----+
   |  /	 |
   | /	 --- 
   |/	  |_|
   |		|
   |	   /|\\
   |	  / | \\
   |	   / \\  
  /|\\	 /   \\   
_/_|_\\_
"""

S = [slika1,
	 slika2,
	 slika3,
	 slika4,
	 slika5,
	 slika6]

for i in range(0,6):
	os.system('clear')
	print(S[i])
	time.sleep(2)