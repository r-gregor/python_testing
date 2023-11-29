#! /usr/bin/env python3
# -*- coding: utf-8 -*-


import sqlite3
import sys

if len(sys.argv) != 3:
	print("Must supply <title> and <year> as parameters!")
	sys.exit(1)


mTitle = sys.argv[1]
mYear = sys.argv[2]

conn = sqlite3.connect("movie_database.db")
c = conn.cursor()
# c.execute("INSERT INTO movies (title, year) VALUES (?, ?)", (mTitle, mYear))
# c.execute("INSERT INTO VALUES (:title, :year)", {'title': mTitle, 'year': mYearr})
c.execute("INSERT INTO movies VALUES (?, ?)", (mTitle, mYear))
conn.commit()
conn.close()

print(f'Added "{mTitle} ({mYear})" to the database.')

