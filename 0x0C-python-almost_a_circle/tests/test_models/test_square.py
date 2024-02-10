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
    TestSquareUpdateArgs    --------------> line
    TestSquareUpdateKwargs  --------------> line
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


class TestSquareUpdateArgs(unittest.TestCase):
    """Unittest for update args method of the Square class"""

    def test_update_zero_args(self):
        """Test case for passing zero arguments"""
        square = Square(10, 10, 10, 10)
        square.update()
        self.assertEqual(str(square), "[Square] (10) 10/10 - 10")

    def test_update_one_args(self):
        """Test case for passing one argument"""
        square = Square(10, 10, 10, 10)
        square.update(89)
        self.assertEqual("[Square] (89) 10/10 - 10", str(square))

    def test_update_two_args(self):
        """Test case for passing two arguments"""
        square = Square(10, 10, 10, 10)
        square.update(89, 2)
        self.assertEqual("[Square] (89) 10/10 - 2", str(square))

    def test_update_three_args(self):
        """Test case for passing three arguments"""
        square = Square(10, 10, 10, 10)
        square.update(89, 2, 3)
        self.assertEqual("[Square] (89) 3/10 - 2", str(square))

    def test_update_four_args(self):
        """Test case for passing four arguments"""
        square = Square(10, 10, 10, 10)
        square.update(89, 2, 3, 4)
        self.assertEqual("[Square] (89) 3/4 - 2", str(square))

    def test_update_more_than_four_args(self):
        """Test case for passing more than four arguments"""
        square = Square(10, 10, 10, 10)
        square.update(89, 2, 3, 4, 5)
        self.assertEqual("[Square] (89) 3/4 - 2", str(square))

    def test_update_set_width(self):
        """Test case for setting the width of square"""
        square = Square(10, 10, 10, 10)
        square.update(89, 2)
        self.assertEqual(2, square.width)

    def test_update_set_height(self):
        """Test case for setting the height of square"""
        square = Square(10, 10, 10, 10)
        square.update(89, 2)
        self.assertEqual(2, square.height)

    def test_update_none(self):
        """Test case for passing None as id"""
        square = Square(10, 10, 10, 10)
        square.update(None)
        res = f"[Square] ({square.id}) 10/10 - 10"
        self.assertEqual(res, str(square))

    def test_update_twice(self):
        """Test case to update swuare twice"""
        square = Square(10, 10, 10, 10)
        square.update(9, 2, 3, 4)
        square.update(4, 3, 2, 9)
        self.assertEqual("[Square] (4) 2/9 - 3", str(square))

    def test_update_invalid_size_args(self):
        """Test case for passing an invalide type to size"""
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            square.update(9, "alx")

    def test_update_size_zero(self):
        """Test case for pass a value of zero"""
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            square.update(9, 0)

    def test_update_size_negative(self):
        """Test case for pass a negative value"""
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            square.update(9, -5)

    def test_update_invalid_x(self):
        """Test case for passing an invalid x coordinate value"""
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            square.update(4, 8, "best")

    def test_update_x_negative(self):
        """Test case for passing a negative x coordinate value"""
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            square.update(12, 2, -9)

    def test_update_invalid_y(self):
        """Test case for passing an invalid y coordinate value"""
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            square.update(8, 10, 2, "school")

    def test_update_y_negative(self):
        """Test case for passing a negative y coordinate value"""
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            square.update(8, 18, 1, -9)


class TestSquareUpdateKwargs(unittest.TestCase):
    """Unittest for update kwargs method of Square class"""

    def test_update_one_kwargs(self):
        """Test case for passing one argument"""
        square = Square(10, 10, 10, 10)
        square.update(id=1)
        self.assertEqual("[Square] (1) 10/10 - 10", str(square))

    def test_update_two_kwargs(self):
        """Test case for passing two arguments"""
        square = Square(10, 10, 10, 10)
        square.update(size=1, id=2)
        self.assertEqual("[Square] (2) 10/10 - 1", str(square))

    def test_update_three_kwargs(self):
        """Test case for passing three arguments"""
        square = Square(10, 10, 10, 10)
        square.update(y=1, size=3, id=89)
        self.assertEqual("[Square] (89) 10/1 - 3", str(square))

    def test_update_four_kwargs(self):
        """Test case for passing four arguments"""
        square = Square(10, 10, 10, 10)
        square.update(id=89, x=1, y=3, size=4)
        self.assertEqual("[Square] (89) 1/3 - 4", str(square))

    def test_update_set_width_kwargs(self):
        """Test case to set width of square"""
        square = Square(10, 10, 10, 10)
        square.update(id=89, size=8)
        self.assertEqual(8, square.width)

    def test_update_set_height_kwargs(self):
        """Test case to set height of square"""
        square = Square(10, 10, 10, 10)
        square.update(id=89, size=9)
        self.assertEqual(9, square.height)

    def test_update__none_id(self):
        """Test case for passing None as id"""
        square = Square(10, 10, 10, 10)
        square.update(id=None)
        res = f"[Square] ({square.id}) 10/10 - 10"
        self.assertEqual(res, str(square))

    def test_update_none_and_more_kwargs(self):
        """Test case for passing None and other values"""
        square = Square(10, 10, 10, 10)
        square.update(id=None, size=7, x=18)
        res = f"[Square] ({square.id}) 18/10 - 7"
        self.assertEqual(res, str(square))

    def test_update_twice_kwargs(self):
        """Test case for double updating"""
        square = Square(10, 10, 10, 10)
        square.update(id=89, x=1)
        square.update(y=3, x=15, size=2)
        self.assertEqual("[Square] (89) 15/3 - 2", str(square))

    def test_update_invalid_size_kwargs(self):
        """Test case for passing an invalid value to size"""
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            square.update(size="best")

    def test_update_size_zero_kwargs(self):
        """Test case for passing a value of zero to size"""
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            square.update(size=0)

    def test_update_size_negative_kwargs(self):
        """Test case for passing a negative value to size"""
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            square.update(size=-9)

    def test_update_invalid_x_kwargs(self):
        """Test case for passing an invalid value to x coordinate"""
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            square.update(x="best")

    def test_update_x_negative_kwargs(self):
        """Test case for passing a negative value to x coordinate"""
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            square.update(x=-5)

    def test_update_invalid_y_kwargs(self):
        """Test case for passing an invalid value to y coordinate"""
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            square.update(y="best")

    def test_update_negative_y_kwargs(self):
        """Test case for passing a negative value to y coordinate"""
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            square.update(y=-5)
