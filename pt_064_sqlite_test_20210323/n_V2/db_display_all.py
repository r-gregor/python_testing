#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
import sys
import db_connect_V3 as db

conn = db.connect()
# db.makeTable(conn)

rows = db.displayAll(conn).fetchall()
print(rows)
