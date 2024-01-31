#!/usr/bin/python3
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os
from models import storage

class State(BaseModel, Base):
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """
            Getter method for cities.
            """
            cities_list = []
            for city in list(storage.all(City).values()):
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
