#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# timediff.py
# 20250521 v1 en

import sys

sih = 60*60 # seconds n hour
sim = 60    # seconds in minute
secsinday = 24*60*60

T1 = "004523"
T2 = "005203"

def get_secs_in_h(T):
	H=int(T[:2])
	if H > 23:
		print(f"Hours part ({H}) is greater than 23 hours")
		sys.exit()
	return H*sih

def get_secs_in_m(T):
	M=int(T[2:4])
	if M > 59:
		print(f"Minutes part ({M}) is greater than 59 minutes")
		sys.exit()
	return M*sim

def get_secs(T):
	S=int(T[4:])
	if S > 59:
		print(f"Seconds part ({S}) is greater than 59 seconds")
		sys.exit()
	return S

if int(T2) - int(T1) <= 0:
	print("Time difference to small (under 1 sec, or negative)")
	sys.exit()


if int(T2) - int(T1) >= secsinday:
	print("Time difference to big (over one day)")
	sys.exit()

T1S = get_secs_in_h(T1) + get_secs_in_m(T1) + get_secs(T1)
T2S = get_secs_in_h(T2) + get_secs_in_m(T2) + get_secs(T2)
totals = T2S - T1S

dm, ds = divmod(totals, 60)
dh, dm = divmod(dm, 60)

print(f"The difference is: {totals} seconds ({dh} hours, {dm} minutes and {ds} seconds)")
print(f"The difference is: {dh:02}:{dm:02}:{ds:02}")

