#!/usr/bin/python3
"""DBStorage module"""
from sqlalchemy import text
from sqlalchemy import create_engine
from os import getenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """manages storage in database"""

    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine(
            f"mysql+mysqldb://{user}:{password}@{host}/{database}",
            pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        request = []
        if cls is not None:
            cls = str(cls)
            request = self.__session.query(globals()[cls]).all()
        else:
            for cls in [User, State, City, Amenity, Place, Review]:
                if hasattr(cls, "__tablename__"):
                    request += self.__session.query(cls).all()
        return {f"{obj.__class__.__name__}.{obj.id}": obj
                for obj in request}

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
