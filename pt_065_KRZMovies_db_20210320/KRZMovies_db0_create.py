#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
import sys


db = "KRZMovies.db"
MFile = 'KRZMovies-list_20210320.txt'
MoviesDict = {}
with open(MFile, "r") as ff:
    for line in ff.readlines():
        print(line.strip())
        oneLine = line.strip().split(" ")
        Mname = " ".join(oneLine[:-1])
        Myear = oneLine[-1].replace("(", "").replace(")", "")
        MoviesDict[Mname] = Myear

# print(MoviesDict)

conn = sqlite3.connect(db)
cr = conn.cursor()

# create table
cr.execute("""CREATE TABLE IF NOT EXISTS movies (
		title TEXT,
		year INTEGER,
        UNIQUE(title, year)
)""")

conn.commit()
conn.close()

for ttl, yr in MoviesDict.items():
    values = (ttl, yr)
    conn = sqlite3.connect(db)
    cr = conn.cursor()
    cr.execute("INSERT INTO movies(title, year) VALUES(?, ?)", values)
    conn.commit()
    conn.close()


