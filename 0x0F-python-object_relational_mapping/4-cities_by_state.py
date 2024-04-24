#!/usr/bin/python3
"""Script that lists all cities from the database hbtn_0e_4_usa"""

from sys import argv
import MySQLdb


if __name__ == "__main__":
    database_connection = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cursor = database_connection.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id""")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()

    database_connection.close()
