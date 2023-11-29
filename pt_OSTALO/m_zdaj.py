# zdaj.py
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------------
# import datetime module to display different date-time -stamps; convert
# stamps to strings, so they can be concatenated to the end of filename
# string, like: long-file-name_[date-time-stamp].txt. For now separate
# current date and time part with hypen [-] (also possible with '..' or 
# '@', ...
#
# import in the main program:
# import zdaj --> variables need to be accesed by reference: [ zdaj.gr_VARNAME ]
# from zdaj import * -- > variables can be accest just by their name: [ gr_VARNAME] 
# -----------------------------------------------------------------------------------
# datetime.now()	-->	current date,time
# strftime('...')	-->	stringformat for date,time, must be between parentheses!
# 				%Y, %m, %d [YYYY, mm, dd]
# 				%H, %M, %S [hh, mm, ss]
# 
# -----------------------------------------------------------------------------------



from datetime import datetime
gr_CURRD=datetime.now().strftime('%Y%m%d')
gr_CURRT=datetime.now().strftime('%H%M')
gr_CURRTL=datetime.now().strftime('%H%M%S')

gr_DANES=str(gr_CURRD)
gr_ZDAJ=str(gr_CURRT)
gr_ZDAJL=str(gr_CURRTL)

gr_TSTMP=gr_DANES + "-" + gr_ZDAJ
gr_TSTMPL=gr_DANES + "-" + gr_ZDAJL

### TEST -----------------------------------------------
### print("Current date [YYYYmmdd]:", gr_CURRD)
### print("Current time - short [HHMM]:", gr_CURRT)
### print("Current time - long [HHMMSS]:", gr_CURRTL)
### print("Timestamp:", gr_TSTMP)
### print("Timestamp - long:", gr_TSTMPL)
### TEST -----------------------------------------------

