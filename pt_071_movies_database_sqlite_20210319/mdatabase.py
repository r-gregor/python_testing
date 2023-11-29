#! /usr/bin/env python3
# -*- coding: utf-8 -*-


import sqlite3

conn = sqlite3.connect(':memory:')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS movies (
			title TEXT,
			year INTEGER,
			UNIQUE(title, year)
)""")

c.execute("INSERT INTO movies VALUES ('Conan the Barbarian', 1996)")
c.execute("INSERT INTO movies VALUES ('Cool Runnings, The beginning', 2016)")
c.execute("INSERT INTO movies VALUES ('STAR WARS', 1970)")
c.execute("INSERT INTO movies VALUES ('STAR WARS III', 1973)")
c.execute("INSERT INTO movies VALUES ('STAR TREK: NEMESYS', 2011)")

c.execute("SELECT * FROM movies")
print(c.fetchall())

c.execute("SELECT * FROM movies WHERE year=:year", {'year': 2011})
print(c.fetchall())

c.execute("SELECT * FROM movies WHERE year > 2000")
print(c.fetchall())


conn.commit()
conn.close()

