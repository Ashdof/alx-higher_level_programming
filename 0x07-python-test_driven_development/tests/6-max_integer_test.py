import unittest
max_int = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):

    """Test case for the max-integer functio """

    def test_max_integer(self):
        self.assertEqual(max_int([5, -2, 9, 3]), 9)

    def test_empty_list(self):
        self.assertEqual(max_int([]), None)

    def test_repeated_number(self):
        self.assertEqual(max_int([2500, 2500, 2500]), 2500)

    def test_float_numbers(self):
        self.assertEqual(max_int([32, 22, 23, 33]), 33)

    def test_max_operated_integer(self):
        self.assertEqual(max_int([-2, -7 * -3, 7, -5]), 21)

    def test_neg_numbers(self):
        self.assertEqual(max_int([-15, -7, -4, -1]), -1)

    def test_max_at_beginning(self):
        self.assertEqual(max_int([5, 4, 3, 2, 1]), 5)

    def test_zero_number(self):
        self.assertEqual(max_int([0, 0]), 0)

    def test_big_list(self):
        self.assertEqual(max_int([
            901, 902, 903, 904, 905, 906, 907, 908, 909, 910,
            911, 912, 913, 914, 915, 916, 917, 918, 919, 920,
            919, 918, 917, 1000, 915, 914, 913, 912, 911, 910,
            909, 908, 907, 906, 905, 904, 903, 902, 901]), 1000)

    def test_list_with_loop(self):
        vals = [1, 2, 3, 4, 5, 7]
        self.assertEqual(max_int([i * 5 for i in vals]), 35)

    def test_one_number_in_a_list(self):
        self.assertEqual(max_int([1]), 1)

    def test_string_number_in_a_list(self):
        with self.assertRaises(TypeError):
            max_int([0, '1'])

    def test_tuple_in_a_list(self):
        with self.assertRaises(TypeError):
            max_int([10, (20, 30)])

    def test_dictionary(self):
        with self.assertRaises(KeyError):
            max_int({'key1': 1, 'key2': 2})

    def test_number(self):
        with self.assertRaises(TypeError):
            max_int(1)
