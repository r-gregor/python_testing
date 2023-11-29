#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# V2:   update 20190921:  have to use STRING.rstrip(<delimiter>, <num of splits>) tp split on last 'dot'
#                   returns a list!
#


import os
import sys
import shutil
import datetime as dt

# timestamp
def tms():
    return dt.datetime.now().strftime('%Y%m%d_%H%M%S')

# MESSAGE:
print("[ {} ] -- Starting {} ...".format(tms(), sys.argv[0]))

if len(sys.argv) != 3:
    print("[ {} ] -- Must supply existing *.srt  and [movie] filename".format(tms()))
    sys.exit(1)
else:
    old_srt_fname = sys.argv[1]
    existing_movie_fname = sys.argv[2]

print("[ {} ] -- Old subscripts file: {}".format(tms(), old_srt_fname))
print("[ {} ] -- Existing movie file: {}".format(tms(), existing_movie_fname))

def chkf(fname):
    if os.path.isfile(fname):
        print("[ {} ] -- {} exists. It's OK to proceede".format(tms(), fname))
    else:
        print("[ {} ] -- There is NO: {}".format(tms(), fname))
        sys.exit(1)


for FN in [old_srt_fname, existing_movie_fname]:
    chkf(FN)

new_srt_fname_base = existing_movie_fname.rsplit(".", 1)[0]
new_srt_ext = "srt"
new_srt_fname = new_srt_fname_base + "." + new_srt_ext

print("[ {} ] -- Copying {} to {}".format(tms(), old_srt_fname, new_srt_fname))
shutil.copy2(old_srt_fname, new_srt_fname)

print("[ {} ] -- Done\n".format(tms()))
