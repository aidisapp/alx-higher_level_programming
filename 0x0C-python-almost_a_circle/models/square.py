#!/usr/bin/python3

"""Square Class Definition

This module defines a Square class representing squares,
a special case of rectangles with equal width and height.

Attributes:
    size (int): The size of the square.
    x (int): The x coordinate of the square.
    y (int): The y coordinate of the square.
    id (int): The identity of the square.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class

    This class represents squares, a special case of
    rectangles with equal width and height.

    Attributes:
        size (int): The size of the square.
        x (int): The x coordinate of the square.
        y (int): The y coordinate of the square.
        id (int): The identity of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square object.

        Args:
            size (int): The size of the square.
            x (int): The x coordinate of the square. Defaults to 0.
            y (int): The y coordinate of the square. Defaults to 0.
            id (int): The identity of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get or set the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the attributes of the square.

        Args:
            *args (ints): New attribute values in the order
            (id, size, x, y).
            **kwargs (dict): New attribute key-value pairs.
        """
        if args:
            attributes = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, attributes[i], value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Convert the square object to a dictionary."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
