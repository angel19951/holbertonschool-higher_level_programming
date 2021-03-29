#!/usr/bin/python3

"""
This module list a state given passed by user in a database
"""
import MySQLdb
import sys


if __name__ == "__main__":
    lookup = sys.argv[4]
    database = MySQLdb.connect(host='localhost',
                               port=3306,
                               user=sys.argv[1],
                               passwd=sys.argv[2],
                               db=sys.argv[3])
    cur = database.cursor()
    cur.execute('SELECT id, name FROM states WHERE states.name = \'{}\'\
                ORDER BY states.id ASC'.format(lookup))

    row = cur.fetchall()
    for i in row:
        if i[1] == lookup:
            print(i)
