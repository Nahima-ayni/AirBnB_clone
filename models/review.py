#!/usr/bin/python3

""" import modules that are needed """
from models.base_model import BaseModel


class Review(BaseModel):
    """ review place, user and text """
    place_id = ""
    user_id = ""
    text = ""
