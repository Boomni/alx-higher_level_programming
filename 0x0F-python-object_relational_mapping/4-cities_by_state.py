#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
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
    query = """SELECT cities.id, cities.name, states.name FROM states
                INNER JOIN cities ON states.id=cities.state_id
                ORDER BY cities.id ASC"""
    cursor.execute(query)
    data = cursor.fetchall()
    for row in data:
        print(row)
    cursor.close()
    db.close()
