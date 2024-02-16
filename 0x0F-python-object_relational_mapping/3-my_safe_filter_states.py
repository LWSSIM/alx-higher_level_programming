#!/usr/bin/python3
"""
Script that takes in an argument and displays all values
 in the states table of hbtn_0e_0_usa where name matches the argument.

-Your script should take 4 arguments: mysql username, mysql password,
-database name and state name searched (no argument validation needed)
-You must use the module MySQLdb (import MySQLdb)
-Your script should connect to a MySQL server running on localhost at port 3306
-You must use format to create the SQL query with the user input
-Results must be sorted in ascending order by states.id
-Results must be displayed as they are in the example below
-Your code should not be executed when imported
"""


import MySQLdb
from sys import argv, exit


def list_key_match(username, password, database, key):
    """Perform connection to db + search logic"""
    try:
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database,
            charset="utf8",
        )
        cur = conn.cursor()
        query = "SELECT * FROM states WHERE name = %s ORDER BY id"
        cur.execute(query, (key,))
        rows = cur.fetchall()

        for row in rows:
            print(row)

        cur.close()
        conn.close()
    except MySQLdb.Error as e:
        print("MySQLdb error: ", e)


if __name__ == "__main__":
    if len(argv) != 5:
        print("Usage: script.py <un> <ps> <db> <key>")
        exit(1)

    un = argv[1]
    ps = argv[2]
    db = argv[3]
    key = argv[4]

    list_key_match(un, ps, db, key)
