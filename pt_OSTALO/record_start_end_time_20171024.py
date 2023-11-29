
# -*- coding: utf-8 -*-

import time
import datetime as dtt

startt = dtt.datetime.now()			 # record start

# ... code to execution to measure time ...
endt = dtt.datetime.now()			   # record end
timedef = endt - startt				 # time difference
tmdfs = timedef.total_seconds()	 # convert in microseconds
print("Sorted in {} seconds".format(tmdfs))
