#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
The script takes 3 arguments: mysql username, mysql password and database name
"""
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=username, passwd=password, db=db_name)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    states = cur.fetchall()

    for state in states:
        print(state)
