#!/usr/bin/python3
"""
Write a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
"""
import sys
import MySQLdb

if __name__ == "__main__":
  db = MySQLdb.connect(user=sys.argv[1], port=3306, host="localhost", passwd=sys.argv[2], db=sys.argv[3])
  c = db.cursor()
  state = str(sys.argv[4])
  c.execute("SELECT * FROM states WHERE name LIKE ? ORDER BY id ASC", (state,))
  data = c.fetchall()
  [print(city) for city in data if city[1] == state]
  c.close()
  db.close()
