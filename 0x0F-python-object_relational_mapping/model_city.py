#!/usr/bin/python3
"""
Define the class City
"""
from model_state import Base as StateBase
from sqlalchemy import Column, Integer, String, ForeignKey


class City(StateBase):
    """
    Class definition for each city
    Attributes: city_id, city_name, state_id (foreign key)
    """
    __tablename__ = 'cities'
    city_id = Column(Integer, unique=True, nullable=False, primary_key=True)
    city_name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
