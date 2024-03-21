#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument and  is safe from MySQL injections!
"""
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    st_name = sys.argv[4]
    conn = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)
    cur = conn.cursor()

    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id", (st_name,))
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    conn.close()
