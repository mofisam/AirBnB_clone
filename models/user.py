#!/usr/bin/python3
"""Defines the User class, inheriting from BaseModel."""

from models.base_model import BaseModel


class User(BaseModel):
    """Represents a User object.

    Attributes:
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        email (str): The email address of the user.
        password (str): The password associated with the user.
    """

    def __init__(self, *args, **kwargs):
        """Initialize User object.

        Args:
            args: Non-keyword variable-length argument list.
            kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)

    first_name: str = ""
    last_name: str = ""
    email: str = ""
    password: str = ""
