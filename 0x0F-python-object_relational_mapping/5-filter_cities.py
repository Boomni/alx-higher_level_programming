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
    query = """
            SELECT cities.name
            FROM cities
            INNER JOIN states ON cities.state_id = states.id
            WHERE states.name = '{}'
            ORDER BY cities.id ASC;
            """
    cursor.execute(query.format(sys.argv[4]))
    cities = cursor.fetchall()
    city_names = []
    for city in cities:
        city_names.append(city[0])
    print(", ".join(city_names))
    cursor.close()
    db.close()
