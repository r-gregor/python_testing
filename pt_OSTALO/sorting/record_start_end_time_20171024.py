
# -*- coding: utf-8 -*-

import time
import datetime

startt = datetime.datetime.now()        # record start

# ... code to execution to measure time ...

endt = datetime.datetime.now()          # record end
timedef = endt - startt                 # time difference
timedefmicro = timedef.microseconds     # convert in microseconds
print("Sorted in " + str(timedefmicro/1000) + " miliseconds.")
