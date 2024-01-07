#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Unittest for max_integer([..])"""
    def test_empty_list(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([]), None)

    def test_no_args(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer(), None)

    def test_with_one_el(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([100]), 100)

    def test_ordered_list(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6]), 6)

    def test_unordered_list(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([5, 7, 9, 3, 0, 55]), 55)

    def test_list_with_negative(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([5, -3, 7, 8, -10, 6, 0]), 8)

    def test_all_negative(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([-1, -9, -4, -3, -4]), -1)

    def test_list_with_floats(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([3, 5.678, 5, 44.9, 56, 55.45678]), 56)

    def test_list_of_floats(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([56.987, 34.853, 69.2385, 70.3456]), 70.3456)

    def test_inf(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([1, float('inf'), float('-inf')]), float('inf'))

    def test_nan(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([100, float('nan'), 1000]), 1000)

    def test_None(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_misxed_list(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer([100, "Biba"])

    def test_arg_int(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer(100)

    def test_arg_float(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer(100.1001)

    def test_arg_str(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer("Biba"), "i")


if __name__ == "__main__":
    unittest.main()
