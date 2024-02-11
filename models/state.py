#!/usr/bin/python3
"""Defines the State class, inheriting from BaseModel."""

from models.base_model import BaseModel


class State(BaseModel):
    """Represents a state object.

    Attributes:
        name (str): The name of the state.
    """

    def __init__(self, *args, **kwargs):
        """Initialize State object.

        Args:
            args: Non-keyword variable-length argument list.
            kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)

    name: str = ""
