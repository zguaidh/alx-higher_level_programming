#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    st_name = sys.argv[4]

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=username, passwd=password, db=db_name)
    cur = conn.cursor()

    cur.execute("""SELECT cities.name, states.name
                FROM cities JOIN states
                ON cities.state_id = states.id
                WHERE BINARY states.name=%s
                ORDER BY cities.id""", (st_name,))
    rows = cur.fetchall()

    cities = [row[0] for row in rows]
    print(", ".join(cities))

    cur.close()
    conn.close()
