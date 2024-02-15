#!/usr/bin/python3
"""Unit test module"""

import unittest
from models.base import Base

"""
    Unit Test Classe Contents:
    TestBaseIntantiation ---------------> line 12
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
        self.assertEqual(Base({"Jay": 87, "Kay": 78}).id, {'Jay': 87, 'Kay': 78})

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
        self.assertEqual(Base(frozenset({3, 10, -12})).id, frozenset({10, 3, -12}))

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
