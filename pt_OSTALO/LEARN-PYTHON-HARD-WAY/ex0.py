#! /usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
rutina, ARG1, ARG2 = sys.argv
prompt = '> '

print("This script \"%s\" has two arguments: ARG1=\"%s\" and ARG2=\"%s\"." % (rutina, ARG1, ARG2))

print("Please enter your age ...")
age = int(input(prompt))

print("Please enter your height in centimetres ...")
height = int(input(prompt))

print("The sum of your age (%d) and your height (%d) is: %d" % (age, height, age + height))
