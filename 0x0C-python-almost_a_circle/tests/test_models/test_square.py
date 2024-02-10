#!/usr/bin/python3
"""Square Model Test Cases"""

import unittest
from models.rectangle import Rectangle
from models.square import Square

"""
    Define unittests for models/square.py.

    Unittest classes:
    TestSquareInstantiation --------------> line
    TestSquareSize          --------------> line
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


class TestSquareSize(unittest.TestCase):
    """Unittest for size initialization of the Square class"""

    def test_none_size(self):
        """Test case for None object"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_str_size(self):
        """Test case for passing a string object"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("best")

    def test_float_size(self):
        """Test case for passing a float object"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(9.2)

    def test_complex_size(self):
        """Test case for passing a complex object"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(9))

    def test_dict_size(self):
        """Test case for passing a dictionary object"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"height": 4, "width": 9}, 2)

    def test_bool_size(self):
        """Test case for passing a boolean object"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(False, 4, 9)

    def test_list_size(self):
        """Test case for passing a list object"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 2, 3])

    def test_set_size(self):
        """Test case for passing a set object"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 2, 3}, 2)

    def test_tuple_size(self):
        """Test case for passing a tuple object"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 2, 3), 2, 3)

    def test_frozenset_size(self):
        """Test case for passing a frozenset object"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(frozenset({1, 2, 3, 1}))

    def test_range_size(self):
        """Test case for passing a range object"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(range(3, 9))

    def test_bytes_size(self):
        """Test case for passing a bytes object"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(b'School')

    def test_bytearray_size(self):
        """Test case for passing a bytearray object"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(bytearray(b'Best'))

    def test_memoryview_size(self):
        """Test case for passing a memoryview object"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(memoryview(b'alx'))

    def test_inf_size(self):
        """Test case for passing an infinit object"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'))

    def test_nan_size(self):
        """Test case for a NaN object"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'))

    def test_negative_size(self):
        "Test case for pass a negative integer object"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1, 2)

    def test_zero_size(self):
        """Test case for passing a value of zero"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 2)
