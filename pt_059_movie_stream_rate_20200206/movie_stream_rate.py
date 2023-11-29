#!/usr/bin/env python
# coding: utf-8

import sys

"""
MS = 6 GB: movie size in GB --> MB = GB * 1024 --> Mb = MB * 8 --> MS = 6 * 1024 * 8[Mbit]
timem = 90 min: duration in minutes --> times = timem * 60 [sec]

rate =       (MS * 1024 * 8) / (timem * 60)
[Mbit/sec] = [Mbit]          / [sec] 

source: https://entertainment.howstuffworks.com/fast-internet-connection-for-streaming-hd-movies1.htm
"""

'''
def rate2(MS, timem):
    rate = (MS * 1024 * 8) / (timem * 60)
    print(("Movie size: {} GB\n" +
           "Dration:    {} min.\n" +
           "Rate:       {:.3f} Mbit/s\n").format(MS, timem, rate))
'''
numc = len("\tUsage:\n\t" + sys.argv[0] + " [movies size in GB] [duration in minutes]\n")
crta = "="*numc

usage = (   crta + 
            "\n" +"\tUsage:\n\t" + sys.argv[0] + " [movies size in GB] [duration in minutes]\n" + 
            "\n" + "\tIf NO parameters: test print.\n" +
            crta)

def rate(MS, timem):
    rate = float(MS * 1024 * 8) / float(timem * 60)
    line = ("Movie size: {} GB\n" +
            "Dration:    {} min.\n" +
            "Rate:       {:.2f} Mbit/s\n").format(MS, int(timem), rate)
    print(line)
    
def showAll():
    rate(6, 60)
    rate(2.8, 120)
    rate(4.2,120)

    print("101 minutes -- average movie length")
    rate(4.2, 101)

    print("average BlueRay 120 min movie = 15 - 25 GB")
    for DVD1080p in [10, 15, 20, 25]:
        rate(DVD1080p, 120)

    print("average HD 720p 101 min movie = 0.8 - 1.4 GB")
    for DVD720p in [0.80, 1.2, 1.4]:
        rate(DVD720p, 101)

myMS = 0.0
mytimem = 0

if len(sys.argv) == 1:
    showAll()
    
elif sys.argv[1] == "h":
    print(usage)
    sys.exit

elif len(sys.argv) == 3:
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    try:
        myMS = float(arg1)
        mytimem = float(arg2)
        print("Custom parameters calculation:")
        rate(myMS, mytimem)
        
    except ValueError:
        print("Wrong parameter type!")
        print(usage)
        sys.exit

else:
    print("Wrong number of parameters!")
    print(usage)
    sys.exit
