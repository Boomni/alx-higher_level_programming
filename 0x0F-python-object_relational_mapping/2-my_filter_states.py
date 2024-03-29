#!/usr/bin/python3
"""
Takes in an argument and displays all values
in the states table of hbtn_0e_0_usa
where name matches the argument
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
    query = "SELECT * FROM states WHERE name LIKE '{}' ORDER BY id ASC"
    cursor.execute(query.format(sys.argv[4]))
    data = cursor.fetchall()
    for row in data:
        if (row[1] == sys.argv[4]):
            print(row)
    cursor.close()
    db.close()
