#!/usr/bin/python3
"""This module defines a Square class with size property and area method."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize the square with an optional size (default is 0)."""
        self.size = size  # use setter for validation

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
