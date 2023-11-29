#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

### version: 20151106-02
### ----------------------------------------------------------------------------
### change 20151106: change T1, T2, DIST, FF vars to float with VAR = float(VAR)
### before: wrong calculations if all vars entered from user were integeres
### ----------------------------------------------------------------------------
###


import os
os.system('clear')

# TEST
# collecting needed data: start,end,distance ...
def cal_fallf():

	gr_T1 = input("Insert START point (T1) height in [m]: ")
	gr_T2 = input("Insert END point (T2) height in [m]: ")
	gr_DIST = input("Insert distance netween points T1 and T2 in [m]: ")

	gr_T1 = float(gr_T1)
	gr_T2 = float(gr_T2)
	gr_DIST = float(gr_DIST)
	
	# CALCULATIONS:
	gr_DIFF=gr_T1 - gr_T2
	print("Vertical difference T1-T2 in [m] is:", round(gr_DIFF,3), "m")
	
	gr_FALLF=(gr_DIFF/gr_DIST)*100.0
	print("Fall factor is:", round(gr_FALLF,3), "%")
	# print("Fall factor is:", gr_FALLF, "%")
	
	print()
	print("Done!")
	print()
	return

def cal_endp():

	gr_T1 = input("Insert START point (T1) height in [m]: ")
	gr_FF = input("Insert FF in [%] +(down \), or -(up /): ")
	gr_DIST = input("Insert distance netween points T1 and T2 in [m]: ")
	
	gr_T1 = float(gr_T1)
	gr_FF = float(gr_FF)
	gr_DIST = float(gr_DIST)

	# CALCULATIONS:
	gr_FF_d = gr_FF/100.0
	gr_T2 = gr_T1 - (gr_DIST * gr_FF_d)
	gr_T2 = float(gr_T2)

	gr_DIFF = gr_T1 - gr_T2
	
	print("Vertical difference T1-T2 in [m] is:", round(gr_DIFF,3), "m")
	print("Value of END point T2 in [m] is:",round(gr_T2,3),"m")
	
	print()
	print("Done!")
	print()
	return


# Decision:
while True:
	print("""\nCalculation of fall factor:
[ 1 ] - calculating fall factor
[ 2 ] - calculating END point (T2) from given fall factor
[ q ] - quit
--------------------------------------------------------
""")
	gr_DES=input("Insert choice: ")
	
	if (gr_DES == 'q') or (gr_DES == 'Q') :
		### os.system('clear')
		print("\nYou chose to QUIT. Bye.")
		exit()
	
	
	if (gr_DES != '1') and (gr_DES != '2'):
		os.system('clear')
		print("\nWrong choice. Try again. Bye.")
		exit()
	
	gr_DES=float(gr_DES)
	
	if gr_DES == 1:
		### os.system('clear')
		print("\nCalculating fall factor")
		cal_fallf()
	
	elif gr_DES == 2:
		### os.system('clear')
		print("\nCalculating END point (T2) from given fall factor")
		cal_endp()
# END
