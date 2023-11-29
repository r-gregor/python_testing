#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import db_connect_V3 as db

conn = db.connect()
db.makeTable(conn)

# db.add_movie(conn, "Conan The Barbarian", 1980)
# db.add_movie(conn, "Tarzan", 1954)
# db.add_movie(conn, "STAR WARS", 1970)
# db.add_movie(conn, "EQUILIBRIUM", 2001)
db.add_movie(conn, "Tarzan", 1977)

rows = db.displayAll(conn).fetchall()
# rows = conn.execute("SELECT * FROM movies;").fetchall()
print(rows)
