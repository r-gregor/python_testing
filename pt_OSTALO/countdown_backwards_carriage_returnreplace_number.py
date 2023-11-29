#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import time	 # only needed for backwards countdown


print("\nWaiting 10 seconds to proceed ...")

# countdown - replace
for T in range(9,0,-1):
	print(" " + str(T), end= "\r")
	time.sleep(1)
