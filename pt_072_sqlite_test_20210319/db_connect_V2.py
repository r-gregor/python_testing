#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
from contextlib import closing

db_file="movies.db"

CREATE_TABLE = "CREATE TABLE IF NOT EXISTS movies(title TEXT, year  INTEGER);"
INSERT_MOVIE="INSERT INTO movies (title, year) VALUES (?, ?);"
GET_ALL="SELECT * FROM movies;"

def connect():
    return sqlite3.connect(db_file)

def makeTable(connection):
    with connection as conn:
        with closing(conn.cursor()) as c:
            c.execute(CREATE_TABLE)
            conn.commit()

def add_movie(connection, mtitle, myear):
    with connection as conn:
        with closing(conn.cursor()) as c:
            c.execute(INSERT_MOVIE, (mtitle, myear))
            conn.commit()

def displayAll(connection):
    with connection as conn:
        c = conn.cursor()
        rows = c.execute(GET_ALL)
        return rows
        conn.commit()
        c.close()

