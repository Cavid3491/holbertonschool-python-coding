#!/usr/bin/python3
"""This module defines a class Square."""

class Square:
    """Represents a square with a private size attribute."""
    
    def __init__(self, size):
        """Initializes a new Square.

        Args:
            size (int): The size of the square (no validation).
        """
        self.__size = size
