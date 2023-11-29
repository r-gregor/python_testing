#! /usr/bin/python2
# -*- coding: utf-8 -*-

# importing python modules:
print("Importing modules...")
import os
import argparse


# Parsing arguments: subject, body:
parser = argparse.ArgumentParser()

parser.add_argument('subject', help='The message subject')
parser.add_argument('body', help='The BODY of the message')
args = parser.parse_args()


parser.add_argument('--foo', help='foo help')
args = parser.parse_args()

