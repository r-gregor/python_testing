#! /usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument('subject', help='The message subject', nargs=1)
parser.add_argument('body', help='The BODY of the message')

os.system('clear')

args = parser.parse_args()
print("The message subject is: " + str(args.subject) + "\n")
print("The body of the message:")
print("\n" + str(args.subject) + "\n" + str(args.body))

