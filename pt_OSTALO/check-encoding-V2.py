#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys, chardet
a = open(sys.argv[1]).read()
print(chardet.detect(a))
