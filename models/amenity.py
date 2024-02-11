#!/usr/bin/python3
"""Defines the Amenity class, inheriting from BaseModel."""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an Amenity object.

    Attributes:
        name (str): The name of the amenity.
    """

    def __init__(self, *args, **kwargs):
        """Initialize Amenity object.

        Args:
            args: Non-keyword variable-length argument list.
            kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)

    name: str = ""
