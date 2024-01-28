#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
from os import getenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """This class manages storage of hbnb models in a database"""
    __engine = None
    __session = None

    def __init__(self):
        """This instantiates the database storage"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            metadata = MetaData()
            metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """This returns a dictionary of every object in the storage"""
        session = self.__session
        objects = {}
        if cls is not None:
            for obj in session.query(cls).all():
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                objects[key] = obj
        else:
            for model in [User, State, City, Place, Amenity, Review]:
                for obj in session.query(model).all():
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    objects[key] = obj
        return objects

    def new(self, obj):
        """This adds an object to the database"""
        self.__session.add(obj)

    def save(self):
        """This saves changes to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """This deletes an object from the database"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """This reloads the database into __objects"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))()

    def close(self):
        """This method calls remove() on the private session attribute"""
        self.__session.remove()
