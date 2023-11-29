#! /usr/bin/env python3
# -*- coding: utf-8 -*-

S = ["00:59:55,000 --> 01:25:22,780", "01:26:59,478 --> 01:45:02,405", "02:58:00,999 --> 04:08:42,012", "12:22:45,000 --> 13:00:00,000"]

print("List S = ", S, "\n")

dT = 5.5
dTs = int(dT * 60)
print("Time difference - dT =", dT, "minutes.")
print("Time difference - dT =", dTs, "seconds.")

def disp_time(T):
	
	for S in T:

		print("------------------------------------------------------------ ")
		print("Total time period:", S)
		
		Ss, Se = S.split(' --> ')
		print("Start time - Ss:", Ss)
		print("End time - Se:  ", Se)
		
		print()
		print("Splitting time to H, M, S, ...")
		H1, M1, S1 = Ss.split(':')
		H2, M2, S2 = Se.split(':')
		S11, S12 = S1.split(",")
		S21, S22 = S2.split(",")
		
		
		print("H1 =", H1)
		print("M1 =", M1)
		print("S11 =", S11)
		print("S12 =", S12)
		
		"""
		print("H2 =", H2)
		print("M2 =", M2)
		print("S21 =", S21)
		print("S22 =", S22)
		"""

		S11d0 = int(S11) + dTs
		if S11d0 >= 60:
			print("S11d0 biger as 60 sek ...")
			S11d = (S11d0/60 - int(S11d0/60))*60
			S11d = int(round(S11d,1))
			Mp1 = int(S11d0/60)
			if S11d < 10:
				S11d = "0" + str(S11d)
			M1d = int(M1) + Mp1

		else:
			print("S11d0 not bigger as 60 sek ...")
			S11d = S11d0
			M1d = M1

		if M1d >= 60:
			print("M1d - bigger as 60 min ...")
			Hp1 = int(M1d/60)
			M1d = int(((M1d)/60 - int(M1d/60))*60)
			H1d = int(H1) + Hp1
			if M1d < 10:
				M1d = "0" + str(M1d)
			
			if H1d < 10:
				H1d = "0" + str(H1d)

		else:
			H1d = H1
		
		print("S11d =", S11d)
		print("M1d =", M1d)
		print("H1d =", H1d)

		



		S1d = ",".join([str(S11d), str(S12)])
		T1d = ":".join([str(H1d), str(M1d), str(S1d)]) 
		print("Changed start time T1d:", T1d)

disp_time(S)

