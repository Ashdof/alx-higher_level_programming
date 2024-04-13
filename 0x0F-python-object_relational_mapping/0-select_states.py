#!/usr/bin/python3
""" List all states from the database hbtn_0e_0_usa:
Usuage:
./0-select_states.py <mysql username> <mysql password> <database name>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    con = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = con.cursor()
    sql = "SELECT * FROM `states`"
    cur.execute(sql)

    for state in cur.fetchall():
        print(state)