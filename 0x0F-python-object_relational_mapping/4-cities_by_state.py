#!/usr/bin/python3
"""
Write a script that lists all cities from the database hbtn_0e_4_usa
Usage: ./4-cities_by_state.py <mysql username> <mysql password> \
                                                 <database name>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT `cities`.`id`, `cities`.`name`, `states`.`name` \
                 FROM `cities` \
                INNER JOIN `states` \
                   ON `cities`.`state_id` = `states`.`id` \
                ORDER BY `cities`.`id`")
    cities = c.fetchall()
    [print(city) for city in cities]
