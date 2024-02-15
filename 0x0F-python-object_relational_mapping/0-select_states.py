#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa:

    Your script should take 3 arguments: mysql username,
     mysql password and database name (no argument validation needed)
    You must use the module MySQLdb (import MySQLdb)
    Your script should connect to a MySQL server
     running on localhost at port 3306
    Results must be sorted in ascending order by states.id
    Results must be displayed as they are in the example below
    Your code should not be executed when imported
"""


import MySQLdb
import sys


def list_all_states(username, password, database):
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

        cursor.execute("SELECT * FROM states ORDER BY states.id")

        rows = cursor.fetchall()

        for row in rows:
            print(row)

        cursor.close()
        conn.close()
    except MySQLdb.Error as e:
        print("MySQLdb.Error: ", e)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: script.py <un> <ps> <db>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_all_states(username, password, database)
