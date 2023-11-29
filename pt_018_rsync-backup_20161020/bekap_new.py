#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import time


# VARIABLES ------------------------------
### gr_doma = "/home/rgregor/majfajls/BIN/PYTHON-en_testing/20161020_rsync-backup"
### gr_doma = "/home/gregor.redelonghi/RUT/home/rgregor/PYTHON-en_testing/20161020_rsync-backup"
gr_doma = "/home/gregor.redelonghi/majfajls/coding/testing-en/PYTHON-en_testing/20161020_rsync-backup"

gr_src_dirname = "source_directory_A"
gr_dest_dirname = "destination_directory_B"

gr_src_dir = gr_doma + "/" + gr_src_dirname
gr_dest_dir = gr_doma + "/" + gr_dest_dirname


# FUNCTIONS ------------------------------
def nl():
	print("")

def ask():
	input("--> Pres any key to continue ...")


### BEGIN THE SCRIPT ### -------------------------------------------
# CLEAR the screen ...
subprocess.call("clear")

# test if there is DOMA ...
if os.path.isdir(gr_doma):
	print("DOMA = " + gr_doma)
else:
	print("There is no \"" + gr_doma + "\"!")
	print("Try again. Bye")
	quit()

# chdir to DOMA ...
os.chdir(gr_doma)
gr_curd = os.getcwd()
print("Current location :" + gr_curd)

ask()

# just a test if no ...
# os.chdir("/home/gregor.redelonghi")
# print("Current location :", os.getcwd())

nl()
# test if in DOMA ...
if gr_doma != os.getcwd():
	print("We are not in DOMA!")
	print("Try again. Bye!")
	quit()
else:
	print("We are in DOMA, and good to go ...")

ask()

nl()
# test if src and dest dirs exist ...	
if os.path.isdir(gr_src_dirname):
	print(gr_src_dirname + " = OK")
	if os.path.isdir(gr_dest_dirname):
		print(gr_dest_dirname + " = OK")
	else:
		print("But there is no " + gr_dest_dirname + "...")
		print("Try again. Bye!")
		quit()
else:
	print("No luck! There is no " + gr_src_dirname + "...")
	print("Try again. Bye!")
	quit()

ask()

# TEST
# print the command ...
nl()
print("Executing rsync script ...(SRY RUN)")
print("rsync -avn --progress " + gr_src_dir + "/ " + gr_dest_dir + "/")
subprocess.call(["rsync", "-avn", "--progress", gr_src_dir + "/", gr_dest_dir + "/"])

ask()
# actual COMMAND ...
nl()
print("Executing rsync script ...")
print("rsync -av --progress " + gr_src_dir + "/ " + gr_dest_dir + "/")
subprocess.call(["rsync", "-av", "--progress", gr_src_dir + "/", gr_dest_dir + "/"])

### END ### --------------

