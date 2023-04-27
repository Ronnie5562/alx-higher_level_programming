#!/usr/bin/python3
"""___ Description ___
A python code that describes a typical row in our states table
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City


class State(Base):
    """ ___ Description ___
    city class that describes a typical row in our cities table in the MySQL database.

    Attributes:
        __tablename__ (str): MySQL states table.
        id (sqlalchemy.Integer): state id.
        name (sqlalchemy.String): state name.
        cities (sqlalchemy.orm.relationship): The State-City relationship.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
