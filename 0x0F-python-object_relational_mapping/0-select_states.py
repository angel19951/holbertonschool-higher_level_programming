#!/usr/bin/python3

"""
This module list all states in a database
"""
import MySQLdb
import sys


if __name__ == "__main__" :
    database = MySQLdb.connect(host='localhost',
                           port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3])
    cur = database.cursor()
    cur.execute('SELECT id, name FROM states ORDER BY states.id ASC')

    for i in cur.fetchall():
        print(i)
