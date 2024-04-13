#!/usr/bin/python3
""" List all states from the database hbtn_0e_0_usa with the name
starting with the letter N

Usuage:
./1-filter_states.py <mysql username> <mysql password> <database name>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    con = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = con.cursor()
    sql = "SELECT * FROM `states` ORDER BY `id`"
    cur.execute(sql)

    for state in cur.fetchall():
        if state[1][0] == "N":
            print(state)
