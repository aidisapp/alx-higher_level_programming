#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in
the states table where name matches the argument.
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    host = "localhost"
    user = argv[1]
    password = argv[2]
    database = argv[3]
    search_name = argv[4]

    db_connection = MySQLdb.connect(
                host=host, user=user, passwd=password, db=database, port=3306)
    cursor = db_connection.cursor()
    cursor.execute(
            "SELECT * FROM states WHERE name LIKE BINARY '{}%'".format(
                                                                search_name))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db_connection.close()
