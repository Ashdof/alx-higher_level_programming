#!/usr/bin/python3
"""A module with test cases for a rectangle object"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


"""
    Unit Test Cases for Rectangle Objects
    TestRectangleInstantiation --------------> line
"""


class TestRectangleInstantiation(unittest.TestCase):
    """Unittest for instantiation of the Rectangle class"""

    def test_rectangle_is_base(self):
        """Test case if rectangle is an instance of base class"""
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        """Test case for no arguments"""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        """Test case for one argument"""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        """Test case for two arguments"""
        rec_1 = Rectangle(10, 2)
        rec_2 = Rectangle(2, 10)
        self.assertEqual(rec_1.id, rec_2.id - 1)

    def test_three_args(self):
        """Test case for three arguments"""
        rec_1 = Rectangle(2, 2, 4)
        rec_2 = Rectangle(4, 4, 2)
        self.assertEqual(rec_1.id, rec_2.id - 1)

    def test_four_args(self):
        """Test case for four arguments"""
        rec_1 = Rectangle(1, 2, 3, 4)
        rec_2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(rec_1.id, rec_2.id - 1)

    def test_five_args(self):
        """Test case for five arguments"""
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

    def test_more_than_five_args(self):
        """Test case for more than five arguments"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_width_private(self):
        """Test case for accessing private method, width"""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_height_private(self):
        """Test case for accessing private method, height"""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def test_x_private(self):
        """Test case for accessing private method, x"""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def test_y_private(self):
        """Test case for accessing private method, y"""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

    def test_width_getter(self):
        """Test case for getting width of rectangle"""
        rec = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, rec.width)

    def test_width_setter(self):
        """Test case for setting width of rectangle"""
        rec = Rectangle(5, 7, 7, 5, 1)
        rec.width = 10
        self.assertEqual(10, rec.width)

    def test_height_getter(self):
        """Test case for getting the height of rectangle"""
        rec = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, rec.height)

    def test_height_setter(self):
        """Test case for setting the height of rectangle"""
        rec = Rectangle(5, 7, 7, 5, 1)
        rec.height = 10
        self.assertEqual(10, rec.height)

    def test_x_getter(self):
        """Test case for getting the x coordinate of rectangle"""
        rec = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, rec.x)

    def test_x_setter(self):
        """Test case for setting the x coordinate of rectangle"""
        rec = Rectangle(5, 7, 7, 5, 1)
        rec.x = 10
        self.assertEqual(10, rec.x)

    def test_y_getter(self):
        """Test case for getting the y coordinate of rectangle"""
        rec = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, rec.y)

    def test_y_setter(self):
        """Test case for setting the y coordinate of rectangle"""
        rec = Rectangle(5, 7, 7, 5, 1)
        rec.y = 10
        self.assertEqual(10, rec.y)
