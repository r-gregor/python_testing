#! /usr/bin/env python3
# -*- coding: utf-8 -*-


import sqlite3

conn = sqlite3.connect('movie_database.db')
c = conn.cursor()

c.execute("SELECT * FROM movies")
print(c.fetchall())


# c.execute("SELECT * FROM movies WHERE year=?", (2000,))
# print(c.fetchall())

# OR:
c.execute("SELECT * FROM movies WHERE year=:year", {'year': 2000})
print(c.fetchall())

conn.commit()
conn.close()


