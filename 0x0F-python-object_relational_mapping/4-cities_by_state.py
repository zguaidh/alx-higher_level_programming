#!/usr/bin/python3
"""Script that lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=username, passwd=password, db=db_name)
    cur = conn.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name FROM
                cities JOIN states ON cities.state_id ORDER BY cities.id")
    cities = cur.fetchall()

    for city in cities:
        print(city)

    cur.close()
    conn.close()
