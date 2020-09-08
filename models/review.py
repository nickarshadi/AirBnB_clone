#!/usr/bin/python3
"""Hold review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Inherit from BaseModel."""

    place_id = ""
    user_id = ''
    text = ''
