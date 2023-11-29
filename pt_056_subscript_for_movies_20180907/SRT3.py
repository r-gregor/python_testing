#! /usr/bin/env python3

S = ["00:59:55,000 --> 01:25:22,780", "01:26:59,478 --> 01:45:02,405", "02:58:00,999 --> 04:08:42,012", "12:22:45,000 --> 13:00:00,000", "00:00:00,000 --> 00:01:59,000", "00:46:33,562 --> 00:47:52,002", "01:35:02,999 --> 01:58:00,504", "02:00:58,444 --> 02:01:01,010"]

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
		# Splitting time to H, M, S, ...
		H1, M1, S1 = Ss.split(':')
		H2, M2, S2 = Se.split(':')
		S1a, S1b = S1.split(",")
		S2a, S2b = S2.split(",")
	   
		def calculate(H1, M1, S1a, S1b):
			# print("H1 =", H1)
			# print("M1 =", M1)
			# print("S1a =", S1a)
			# print("S1b =", S1b)
			
			
			S1ad0 = int(S1a) + dTs
			if S1ad0 >= 60:
				# print("S1ad0 biger as 60 sek ...")
				S1ad = (S1ad0/60 - int(S1ad0/60))*60
				S1ad = int(round(S1ad,1))
				Mp1 = int(S1ad0/60)
				M1d = int(M1) + Mp1

			else:
				# print("S1ad0 not bigger as 60 sek ...")
				S1ad = S1ad0
				M1d = M1

			if M1d >= 60:
				# print("M1d - bigger as 60 min ...")
				Hp1 = int(M1d/60)
				M1d = int(((M1d)/60 - int(M1d/60))*60)
				H1d = int(H1) + Hp1
			else:
				H1d = H1
			
			if int(S1ad) < 10:
				S1ad = "0" + str(int(S1ad))
			
			if int(M1d) < 10:
				M1d = "0" + str(int(M1d))
			   
			if int(H1d) < 10:
				H1d = "0" + str(int(H1d))

		   
			# print("S1ad =", S1ad)
			# print("M1d =", M1d)
			# print("H1d =", H1d)

			



			S1d = ",".join([str(S1ad), str(S1b)])
			T1d = ":".join([str(H1d), str(M1d), str(S1d)]) 
			# print("Changed dtart time T1d:", T1d)
			return(T1d)
		
		print("End time with offset of", dT, "minutes (" + str(dTs) + " seconds)")
		print(calculate(H1, M1, S1a, S1b) + " --> " + calculate(H2, M2, S2a, S2b))

disp_time(S)

