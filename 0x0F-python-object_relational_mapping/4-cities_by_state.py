#!/usr/bin/python3
"""Lists all cities of the database hbtn_0e_4_usa, ordered by city id.

Usage:
./4-cities_by_state.py <mysql username> <mysql password> <database name>
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    con = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = con.cursor()
    sql = "SELECT `c`.`id`, `c`.`name`, `s`.`name` \
                 FROM `cities` AS `c` \
                INNER JOIN `states` AS `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`"
    cur.execute(sql)

    for city in cur.fetchall():
        print(city)
