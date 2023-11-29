#! /usr/bin/env python3

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
		S1a, S1b = S1.split(",")
		S2a, S2b = S2.split(",")
	   
		print("H1 =", H1)
		print("M1 =", M1)
		print("S1a =", S1a)
		print("S1b =", S1b)
		
		"""
		print("H2 =", H2)
		print("M2 =", M2)
		print("S2a =", S2a)
		print("S2b =", S2b)
		"""

		S1ad0 = int(S1a) + dTs
		if S1ad0 >= 60:
			print("S1ad0 biger as 60 sek ...")
			S1ad = (S1ad0/60 - int(S1ad0/60))*60
			S1ad = int(round(S1ad,1))
			Mp1 = int(S1ad0/60)
			if S1ad < 10:
				S1ad = "0" + str(S1ad)
			M1d = int(M1) + Mp1

		else:
			print("S1ad0 not bigger as 60 sek ...")
			S1ad = S1ad0
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
		
		print("S1ad =", S1ad)
		print("M1d =", M1d)
		print("H1d =", H1d)

		



		S1d = ",".join([str(S1ad), str(S1b)])
		T1d = ":".join([str(H1d), str(M1d), str(S1d)]) 
		print("Changed dtart time T1d:", T1d)

disp_time(S)

