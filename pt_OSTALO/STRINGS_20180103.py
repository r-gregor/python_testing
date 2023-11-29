#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# date: 20180104
# clean movie folder

S = "The Terminator (2017) [YTS-AG]"
print(S)

if '[YTS-AG]' in S:
	S2 = S.replace('[YTS-AG]', '')
else:
	S2 = S

print(S2)
