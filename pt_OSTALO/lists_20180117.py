#! /usr/bin/env python3

L1 = [1, 2, 3, 4, [5, 6], [7, [8, 9], 10], 11]
L2 = []
L3 = []

print(L1)

lvl = 1
N = 0

def disp(N, EL):
	print("This is element {} in level {}: {}".format(N, lvl, EL))

print("-"*80)	 
for EL in L1:
	disp(N, EL)
	N += 1
	
	if isinstance(EL, list):
		for EL2 in EL:
			L2.append(EL2)
			
		for EL3 in L2:
			if isinstance(EL3, list):
				for EL4 in EL3:
					L3.append(EL4)


print("-"*80)				   
for i in 1, 2, 3:
	print("L{}: {}".format(i, eval("L" + str(i))))

					
print("-"*80)		   
lvl = 2
N = 0
for EL in L2:
	disp(N, EL)
	N += 1

print("-"*80)	
lvl = 3
N = 0
for EL in L3:
	disp(N, EL)
	N += 1