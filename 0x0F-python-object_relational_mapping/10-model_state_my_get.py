#!/usr/bin/python3
"""
A script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa
Usage: ./10-model_state_my_get.py <mysql username> <mysql password> <database name> <state name searched>
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    found_state = False
    for state in session.query(State):
        if state.name == sys.argv[4]:
            print("{}".format(state.id))
            found_state = True
            break
    if found_state is False:
        print("Not found")
