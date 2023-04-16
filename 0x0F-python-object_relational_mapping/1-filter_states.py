#!/usr/bin/python3
"""
Lists all states with a name starting with N from the database hbtn_0e_0_usa
"""


import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    cursor = db.cursor()
    query = "SELECT * FROM states ORDER BY id ASC;"
    cursor.execute(query)
    data = cursor.fetchall()
    for row in data:
        if (row[1][0] == 'N'):
            print(row)
    cursor.close()
    db.close()
