#!/usr/bin/python3
"""Define a square class that inherits from Rectangle class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Model a square"""

    def __init__(self, size):
        """Initialize a square object"""

        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
