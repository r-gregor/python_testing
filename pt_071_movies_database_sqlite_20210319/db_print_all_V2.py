#! /usr/bin/env python3
# -*- coding: utf-8 -*-


import sqlite3

conn = sqlite3.connect('movie_database.db')
c = conn.cursor()

# c.execute("SELECT * FROM movies")
c.execute("SELECT * FROM movies ORDER BY year DESC, title ASC")
rows = c.fetchall()

cw1 = 30
cw2 = 4 
rw = cw1 + cw2
columnWidths = "{0:<"+str(cw1)+"}{1:<"+str(cw2)+"}"
print(columnWidths.format("Movie name","Year"))
print("-"*rw)
for row in rows:
	print(columnWidths.format(row[0], row[1]))


conn.commit()
conn.close()


