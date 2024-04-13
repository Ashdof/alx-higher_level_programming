#!/usr/bin/python3
""" List all states from the database hbtn_0e_0_usa with a searched
name, safe from SQL injections

Usuage:
./3-my_safe_filter_states.py <mysql username> <mysql password> \
                     <database name> <state name searched>
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    con = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                          passwd=argv[2], db=argv[3], charset="utf8")
    cur = con.cursor()
    sql = "SELECT * FROM `states` WHERE name LIKE %s ORDER BY `id` ASC"
    cur.execute(sql, (argv[4],))

    for state in cur.fetchall():
        print(state)
    cur.close()
    con.close()
