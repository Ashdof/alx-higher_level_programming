#!/usr/bin/python3
"""Lists all cities of the database hbtn_0e_4_usa, based on the
state name.

Usage:
./5-filter_cities.py <mysql username> <mysql password> <database name>
                     <state name>
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    con = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = con.cursor()
    sql = "SELECT * FROM `cities` AS `c` \
                INNER JOIN `states` AS `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`"
    cur.execute(sql)

    print(", ".join(c[2] for c in cur.fetchall() if c[4] == argv[4]))
