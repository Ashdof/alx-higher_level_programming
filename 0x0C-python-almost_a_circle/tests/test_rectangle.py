#!/usr/bin/python3
"""A module with test cases for a rectangle object"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


"""
    Unit Test Cases for Rectangle Objects
    TestRectangleInstantiation  -------------> line
    TestRectangleWidth          -------------> line
    TestRectangleHeight         -------------> line
    TestRectangleX              -------------> line
    TestRectangleY              -------------> line
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


class TestRectangleWidth(unittest.TestCase):
    """Unittest for initialization of Rectangle width attribute"""

    def test_negative_width(self):
        """Test case for assigning negative value to width"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-8, 9)

    def test_zero_width(self):
        """Test case for assigning a value of zero to width"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_none_width(self):
        """Test case for assigning None to width of rectangle"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 8)

    def test_str_width(self):
        """Test case for assigning string of charaters to width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("best", 120)

    def test_str_int_width(self):
        """Test case for assigning string of charaters to width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("23", 8)

    def test_float_width(self):
        """Test case for assigning float value to width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(9.009, 3)

    def test_complex_width(self):
        """Test case for assigning complex value to width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(2), 5)

    def test_dict_width(self):
        """Test case for assigning a dictionary object to width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"Jay": 78, "Kay": 87}, 9)

    def test_bool_width(self):
        """Test case for assigning a Boolean value to width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(False, 9)

    def test_list_width(self):
        """Test case for assigning a list object to width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([23, 32, 14, 41], 9)

    def test_set_width(self):
        """Test case for assigning a set object to width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({6, 7, 8}, 9)

    def test_tuple_width(self):
        """Test case for assigning a tuple object to width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((6, 7, 8), 9)

    def test_frozenset_width(self):
        """Test case for assigning a frozenset object to width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({5, 4, 8, 6, 3, 7}), 9)

    def test_range_width(self):
        """Test case for assigning a range value to width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(2, 8), 9)

    def test_bytes_width(self):
        """Test case for assigning a byte object to width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b'Best Scool', 9)

    def test_bytearray_width(self):
        """Test case for assigning a bytearray object to width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytearray(b'uvwxyz'), 9)

    def test_memoryview_width(self):
        """Test case for assigning a memoryview object to width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(memoryview(b'uvwxyz'), 9)

    def test_inf_width(self):
        """Test case for assigning infinit object to width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 9)

    def test_nan_width(self):
        """Test case for assigning nan object to width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 9)


class TestRectangleHeight(unittest.TestCase):
    """Unittest for initialization of Rectangle height attribute"""

    def test_negative_height(self):
        """Test case for assigning negative value to height"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(8, -9)

    def test_zero_height(self):
        """Test case for assigning a value of zero to height"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(9, 0)

    def test_none_height(self):
        """Test case for assigning None to height of rectangle"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(8, None)

    def test_str_height(self):
        """Test case for assigning string of charaters to height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(120, "school")

    def test_str_int_height(self):
        """Test case for assigning string of charaters to height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(8, "9")

    def test_float_height(self):
        """Test case for assigning float value to height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, 3.009)

    def test_complex_height(self):
        """Test case for assigning complex value to height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, complex(2))

    def test_dict_height(self):
        """Test case for assigning a dictionary object to height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, {"Jay": 78, "Kay": 87})

    def test_bool_height(self):
        """Test case for assigning a Boolean value to height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, False)

    def test_list_height(self):
        """Test case for assigning a list object to height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, [23, 32, 14, 41])

    def test_set_height(self):
        """Test case for assigning a set object to height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, {6, 7, 8})

    def test_tuple_height(self):
        """Test case for assigning a tuple object to height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, (6, 7, 8))

    def test_frozenset_height(self):
        """Test case for assigning a frozenset object to height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, frozenset({5, 4, 8, 6, 3, 7}))

    def test_range_height(self):
        """Test case for assigning a range value to height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, range(2, 8))

    def test_bytes_height(self):
        """Test case for assigning a byte object to height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, b'Best Scool')

    def test_bytearray_height(self):
        """Test case for assigning a bytearray object to height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, bytearray(b'uvwxyz'))

    def test_memoryview_height(self):
        """Test case for assigning a memoryview object to height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, memoryview(b'uvwxyz'))

    def test_inf_height(self):
        """Test case for assigning infinit object to height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, float('inf'))

    def test_nan_height(self):
        """Test case for assigning nan object to height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, float('nan'))


class TestRectangleX(unittest.TestCase):
    """Unittest for initialization of the x attribute"""

    def test_negative_x(self):
        """Test case for assigning a negative value to coordinate x"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(6, 7, -8, 9)

    def test_none_x(self):
        """Test case for assigning a None object to coordindate x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(8, 9, None)

    def test_str_x(self):
        """Test case for assigning string of characters to coordinate x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(7, 8, "best", 9)

    def test_float_x(self):
        """Test case for assigning a float object to coordinate x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(6, 7, 8.8, 9)

    def test_complex_x(self):
        """Test case for assigning a complex object to coordinate x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(7, 8, complex(9))

    def test_dict_x(self):
        """Test case for assigning a dictionary object to coordinate x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(7, 8, {"Jay": 78, "Kay": 87}, 9)

    def test_bool_x(self):
        """Test case for assigning a Boolean object to coordinate x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(7, 8, False, 9)

    def test_list_x(self):
        """Test case for assigning a list object to coordinate x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 5, [6, 7, 8], 9)

    def test_set_x(self):
        """Test case for assigning a set object to coordinate x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 5, {6, 7, 8}, 9)

    def test_tuple_x(self):
        """Test case for assigning a tuple object to coordinate x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 5, (6, 7, 8), 9)

    def test_frozenset_x(self):
        """Test case for assigning a frozenset object to coordinate x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 4, frozenset({5, 9, 7, 6, 8}))

    def test_range_x(self):
        """Test case for assigning a range value to coordinate x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, range(4, 9))

    def test_bytes_x(self):
        """Test case for assigning a byte object to coordinate x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(8, 9, b'Best School')

    def test_bytearray_x(self):
        """Test case for assigning a bytearray object to coordinate x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(8, 9, bytearray(b'uvwxyz'))

    def test_memoryview_x(self):
        """Test case for assigning memoryview object to coordinate x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(8, 9, memoryview(b'uvwxyz'))

    def test_inf_x(self):
        """Test case for assigning an infinit object to coordinate x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(7, 8, float('inf'), 9)

    def test_nan_x(self):
        """Test case for assigning a Nan object to coordinate x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(7, 8, float('nan'), 9)


class TestRectangleY(unittest.TestCase):
    """Unittest for initialization of the y attribute"""

    def test_negative_y(self):
        """Test case for assigning a negative value to coordinate y"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(6, 7, 8, -9)

    def test_none_y(self):
        """Test case for assigning a None object to coordindate y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 8, 9, None)

    def test_str_y(self):
        """Test case for assigning string of characters to coordinate x"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 8, 9, "best")

    def test_float_y(self):
        """Test case for assigning a float object to coordinate y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(6, 7, 8, 9.9)

    def test_complex_y(self):
        """Test case for assigning a complex object to coordinate y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(6, 7, 8, complex(9))

    def test_dict_y(self):
        """Test case for assigning a dictionary object to coordinate y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 8, 9, {"Jay": 78, "Kay": 87})

    def test_bool_y(self):
        """Test case for assigning a Boolean object to coordinate y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 8, 9, False)

    def test_list_y(self):
        """Test case for assigning a list object to coordinate y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 5, 6, [7, 8, 9])

    def test_set_y(self):
        """Test case for assigning a set object to coordinate y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 5, 6, {7, 8, 9})

    def test_tuple_y(self):
        """Test case for assigning a tuple object to coordinate y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 5, 6, (7, 8, 9))

    def test_frozenset_y(self):
        """Test case for assigning a frozenset object to coordinate y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 3, 4, frozenset({5, 9, 7, 6, 8}))

    def test_range_y(self):
        """Test case for assigning a range value to coordinate y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 3, 4, range(5, 9))

    def test_bytes_y(self):
        """Test case for assigning a byte object to coordinate y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 8, 9, b'Best School')

    def test_bytearray_y(self):
        """Test case for assigning a bytearray object to coordinate y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 8, 9, bytearray(b'uvwxyz'))

    def test_memoryview_y(self):
        """Test case for assigning memoryview object to coordinate y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 8, 9, memoryview(b'uvwxyz'))

    def test_inf_y(self):
        """Test case for assigning an infinit object to coordinate y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 8, 9, float('inf'))

    def test_nan_y(self):
        """Test case for assigning a Nan object to coordinate y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 8, 9, float('nan'))


class TestRectangleHeight(unittest.TestCase):
    """Unittest for initialization of Rectangle height attribute"""

    def test_negative_height(self):
        """Test case for assigning negative value to height"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(8, -9)

    def test_zero_height(self):
        """Test case for assigning a value of zero to height"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(9, 0)

    def test_none_height(self):
        """Test case for assigning None to height of rectangle"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(8, None)

    def test_str_height(self):
        """Test case for assigning string of charaters to height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(120, "school")

    def test_str_int_height(self):
        """Test case for assigning string of charaters to height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(8, "9")

    def test_float_height(self):
        """Test case for assigning float value to height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, 3.009)

    def test_complex_height(self):
        """Test case for assigning complex value to height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, complex(2))

    def test_dict_height(self):
        """Test case for assigning a dictionary object to height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, {"Jay": 78, "Kay": 87})

    def test_bool_height(self):
        """Test case for assigning a Boolean value to height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, False)

    def test_list_height(self):
        """Test case for assigning a list object to height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, [23, 32, 14, 41])

    def test_set_height(self):
        """Test case for assigning a set object to height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, {6, 7, 8})

    def test_tuple_height(self):
        """Test case for assigning a tuple object to height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, (6, 7, 8))

    def test_frozenset_height(self):
        """Test case for assigning a frozenset object to height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, frozenset({5, 4, 8, 6, 3, 7}))

    def test_range_height(self):
        """Test case for assigning a range value to height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, range(2, 8))

    def test_bytes_height(self):
        """Test case for assigning a byte object to height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, b'Best Scool')

    def test_bytearray_height(self):
        """Test case for assigning a bytearray object to height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, bytearray(b'uvwxyz'))

    def test_memoryview_height(self):
        """Test case for assigning a memoryview object to height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, memoryview(b'uvwxyz'))

    def test_inf_height(self):
        """Test case for assigning infinit object to height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, float('inf'))

    def test_nan_height(self):
        """Test case for assigning nan object to height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, float('nan'))


class TestRectangleX(unittest.TestCase):
    """Unittest for initialization of the x attribute"""

    def test_negative_x(self):
        """Test case for assigning a negative value to coordinate x"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(6, 7, -8, 9)

    def test_none_x(self):
        """Test case for assigning a None object to coordindate x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(8, 9, None)

    def test_str_x(self):
        """Test case for assigning string of characters to coordinate x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(7, 8, "best", 9)

    def test_float_x(self):
        """Test case for assigning a float object to coordinate x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(6, 7, 8.8, 9)

    def test_complex_x(self):
        """Test case for assigning a complex object to coordinate x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(7, 8, complex(9))

    def test_dict_x(self):
        """Test case for assigning a dictionary object to coordinate x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(7, 8, {"Jay": 78, "Kay": 87}, 9)

    def test_bool_x(self):
        """Test case for assigning a Boolean object to coordinate x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(7, 8, False, 9)

    def test_list_x(self):
        """Test case for assigning a list object to coordinate x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 5, [6, 7, 8], 9)

    def test_set_x(self):
        """Test case for assigning a set object to coordinate x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 5, {6, 7, 8}, 9)

    def test_tuple_x(self):
        """Test case for assigning a tuple object to coordinate x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 5, (6, 7, 8), 9)

    def test_frozenset_x(self):
        """Test case for assigning a frozenset object to coordinate x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 4, frozenset({5, 9, 7, 6, 8}))

    def test_range_x(self):
        """Test case for assigning a range value to coordinate x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, range(4, 9))

    def test_bytes_x(self):
        """Test case for assigning a byte object to coordinate x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(8, 9, b'Best School')

    def test_bytearray_x(self):
        """Test case for assigning a bytearray object to coordinate x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(8, 9, bytearray(b'uvwxyz'))

    def test_memoryview_x(self):
        """Test case for assigning memoryview object to coordinate x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(8, 9, memoryview(b'uvwxyz'))

    def test_inf_x(self):
        """Test case for assigning an infinit object to coordinate x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(7, 8, float('inf'), 9)

    def test_nan_x(self):
        """Test case for assigning a Nan object to coordinate x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(7, 8, float('nan'), 9)


class TestRectangleY(unittest.TestCase):
    """Unittest for initialization of the y attribute"""

    def test_negative_y(self):
        """Test case for assigning a negative value to coordinate y"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(6, 7, 8, -9)

    def test_none_y(self):
        """Test case for assigning a None object to coordindate y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 8, 9, None)

    def test_str_y(self):
        """Test case for assigning string of characters to coordinate x"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 8, 9, "best")

    def test_float_y(self):
        """Test case for assigning a float object to coordinate y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(6, 7, 8, 9.9)

    def test_complex_y(self):
        """Test case for assigning a complex object to coordinate y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(6, 7, 8, complex(9))

    def test_dict_y(self):
        """Test case for assigning a dictionary object to coordinate y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 8, 9, {"Jay": 78, "Kay": 87})

    def test_bool_y(self):
        """Test case for assigning a Boolean object to coordinate y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 8, 9, False)

    def test_list_y(self):
        """Test case for assigning a list object to coordinate y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 5, 6, [7, 8, 9])

    def test_set_y(self):
        """Test case for assigning a set object to coordinate y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 5, 6, {7, 8, 9})

    def test_tuple_y(self):
        """Test case for assigning a tuple object to coordinate y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 5, 6, (7, 8, 9))

    def test_frozenset_y(self):
        """Test case for assigning a frozenset object to coordinate y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 3, 4, frozenset({5, 9, 7, 6, 8}))

    def test_range_y(self):
        """Test case for assigning a range value to coordinate y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 3, 4, range(5, 9))

    def test_bytes_y(self):
        """Test case for assigning a byte object to coordinate y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 8, 9, b'Best School')

    def test_bytearray_y(self):
        """Test case for assigning a bytearray object to coordinate y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 8, 9, bytearray(b'uvwxyz'))

    def test_memoryview_y(self):
        """Test case for assigning memoryview object to coordinate y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 8, 9, memoryview(b'uvwxyz'))

    def test_inf_y(self):
        """Test case for assigning an infinit object to coordinate y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 8, 9, float('inf'))

    def test_nan_y(self):
        """Test case for assigning a Nan object to coordinate y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 8, 9, float('nan'))