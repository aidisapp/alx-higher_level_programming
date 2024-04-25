#!/usr/bin/python3
"""
Script that lists all states with a name starting with
N (upper N) from the database.
"""

from sys import argv
import MySQLdb

if __name__ == '__main__':
    if len(argv) < 5:
        print(
            "Usage: {} <user> <password> <database> <state_name>".format(
                argv[0]))
        exit(1)

    user = argv[1]
    password = argv[2]
    database_name = argv[3]
    state_name = argv[4]

    db_connection = MySQLdb.connect(
        user=user, passwd=password, db=database_name)
    cursor = db_connection.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}%'".format(
                                        state_name))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db_connection.close()
