#!/usr/bin/python3
"""
A python code that describes a typical row in our cities table
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """___Description___
    A python code that describes a typical row in our cities table

    Attributes:
        id (sqlalchemy.Integer): city's id.
        name (sqlalchemy.String): city name.
        state_id (sqlalchemy.String): city state id.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
