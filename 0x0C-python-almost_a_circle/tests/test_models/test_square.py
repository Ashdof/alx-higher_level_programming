#!/usr/bin/python3
"""Square Model Test Cases"""

import unittest
from models.rectangle import Rectangle
from models.square import Square

"""
    Define unittests for models/square.py.

    Unittest classes:
    TestSquareInstantiation --------------> line
"""


class TestSquareInstantiation(unittest.TestCase):
    """Unittest for instantiation of the Square class"""

    def test_rectangle_is_base(self):
        """Test case if square is an instance of rectangle class"""
        self.assertIsInstance(Square(5), Rectangle)

    def test_no_args(self):
        """Test case for no arguments"""
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        """Test case for one argument"""
        squ_1 = Square(9)
        squ_2 = Square(5)
        self.assertEqual(squ_1.id, squ_2.id - 1)

    def test_two_args(self):
        """Test case for two arguments"""
        squ_1 = Square(8, 2)
        squ_2 = Square(2, 9)
        self.assertEqual(squ_1.id, squ_2.id - 1)

    def test_three_args(self):
        """Test case for three arguments"""
        squ_1 = Square(10, 2, 2)
        squ_2 = Square(2, 2, 10)
        self.assertEqual(squ_1.id, squ_2.id - 1)

    def test_four_args(self):
        """Test case for three arguments"""
        self.assertEqual(Square(10, 2, 2, 7).id, 7)

    def test_more_than_four_args(self):
        """Test case for more than four arguments"""
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_size_private(self):
        """Test case for accessing private size"""
        with self.assertRaises(AttributeError):
            print(Square(10, 2, 3, 4).__size)

    def test_size_getter(self):
        """Test case for setting the size"""
        self.assertEqual(Square(5, 2, 3, 9).size, 5)

    def test_size_setter(self):
        """Test case for setting the size"""
        square = Square(4, 1, 9, 2)
        square.size = 8
        self.assertEqual(square.size, 8)

    def test_width_getter(self):
        """Test case for accessing the width"""
        square = Square(4, 1, 9, 2)
        square.size = 8
        self.assertEqual(square.width, 8)

    def test_height_getter(self):
        """Test case for accessing the height"""
        square = Square(4, 1, 9, 2)
        square.size = 8
        self.assertEqual(square.height, 8)

    def test_x_getter(self):
        """Test case for accessing the x coordinate"""
        self.assertEqual(Square(10).x, 0)

    def test_y_getter(self):
        """Test case for accessing the y coordindate"""
        self.assertEqual(Square(10).y, 0)
