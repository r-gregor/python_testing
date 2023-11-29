#! /usr/env/bin python3

from chardet.universaldetector import UniversalDetector

FJL = 'Spectre.2015.DVDScr.XVID.AC3.HQ.Hive-CM8.srt'

f = open(FJL, 'rb')
detector = UniversalDetector()
for line in f.readlines():
    detector.feed(line)
    if detector.done: break
detector.close()
f.close()
print(detector.result)