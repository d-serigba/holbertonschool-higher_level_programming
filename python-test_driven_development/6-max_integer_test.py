#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_empty_list(self):
        """Test empty list"""
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """Test list with one element"""
        self.assertEqual(max_integer([5]), 5)

    def test_ordered_list(self):
        """Test ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test unordered list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        """Test list with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_mixed_numbers(self):
        """Test list with mixed positive and negative numbers"""
        self.assertEqual(max_integer([-10, 5, 3, -2]), 5)

    def test_max_at_beginning(self):
        """Test max value at the beginning"""
        self.assertEqual(max_integer([10, 1, 2, 3]), 10)

    def test_max_at_end(self):
        """Test max value at the end"""
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)

    def test_duplicates(self):
        """Test list with duplicate values"""
        self.assertEqual(max_integer([2, 2, 2]), 2)

    def test_large_numbers(self):
        """Test list with large numbers"""
        self.assertEqual(max_integer([1000, 2000, 3000]), 3000)

    def test_default_argument(self):
        """Test default argument"""
        self.assertIsNone(max_integer())

    def test_float_numbers(self):
        """Test list with floats"""
        self.assertEqual(max_integer([1.5, 2.7, 0.3]), 2.7)
