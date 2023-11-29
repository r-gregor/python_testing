#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Draw a romb

Draw a romb with the use of for loops

"""


# <code>
K = 8
for N in range(K):
	print(" "*(K-1) + "/" + " "*N*2 + "\\")
	K -= 1

K = 8
for N in range(K):
	print(" "*N + "\\" + " "*(K-1)*2 + "/")
	K -= 1
# </code>

"""
result:
$> gregor.redelonghi@cygwin-en [/home/gregor.redelonghi]
$> python3 ~/_BRISI/romb.py
	   /\
	  /  \
	 /	\
	/	  \
   /		\
  /		  \
 /			\
/			  \
\			  /
 \			/
  \		  /
   \		/
	\	  /
	 \	/
	  \  /
	   \/
"""
