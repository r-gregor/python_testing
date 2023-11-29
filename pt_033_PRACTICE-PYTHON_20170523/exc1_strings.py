#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os

os.system('clear')
gr_curyr = 2017
gr_name = str(input("Enter your name: __ "))
gr_age = int(input("Enter your age (must be integer!): __ "))

gr_ENDT = 100
gr_TDIF = 100 - gr_age
gr_ENDYR = gr_curyr + gr_TDIF


print("\n--- response ---")
print("Hello " + gr_name +  "! Welcome to my python program.")
print("The intersting fact: you are going to be a 100 years old " + str(gr_TDIF) + " years from now.")
print("That is in year " + str(gr_ENDYR) + ".")
print("Bye!")
