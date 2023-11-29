#! /usr/bin/env python3

I0 = 10000
rate = 5
perc = rate / 100
i = 0

I = I0
for year in range(0,1):
	comm = (I * (perc))
	print("{}.) {} / {}".format(i, I, comm))
	I = I + comm
	i += 1
print("{}.) {}".format(i, I))
print()

I2 = I0
i2 = 0
for year in range(0,10):
	comm = (I2 * (perc))
	print("{}.) {} / {}".format(i2, I2, comm))
	I2 = I2 + comm
	i2 += 1
print("{}.) {}".format(i2, I2))
print()

I3 = I2
i3 = 0
for year in range(0,4):
	comm = (I3 * (perc))
	print("{}.) {} / {}".format(i3, I3, comm))
	I3 = I3 + comm
	i3 += 1
print("{}.) {}".format(i3, I3))
