#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
import sys
import db_connect_V3 as db

if len(sys.argv) != 3:
	print("Must supply <title> and <year> as parameters!")
	sys.exit(1)

mTitle = sys.argv[1]
mYear = sys.argv[2]

conn = db.connect()
db.makeTable(conn)

db.add_movie(conn, mTitle, mYear)
print(f'Added "{mTitle} ({mYear})" to the database.')
