#!/usr/bin/python3

"""___ Description ___
A python code that describes a typical row in our cities table
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """ ___ Description ___
    A city class that describes a typical row in our cities table in the MySQL database.

    Attributes:
        id (sqlalchemy.Column): city id.
        name (sqlalchemy.Column): city name.
        state_id (sqlalchemy.Column): city state id.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
