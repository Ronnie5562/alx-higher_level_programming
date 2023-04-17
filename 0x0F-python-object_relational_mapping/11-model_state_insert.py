#!/usr/bin/python3
""" ___ Description ___
A script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
Usage: ./11-model_state_insert.py <mysql username> <mysql password> <database name>
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import State as ST

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    louisiana_obj = ST(name="Louisiana")
    session.add(louisiana_obj)
    session.commit()
    print(louisiana_obj.id)
