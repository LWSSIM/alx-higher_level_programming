#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
        Class using the unit-test method to test:
            6-max_integer.
    """

    def test_mod_docstr(self):
        """
            tests module docstrings
        """
        docstr = __import__("6-max_integer").__doc__

        self.assertTrue(len(docstr) > 0)

    def test_fn_docstring(self):
        """
            tests fn docstring
        """
        docstr_fn = __import__("6-max_integer").max_integer.__doc__

        self.assertTrue(len(docstr_fn) > 0)

    def test_correct_list(self):
        """
            Normal fn use case test:
                correct type and lenght input
        """
        test_list = [1, 9, 6, 8, 5]
        self.assertEqual(max_integer(test_list), 9)

    def test_ordered_list(self):
        """
            fn use case test:
                correct type and lenght input
                the list is sorted in ascending order
        """
        test_list = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(test_list), 5)

    def test_rev_ordered_list(self):
        """
            fn use case test:
                correct type and lenght input
                the list is sorted in descending order
        """
        test_list = [1, 2, 3, 4, 5]
        test_list.reverse()
        self.assertEqual(max_integer(test_list), 5)

    def test_none_input_list(self):
        """
            fn use case test:
                None list input
                the list is empty
        """
        test_list = []
        self.assertIsNone(max_integer(test_list))

    def test_float_type_list(self):
        """
            fn use case test:
                float list input
        """
        test_list = [1.5, 69.3, 402.05, 99]
        self.assertEqual(max_integer(test_list), 402.05)

    def test_negative_list(self):
        """
            fn use case test:
                negative list input
        """
        test_list = [-1, -2, -3, -4, -5]
        self.assertEqual(max_integer(test_list), -1)

    def test_mixed_list(self):
        """
            fn use case test:
                negative and positive list inputs +
                different types
        """
        test_list = [-1, 2.99, 3.6, -499, -5]
        self.assertEqual(max_integer(test_list), 3.6)

    def test_single_item_list(self):
        """
            fn use case test:
                single input
        """
        test_list = [999]
        self.assertEqual(max_integer(test_list), 999)

    def test_large_list(self):
        """
            fn use case test:
                large input
        """
        test_list = [99999999, 6666666, 333333333, 8888888888]
        self.assertEqual(max_integer(test_list), 8888888888)

    if __name__ == "__main__":
        unittest.main()

