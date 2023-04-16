#!/usr/bin/python3
"""
Takes in the name of a state as an argument and
lists all cities of that state
using the database hbtn_0e_4_usa
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
    query = "SELECT * FROM cities " \
            "INNER JOIN cities ON states.id=cities.state_id;"
    cursor.execute(query)
    data = cursor.fetchall()
    for row in data:
        print(row)
    cursor.close()
    db.close()
