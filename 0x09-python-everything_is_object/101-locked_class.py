#!/usr/bin/python3
"""This actually define a locked class"""


class LockedClass:
    """Class that prevents the user from dynamically creating new
    instance attributes,except if the new instance
    attribute is called first_name.
    """

    __slots__ = ["first_name"]
