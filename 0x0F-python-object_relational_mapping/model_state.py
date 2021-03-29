#!/usr/bin/python3
"""
Defines a State model class
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()

class State(Base):
    """
    Defines a State class to linked to a database table
    """
    __tablename__ = 'states'

    id = Column(Integer, nullable=False, autoincrement=True,
                unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
