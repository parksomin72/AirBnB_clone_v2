#!/usr/bin/python3
"""This module defines a class State that inherits from BaseModel"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """This class defines a State and its attributes"""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    
    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state", cascade="all, delete-orphan",
                              passive_deletes=True)
    else:
        @property
        def cities(self):
            """Return the list of City instances with state_id equal to the current State.id"""
            cities_list = []
            all_cities = models.storage.all(models.City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
