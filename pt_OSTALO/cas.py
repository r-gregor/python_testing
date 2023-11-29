#! /usr/bin/env python3
# -*- coding: utf-8 -*-

## calculating time

import sys
import os

# Clear the screen
os.system('clear')

print("""
--------------------------------------------------------------------
time: 01:30:54,750

Script will convert the time to msc and add the time difference of
7 min (also converted to msc), and then display final time in
original format: hrs:min:sec,msc

All steps are going to be extensively documented for the educational
purposes.
--------------------------------------------------------------------
scriptname: cas.py (python3!)
created:	20170504
author:	 ME
--------------------------------------------------------------------
""")

# --- START TIME ---
gr_STIME = "01:30:54,750"
# gr_STIME = "00:55:32,950"
print("value of gr_STIME:", gr_STIME)


gr_STL = [t for t in gr_STIME.split(':')]
print("List gr_STL comprehended from gr_STIME:\n", gr_STL)

gr_hrs1 = gr_STL[0]
gr_min1 = gr_STL[1]
gr_sec1, gr_msc1 = gr_STL[2].split(',')

print("\nSplitting list GR_STL to time sequences ...")
print("gr_hrs1 =", gr_hrs1)
print("gr_min1 =", gr_min1)
print("gr_sec1 =", gr_sec1)
print("gr_msc1 =", gr_msc1)

print("\nConverting time sequences to single time in msc ...")

gr_stime1 = int(gr_hrs1)*(60*60*1000) + int(gr_min1)*(60*1000) + int(gr_sec1)*1000 + int(gr_msc1)
print("gr_stime1 =", gr_stime1, "miliseconds")

# --- TIME DIFFERENCE ---
print("Doing the same for time difernece: 00:07:00,000 ...")
gr_DIFF = "00:00:07,000"
gr_DTL = [t for t in gr_DIFF.split(':')]
gr_hrsd = gr_DTL[0]
gr_mind = gr_DTL[1]
gr_secd, gr_mscd = gr_DTL[2].split(',')


print("\nSplitting list gr_DTL to time sequences ...")
print("gr_hrsd =", gr_hrsd)
print("gr_mind =", gr_mind)
print("gr_secd =", gr_secd)
print("gr_mscd =", gr_mscd)

print("\nConverting time sequences to single time in msc ...")

gr_timed = int(gr_hrsd)*(60*60*1000) + int(gr_mind)*(60*1000) + int(gr_secd)*1000 + int(gr_mscd)
print("gr_timed =", gr_timed, "miliseconds")

# --- TOTAL TIME ---
print("\nAdding time difference gr_stimed to start time gr_stime1 ...")
gr_etime2 = gr_stime1 + gr_timed
print(gr_stime1, "+", gr_timed, "=", gr_etime2)

# --- CONVERSION ---
print("\nSplitting final time gr_etime2 to time sequences ...")

gr_hrse = gr_etime2/(60*60*1000)
gr_hrs2 = int(gr_hrse)
print ("Hours =", gr_hrse, "=", gr_hrs2)

gr_mine = (gr_hrse - gr_hrs2)*60
gr_min2 = int(gr_mine)
print ("Minutes =", gr_mine, "=", gr_min2)

gr_sece = (gr_mine - gr_min2)*60
gr_sec2 = int(gr_sece)
print ("Seconds =", gr_sece, "=", gr_sec2)

gr_msc2 = int((gr_sece - gr_sec2)*1000)
print ("Miliseconds=", gr_msc2)

if len(str(gr_hrs2)) < 2:
	gr_hrs2 = "0" + str(gr_hrs2)

if len(str(gr_min2)) < 2:
	gr_min2 = "0" + str(gr_min2)

if len(str(gr_sec2)) < 2:
	gr_sec2 = "0" + str(gr_sec2)

# --- FINAL TIME ---
gr_time2 = str(gr_hrs2) + ":" + str(gr_min2) + ":" + str(gr_sec2) + "," + str(gr_msc2)
print("\nEND time:", gr_time2)




