#!/usr/bin/python3
"""Defines a Square class that supports size property and printing."""


class Square:
    """Represents a square with size and methods to compute area and print."""

    def __init__(self, size=0):
        """Initialize square with optional size (default is 0)."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
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
        """Calculate and return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#' character, or a blank line if size is 0."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)
