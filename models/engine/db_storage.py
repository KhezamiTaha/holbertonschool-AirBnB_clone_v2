#!/usr/bin/python3
"""This module defines a class to manage DBStorage storage for hbnb clone"""
from sqlalchemy import create_engine
import os
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session

class DBStorage:
    """This class manages storage of hbnb models in MySQL"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                            os.getenv("HBNB_MYSQL_USER"),
                            os.getenv("HBNB_MYSQL_PWD"),
                            os.getenv("HBNB_MYSQL_HOST"),
                            os.getenv("HBNB_MYSQL_DB")), pool_pre_ping=True)
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects depending on the class."""
        if cls:
            objects = self.__session.query(cls).all()
        else:
            from models.user import User
            from models.place import Place
            from models.state import State
            from models.city import City
            from models.amenity import Amenity
            from models.review import Review
            objects = []
            classes = [State, User, Place, City, Amenity, Review]

            for clss in classes:
                objects += self.__session.query(clss).all()
        dictonary = {}
        for obj in objects:
            dictonary[obj.__class__.__name__ + '.' + obj.id] = obj
        return dictonary

    def new(self, obj):
        """add the object to the current database session (self.__session)"""
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session (self.__session)"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """create all tables in the database"""
        self.__session.remove()
