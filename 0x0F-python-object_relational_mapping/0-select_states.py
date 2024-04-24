#!/usr/bin/python3
"""Script that lists all states from the database."""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    db_host = "localhost"
    db_user = argv[1]
    db_pass = argv[2]
    db_name = argv[3]
    db_port = 3306

    database_connection = MySQLdb.connect(
        host=db_host, user=db_user, passwd=db_pass, db=db_name, port=db_port)
    cursor = database_connection.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    database_connection.close()
