#!/usr/bin/python3
"""Defines the Review class, inheriting from BaseModel."""

from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review object.

    Attributes:
        place_id (str): The ID of the place being reviewed.
        user_id (str): The ID of the user who wrote the review.
        text (str): The content of the review.
    """

    def __init__(self, *args, **kwargs):
        """Initialize Review object.

        Args:
            args: Non-keyword variable-length argument list.
            kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)

    place_id: str = ""
    user_id: str = ""
    text: str = ""
