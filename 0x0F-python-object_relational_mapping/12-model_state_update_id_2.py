#!/usr/bin/python3
"""
A script that changes the name of a State object from the database hbtn_0e_6_usa
Usage: ./12-model_state_update_id_2.py <mysql username> <mysql password> <database name>
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

    state = session.query(ST).filter_by(id=2).first()
    state.name = "New Mexico"
    session.commit()
