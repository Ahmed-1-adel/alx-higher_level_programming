#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
from sys import argv


if __name__ == '__main__':

    # make a connection to the database

    mydb = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    # It gives us the ability to have multiple seperate working environments
    # through the same connection to the database.

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM states")

    rows = mycursor.fetchall()
    for i in rows:
        print(i)
    # Clean up process
    mycursor.close()
    mydb.close()
