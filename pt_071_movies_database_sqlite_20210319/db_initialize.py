#! /usr/bin/env python3
# -*- coding: utf-8 -*-


import sqlite3

# conn = sqlite3.connect(':memory:') # in RAM!!
conn = sqlite3.connect('movie_database.db')
c = conn.cursor()

# initialization part that cannot be repeted if db exists!
c.execute("""CREATE TABLE IF NOT EXISTS movies (
			title TEXT,
			year INTEGER,
			UNIQUE(title, year)
)""")


# inserts clould all be done from db_add_movie.py! 
c.execute("INSERT INTO movies VALUES ('Conan the Barbarian', 1996)")
c.execute("INSERT INTO movies VALUES ('STAR WARS', 1970)")
c.execute("INSERT INTO movies VALUES ('STAR WARS III', 1973)")

conn.commit()
conn.close()

