#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
import sys


if len(sys.argv) != 2:
    print("You must supply a year in form [YYYY]")
    sys.exit(1)
else:
    myear = sys.argv[1]
    if len(myear) != 4 or not myear.isdigit():
        print("You must supply a year in form [YYYY]")
        sys.exit(1)

db = "KRZMovies.db"

conn = sqlite3.connect(db)
cr = conn.cursor()

cr.execute("SELECT * FROM movies WHERE year LIKE '%" + myear  + "%' ORDER BY year DESC, title ASC ")
rows = cr.fetchall()

columnWidths = "{0:<6}{1}"
for row in rows:
	print(columnWidths.format(str(row[1]) + ":", row[0]))

conn.close()

