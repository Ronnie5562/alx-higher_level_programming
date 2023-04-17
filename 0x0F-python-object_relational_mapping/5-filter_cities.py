#!/usr/bin/python3
"""
Write a script that takes in the name of a state as an argument and 
lists all cities of that state, using the database hbtn_0e_4_usa
Usage: ./5-filter_cities.py <mysql username> <mysql password> \
                            <database name> <state name searched>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `cities` \
                INNER JOIN `states` \
                   ON `cities`.`state_id` = `states`.`id` \
                ORDER BY `cities`.`id`")
    cities = c.fetchall()
    print(", ".join([city[2] for city in cities if city[4] == sys.argv[4]]))
