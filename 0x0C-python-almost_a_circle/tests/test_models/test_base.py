#!/usr/bin/python3
"""Unit test module"""

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

"""
    Unit Test Classe Contents:
    TestBaseIntantiation    ---------------> line
    TestBaseToJsonString    ---------------> line
    TestBaseSaveToFile      ---------------> line
    TestBaseFromJsonString  ---------------> line
"""


class TestBaseIntantiation(unittest.TestCase):
    """Unittest for instantiation of the Base class"""

    def test_none_id(self):
        """Test case for None as id"""
        base_1 = Base(None)
        base_2 = Base(None)
        self.assertEqual(base_1.id, base_2.id - 1)

    def test_unique_id(self):
        """Test case for unique id"""
        self.assertEqual(Base(20).id, 20)

    def test_id_public(self):
        """Test case for public id"""
        base = Base(15)
        base.id = 20
        self.assertEqual(base.id, 20)

    def test_nb_instances_private(self):
        """Test case for private attribute id"""
        with self.assertRaises(AttributeError):
            print(Base(15).__nb_instances)

    def test_str_id(self):
        """Test case for a string"""
        self.assertEqual(Base("hello").id, "hello")

    def test_float_id(self):
        """Test case for a floating point id"""
        self.assertEqual(Base(12.5).id, 12.5)

    def test_complex_id(self):
        """Test case for complex id"""
        self.assertEqual(Base(complex(3)).id, complex(3))

    def test_dict_id(self):
        """Test case for a ductionary id"""
        self.assertEqual(Base({"Jay": 87, "Kay": 78}).id,
                         {'Jay': 87, 'Kay': 78})

    def test_bool_id(self):
        """Test case for a Boolean id"""
        self.assertEqual(Base(False).id, False)

    def test_list_id(self):
        """Test case for a list argument"""
        self.assertEqual(Base([17, 71, 81, 18]).id, [17, 71, 81, 18])

    def test_tuple_id(self):
        """Test case for a tupel argument"""
        self.assertEqual(Base((21, 12, 14, 41)).id, (21, 12, 14, 41))

    def test_set_id(self):
        """Test case for a set argument"""
        self.assertEqual(Base({"a", "b", "c"}).id, {'c', 'a', 'b'})

    def test_frozenset_id(self):
        """Test case for a frozenset argument"""
        self.assertEqual(Base(frozenset({3, 10, -12})).id,
                         frozenset({10, 3, -12}))

    def test_range_id(self):
        """Test case for a range id"""
        self.assertEqual(Base(range(4, 14)).id, range(4, 14))

    def test_bytes_id(self):
        """Test case for bytes argument"""
        self.assertEqual(Base(b'ALX').id, b'ALX')

    def test_bytearray_id(self):
        """Test case for a bytearray argument"""
        self.assertEqual(Base(bytearray(b'uvwxyz')).id, bytearray(b'uvwxyz'))

    def test_memoryview_id(self):
        """Test case for a memory view argument"""
        self.assertEqual(Base(memoryview(b'abcefg')).id, memoryview(b'abcefg'))

    def test_inf_id(self):
        """Test case for an infinit id"""
        self.assertEqual(Base(float('inf')).id, float('inf'))

    def test_nan_id(self):
        """Test case for a nan id"""
        self.assertNotEqual(Base(float('nan')).id, float('nan'))

    def test_two_args(self):
        """Test case for two arguments"""
        with self.assertRaises(TypeError):
            Base(6, 3)


class TestBaseToJsonString(unittest.TestCase):
    """Unittest for to_json_string method of Base class"""

    def test_to_json_string_rectangle_type(self):
        """Test case for rectangle initialisation"""
        rec = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(type(Base.to_json_string([rec.to_dictionary()])), str)

    def test_to_json_string_square_type(self):
        """Test case for square initialisation"""
        square = Square(10, 2, 3, 4)
        self.assertEqual(type(Base.to_json_string([square.to_dictionary()])),
                         str)

    def test_to_json_string_square_two_dicts(self):
        """Test case for two squares"""
        square_1 = Square(10, 2, 3, 4)
        square_2 = Square(4, 5, 21, 2)
        list_dicts = [square_1.to_dictionary(), square_2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 163)

    def test_to_json_string_empty_list(self):
        """Test case with an empty list"""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_none(self):
        """Test case for a None argument"""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_no_args(self):
        """Test case for no argument"""
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        """Test case for more than one argument"""
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


class TestBaseSaveToFile(unittest.TestCase):
    """Unittest for save_to_file method of the Base class"""

    @classmethod
    def tearDown(self):
        """Delete any created files"""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_one_rectangle(self):
        """Test case for saving a rectangle object to file"""
        rec = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([rec])
        with open("Rectangle.json", "r", encoding="UTF-8") as file:
            self.assertTrue(len(file.read()) == 105)

    def test_save_to_file_one_square(self):
        """Test case for saving a square object to file"""
        square = Square(10, 7, 2, 8)
        Square.save_to_file([square])
        with open("Square.json", "r", encoding="UTF-8") as file:
            self.assertTrue(len(file.read()) == 83)

    def test_save_to_file_cls_name_for_filename(self):
        """Test case for saving a object by cls"""
        square = Square(10, 7, 2, 8)
        Base.save_to_file([square])
        with open("Base.json", "r", encoding="UTF-8") as file:
            self.assertTrue(len(file.read()) == 83)

    def test_save_to_file_overwrite(self):
        """Test case for overwriting previous data"""
        square = Square(9, 2, 39, 2)
        Square.save_to_file([square])
        square = Square(10, 7, 2, 8)
        Square.save_to_file([square])
        with open("Square.json", "r", encoding="UTF-8") as file:
            self.assertTrue(len(file.read()) == 83)

    def test_save_to_file_none(self):
        """Test case for saving a None to file"""
        Square.save_to_file(None)
        with open("Square.json", "r", encoding="UTF-8") as file:
            self.assertEqual("[]", file.read())

    def test_save_to_file_empty_list(self):
        """Test case for saving an empty list"""
        Square.save_to_file([])
        with open("Square.json", "r", encoding="UTF-8") as file:
            self.assertEqual("[]", file.read())

    def test_save_to_file_no_args(self):
        """Test case for saving to file with an empty argument"""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_one_arg(self):
        """Test case for saving with more than one argument"""
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)


class TestBaseFromJsonString(unittest.TestCase):
    """Unittests for from_json_string method of Base class"""

    def test_from_json_string_type(self):
        """Test case for the type of returned object"""
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(list_output), list)

    def test_from_json_string_rectangle(self):
        """Test case for returning a json string from a rectangle object"""
        list_input = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_square(self):
        """Test case for returning a square object from a json string"""
        list_input = [{"id": 89, "size": 10, "height": 4}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_none(self):
        """Test case for assinging None as parameter"""
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        """Test case for assigning an empty list"""
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_args(self):
        """Test case for assigning no parameter"""
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_than_one_arg(self):
        """Test case for assigning more than one argument"""
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)
