#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
import sys


if len(sys.argv) != 2:
    print("You must supply a part of the filename")
    sys.exit(1)
else:
    mname = sys.argv[1]

db = "KRZMovies.db"

conn = sqlite3.connect(db)
cr = conn.cursor()

cr.execute("SELECT * FROM movies WHERE title LIKE '%" + mname  + "%' ORDER BY year DESC, title ASC ")
rows = cr.fetchall()

columnWidths = "{0:<6}{1}"
for row in rows:
	print(columnWidths.format(str(row[1]) + ":", row[0]))

conn.close()

