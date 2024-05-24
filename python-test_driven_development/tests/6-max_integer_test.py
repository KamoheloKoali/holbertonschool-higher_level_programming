"""
Unittest for max_integer([..])
"""

import unittest
max_integer = __import__("6-max_integer").max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Class for testing max_integer
    """

    def test_output(self):
        """
        Tests if the output of the program is correct
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)
        self.assertEqual(max_integer([3]), 3)
        self.assertEqual(max_integer([10, 9, 8, 7]), 10)

    def test_args(self):
        """
        Tests if argument is valid
        """
        self.assertRaises(ValueError, max_integer, [])
        self.assertRaises(TypeError, max_integer, None)

    def test_elements(self):
        """
        Tests if all elements of the list are numbers
        """
        self.assertRaises(TypeError, max_integer, [1, 2, 'a'])
        self.assertRaises(TypeError, max_integer, [1, 2, None])
        self.assertRaises(TypeError, max_integer, [1, 2, [3]])
