#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# V1_20180116;

import os, sys
import time as tt
import datetime as dt
from dateutil import relativedelta as rlt

# importing print table --> function
import print_table_V2 as pt


# timestamp
def tms():
    return dt.datetime.now().strftime('%Y%m%d_%H%M%S')

  
# main part ==================================================================================================
# CLEAR THE SCREEN    
os.system('clear')

# MESSAGE:
print("[ {} ] -- Starting {} ...".format(tms(), sys.argv[0]))

# OUTPUT =====================================================================================================


# print full table of base list
# pt.print_full_table()

pt.less_days(12)
pt.more_days(100)
pt.is_not_in('01-12')
pt.is_in('GRE')
