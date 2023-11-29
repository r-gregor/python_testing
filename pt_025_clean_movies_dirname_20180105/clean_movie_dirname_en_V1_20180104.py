#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# version: V1
# date: 20180104
# clean movie dirname

S = "The Terminator (2017) [YTS-AG] "
# S = "The Terminator (2017)  "

lng = len('Changing:')
numl = lng + len(S) + 3 # 3 --> 1 spaces + quotes

print("{} {}".format("Changing:".rjust(lng), ("'" + S + "'")))

if '[YTS-AG]' in S:
	S2 = S.replace('[YTS-AG]', '').strip()
else:
	S2 = S.strip()

print("{} {}".format("To:".rjust(lng), ("'" + S2 + "'")))
print("-"*numl)
