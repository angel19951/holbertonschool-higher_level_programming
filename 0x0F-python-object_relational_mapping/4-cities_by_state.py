#!/usr/bin/python3

"""
This module list all states in a database
"""
import MySQLdb
import sys


if __name__ == "__main__":
    database = MySQLdb.connect(host='localhost',
                               port=3306,
                               user=sys.argv[1],
                               passwd=sys.argv[2],
                               db=sys.argv[3])
    cur = database.cursor()
    cur.execute('SELECT cities.id, cities.name, states.name FROM cities JOIN\
                states on cities.state_id = states.id ORDER BY cities.id ASC')

    row = cur.fetchall()
    for i in row:
        print(i)
