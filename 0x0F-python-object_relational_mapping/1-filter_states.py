#!/usr/bin/python3
"""
lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
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
    cur.execute("SELECT id, name FROM states WHERE BINARY
                name LIKE 'N%' ORDER BY id")
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    conn.close()
