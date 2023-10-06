#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ unitest for max integer"""
    def test_no_arg(self):
        """unitest for max integer"""
        self.assertEqual(max_integer(), None)

    def test_empty_list(self):
        """unitest for max integer"""
        self.assertEqual(max_integer([]), None)

    def test_one(self):
        """unitest for max integer"""
        self.assertEqual(max_integer([98]), 98)

    def test_identical(self):
        """unitest for max integer"""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_max_start(self):
        """unitest for max integer"""
        self.assertEqual(max_integer([5, 4, 3, 2]), 5)

    def test_ordered(self):
        """unitest for max integer"""
        self.assertEqual(max_integer([2, 4, 8, 10]), 10)

    def test_pos_and_neg(self):
        """unitest for max integer"""
        self.assertEqual(max_integer([-23, 58, 24, 100, 88]), 100)

    def test_all_neg(self):
        """unitest for max integer"""
        self.assertEqual(max_integer([-33, -32, -41, -100, -50]), -32)


if __name__ == '__main__':
    unittest.main()
