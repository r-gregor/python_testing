#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# imports
import os, sys
import time as tt
import datetime as dt
from pathlib import Path

heref = (Path(__file__)).resolve()
here = heref.parent
print(str(here))
extf = os.path.join(here, "ROJSTNIDNEVI.txt")

print(str(extf))
# here2 = os.readlink(here)
# print(str(here2))

# extf = (here/"ROJSTNIDNEVI.txt").resolve()
# print(extf)
