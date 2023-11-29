#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# filename: softlink1_fname_to_ulb.py
# version: V1 (20190131)

import os, sys
import subprocess
import datetime as dt

# timestamp
def tms():
	return dt.datetime.now().strftime('%Y%m%d_%H%M%S')

# USAGE
my_usage = '''
		Usage: ssoftlink1_fname_to_ulb.py [filename]

		[filename]	  existing filename (relatve, or absolute path)
'''


# CLEAR the screen ...
subprocess.call("clear")


# FUNCTIONS ==============================================================

def crtice():
	print("[ {} ] -- ".format(tms()) + "-"*80)


def done():
	print("[ {} ] -- ".format(tms()) + "Done")
	crtice()

# FUNCTIONS ==============================================================

# MAIN
print("[ {} ] -- ".format(tms()) + "Starting {} ...".format(sys.argv[0]))

# check if filename supplied as argument
if len(sys.argv) != 2:
	print("[ {} ] -- ".format(tms()) + "Filename must be supplied as argument!")
	print(my_usage)
	sys.exit()

file = sys.argv[1]

# check if file exists
if not os.path.isfile(file):
	print("[ {} ] -- ".format(tms()) + "File [ {} ] NOT found!".format(file))
	sys.exit()

file_abs_path = os.path.abspath(file)
file_path, fname_full = file_abs_path.rsplit("/", 1)
fname, ext = fname_full.rsplit(".", 1)

source_path = file_path + "/"
dest_path = "/usr/local/bin/"


# test --------------------------------------------------------------------------------------
D = {"file":file, "file_path":file_path, "fname_full":fname_full, "fname":fname, "ext":ext, "source_path":source_path, "dest_path":dest_path}

crtice()
for key, value in D.items():
	print("[ {} ] -- ".format(tms()) + "{:<15}{}".format(key + ":", value))
# test --------------------------------------------------------------------------------------	
	
crtice()
print("[ {} ] -- ".format(tms()) + "COMMAND:\n\n\tln -s -v " + source_path + fname_full + " " + dest_path + fname + "\n")
my_ans = input("[ {} ] -- ".format(tms()) + "RUN? enter 'run' to run or anything else to stop: ")

if not my_ans == "run":
	print("You chose to quit.")
	sys.exit()

print("[ {} ] -- ".format(tms()) + "Running ...\n")
my_command = subprocess.call(["ln", "-s", "-v", source_path + fname_full, dest_path + fname])
print()
print("[ {} ] -- ".format(tms()) + "Done!")






