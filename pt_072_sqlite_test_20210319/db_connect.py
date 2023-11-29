#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3


db_file="movies.db"

CREATE_TABLE = "CREATE TABLE IF NOT EXISTS movies(title TEXT,year  INTEGER);"
INSERT_MOVIE="INSERT INTO movies (title, year) VALUES (?, ?);"
GET_ALL="SELECT * FROM movies;"

def connect():
    return sqlite3.connect(db_file)

def makeTable(connection):
    with connection:
        connection.execute(CREATE_TABLE)

def add_movie(connection, title, year):
    with connection:
        connection.execute(INSERT_MOVIE, (title, year))


def displayAll(connection):
    with connection:
        return connection.execute(GET_ALL)


