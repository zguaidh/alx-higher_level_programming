#!/usr/bin/python3
"""
class definition of a City and an instance Base
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import State
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """The class City Definition"""
    __tablename__ = "cities"
    id = Column(Integer, autoincrement=True, nullable=False,
                unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
