#!/usr/bin/python3

"""
This module list all states in a database
"""
import MySQLdb
import sys


if __name__ == "__main__" :
    f_letter = 'N'
    database = MySQLdb.connect(host='localhost',
                           port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3])
    cur = database.cursor()
    cur.execute('SELECT id, name FROM states ORDER BY states.id ASC')

    row = cur.fetchall()
    for i in row:
        if i[1][0] == f_letter:
            print(i)
