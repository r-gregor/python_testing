#! /usr/bin/env python3
# -*- coding: utf-8 -*-


import sqlite3

db = "KRZMovies.db"
conn = sqlite3.connect(db)
cr = conn.cursor()

# c.execute("SELECT * FROM movies")
cr.execute("SELECT * FROM movies ORDER BY year DESC, title ASC")
rows = cr.fetchall()

columnWidths = "{0:<6}{1}"
for row in rows:
	print(columnWidths.format(str(row[1]) + ":", row[0]))

conn.close()
