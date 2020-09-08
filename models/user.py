#!/usr/bin/python3
"""This Module creates the User class."""
from models.base_model import BaseModel
import json


class User(BaseModel):
    """Inherit from BaseModel via class User."""

    email = ''
    password = ''
    first_name = ''
    last_name = ''
