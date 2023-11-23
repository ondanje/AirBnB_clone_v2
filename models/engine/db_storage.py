#!/usr/bin/python3
""" Module for DBStorage """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """ DataBase Storage class """

    __engine = None
    __session = None

    def __init__(self):
        """ A class Constructor """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Query all objects depending on the class name """
        obj_dict = {}
        if cls:
            objects = self.__session.query(cls).all()
        else:
            classes = ["User", "State", "City", "Amenity", "Place", "Review"]
            objects = []
            for c in classes:
                objects += self.__session.query(eval(c)).all()

        for obj in objects:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            obj_dict[key] = obj

        return obj_dict

    def new(self, obj):
        """ Adds object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commit all current changes of the database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete from current database session """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Create all tables in database and creates the session """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
