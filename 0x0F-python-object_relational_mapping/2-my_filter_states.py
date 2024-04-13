#!/usr/bin/python3
""" List all states from the database hbtn_0e_0_usa with the
searched name

Usuage:
./2-my_filter_states.py <mysql username> <mysql password> \
                     <database name> <state name searched>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    con = MySQLdb.connect(user=sys.argv[1], port=3306, host="localhost",
                          passwd=sys.argv[2], db=sys.argv[3], )
    cur = con.cursor()
    sql = "SELECT * FROM `states` WHERE name LIKE '{:s}' ORDER BY \
    `id` ASC".format(sys.argv[4])
    cur.execute(sql)

    for state in cur.fetchall():
        if state[1] == sys.argv[4]:
            print(state)
    cur.close()
    con.close()
