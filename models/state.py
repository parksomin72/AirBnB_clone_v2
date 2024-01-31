#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import environ as env
import models


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        __tablename__: table name
        name: input name
        cities: relation to cities table
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    
    if env.get('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", cascade="all, delete", backref="state")
    else:
        @property
        def cities(self):
            """get all cities with the current state id
            from file storage
            """
            l = [
                v for k, v in models.storage.all(models.City).items()
                if v.state_id == self.id
            ]
            return l
