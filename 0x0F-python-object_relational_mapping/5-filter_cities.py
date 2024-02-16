#!/usr/bin/python3
"""
Write a script that takes in the name of a state as an argument and
 lists all cities of that state, using the database hbtn_0e_4_usa

 -Your script should take 4 arguments:
  mysql username, mysql password, database name and state name
  (SQL injection free!)
 -You must use the module MySQLdb (import MySQLdb)
 -Your script should connect to a MySQL server
  running on localhost at port 3306
 -Results must be sorted in ascending order by cities.id
 -You can use only execute() once
 -The results must be displayed as they are in the example below
 -Your code should not be executed when imported
"""


import MySQLdb
import sys


def filter_cities(username, password, database, key):
    try:
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database,
            charset="utf8",
        )
        cursor = conn.cursor()

        query = "SELECT cities.name FROM cities \
        WHERE state_id = \
        (SELECT id FROM states WHERE name = %s) \
        ORDER BY id"

        cursor.execute(query, (key,))

        rows = cursor.fetchall()

        res = ()

        for row in rows:
            res += row

        print(*res, sep=", ")
        cursor.close()
        conn.close()
    except MySQLdb.Error as e:
        print("MySQLdb.Error: ", e)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: script.py <un> <ps> <db> <key>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    key = sys.argv[4]

    filter_cities(username, password, database, key)
