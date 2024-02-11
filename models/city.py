#!/usr/bin/python3
"""Defines the City class, inheriting from BaseModel."""

from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city object.

    Attributes:
        state_id (str): The state ID associated with the city.
        name (str): The name of the city.
    """

    def __init__(self, *args, **kwargs):
        """Initialize City object.

        Args:
            args: Non-keyword variable-length argument list.
            kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)

    state_id: str = ""
    name: str = ""
