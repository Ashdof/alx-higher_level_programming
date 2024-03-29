#!/usr/bin/python3
"""A module with a class"""


class Rectangle:
    """A class that defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize the rectangle object

        Args:
            width (int): the width value
            height (int): the height value
        """
        self.__width = width
        self.__height = height

        type(self).number_of_instances += 1

    @property
    def width(self):
        """Return the width of the rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        """Update the width of the rectangle

        Args:
            value (int): the value to update the width
        """

        err_type = "width must be an integer"
        err_value = "width must be >= 0"

        if not isinstance(value, int):
            raise TypeError(err_type)
        elif value < 0:
            raise ValueError(err_value)
        else:
            self.__width = value

    @property
    def height(self):
        """Return the height of this rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        """Update the height of the rectangle

        Args:
            value (int): the value to update the rectangle
        """

        err_type = "height must be an integer"
        err_value = "height must be >= 0"

        if not isinstance(value, int):
            raise TypeError(err_type)
        elif value < 0:
            raise ValueError(err_value)
        else:
            self.__height = value

    def area(self):
        """Return the area of the rectangle"""

        return self.__height * self.__width

    def perimeter(self):
        """Return the perimeter of the rectangle"""

        ans = 0

        if self.__height == 0 or self.__width == 0:
            ans = 0
        else:
            ans = (2 * self.__height) + (2 * self.__width)

        return ans

    def __str__(self):
        """Print rectangle object

        Description:
            This method prints a rectangle representation
            of the object using the # character
        """

        ans = ""

        if self.__width == 0 or self.__height == 0:
            ans = ""
        else:
            ans = ("\n".join(["".join([str(self.print_symbol) for i in
                   range(self.__width)]) for j in range(self.__height)]))

        return ans

    def __repr__(self):
        """Return a string representation of the rectangle"""

        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Delete an instance of the retangle"""

        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """Compare rectangles

        Args:
            rect_1 (Rectangle): an object of type Rectangle
            rect_2 (Rectnagle): an object of type Rectangle

        Returns:
            The rectangle with the largest area or rect_1 if both
            have the same area size
        """

        err_type_1 = "rect_1 must be an instance of Rectangle"
        err_type_2 = "rect_2 must be an instance of Rectangle"

        if type(rect_1) is not Rectangle:
            raise TypeError(err_type_1)

        if type(rect_2) is not Rectangle:
            raise TypeError(err_type_2)

        if rect_1.area() >= rect_2.area():
            return rect_1

        return rect_2
