#!/usr/bin/python3
"""This module defines a Square class with size validation and area computation."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """
        Initialize the square with an optional size (default is 0).
        Validates that size is a non-negative integer.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2
