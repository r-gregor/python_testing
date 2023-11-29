#! /usr/bin/env python3


### Name:       check_subtitles.py
### Author:     RgregoR
### Date:       2017-06-58
###
### Decription:
### Traverse trough directiries with movies and
### print out list of movies directories without srt files
###

import os, sys
import glob


os.system('clear')

gr_pwd = os.getcwd()
print("Working dir:\n", gr_pwd, "\n")

gr_mvspth = "/home/rgregor/majfajls/FILMCKI/iz-KORUZE/Movies/"
print("Checking in:\n", gr_mvspth, "\n")


for root, dirs, files in os.walk(gr_mvspth):
    for file in files:
        if file.endswith(".mp4") or file.endswith(".mkv"):
            gr_fjl = os.path.join(root, file)
            gr_d = os.path.dirname(gr_fjl)
            # print(gr_d)       # test

            gr_fe = os.path.basename(gr_fjl)
            # print(gr_fe)      # test

            gr_f, gr_e = os.path.splitext(gr_fe)
            # print(gr_f, " ... ", gr_e)    # test

            gr_f_srt =  '.'.join((gr_f, "srt"))
            # print(gr_f_srt)       # test
            
            if os.path.exists(os.path.join(root, gr_f_srt)):
                pass
                # print("SRT file exists!")
            else:
                print("There is NO SRT file in", root)



