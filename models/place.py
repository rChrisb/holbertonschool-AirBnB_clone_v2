#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from os import getenv
from sqlalchemy.orm import relationship
import models
from models.review import Review


class Place(BaseModel):
    """ A place to stay """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="place")
    else:
        @property
        def reviews(self):
            reviews_list = []
            for review in models.storage.all(Review).values():
                if self.id == review.place_id:
                    reviews_list.append(review)
            return reviews_list
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
