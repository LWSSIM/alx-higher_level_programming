#!/usr/bin/python3
"""
Module for the unittest of the class Square
"""
import models.base as B
import models.square as S
import unittest
from io import StringIO
import os
from unittest.mock import patch


class TestSquare(unittest.TestCase):
    """
    class TestSquare
    """

    def test_module_doc(self):
        """
        test for module doc
        """
        self.assertIsNotNone(S.__doc__)
        self.assertGreater(len(S.__doc__), 0)

    def setUp(self):
        """
        Resets id
        """
        B.Base._Base__nb_objects = 0

    def test_no_new_attrs(self):
        """
        test for no new attributes
        """
        sqr = S.Square(5)
        self.assertNotIn("size", sqr.__dict__)
        self.assertNotIn("_Square__size", sqr.__dict__)
        dictt = {
            "id": 0,
            "_Rectangle__width": 1,
            "_Rectangle__height": 1,
            "_Rectangle__x": 0,
            "_Rectangle__y": 0,
        }
        self.assertCountEqual(dictt, sqr.__dict__)

    def test_no_args(self):
        """
        test for no arguments
        """
        with self.assertRaises(TypeError) as err:
            S.Square()
        self.assertEqual(
            str(err.exception),
            "__init__() missing 1 required positional argument: 'size'",
        )

    def test_too_many_args(self):
        """
        test for too many arguments
        """
        with self.assertRaises(TypeError) as err:
            S.Square(1, 2, 3, 4, 5, 6)
        self.assertEqual(
            str(err.exception),
            "__init__() takes from 2 to 5 positional" +
            " arguments but 7 were given",
        )

    def test_size_validation(self):
        """
        test for size validation
        """
        with self.assertRaises(TypeError) as err:
            S.Square(True)
            S.Square("Hola")
            S.Square([1, 2])
            S.Square(1.2)
            S.Square(float("inf"))
            S.Square(float("nan"))
        self.assertEqual(str(err.exception), "width must be an integer")
        with self.assertRaises(ValueError) as err:
            S.Square(0)
            S.Square(-1)
        self.assertEqual(str(err.exception), "width must be > 0")

    def test_x_validation(self):
        """
        test for x validation
        """
        sqr = S.Square(1)
        with self.assertRaises(TypeError) as err:
            sqr.x = True
            sqr.x = "Hola"
            sqr.x = {}
            sqr.x = 1.2
            sqr.x = [1]
            sqr.x = float("inf")
            sqr.x = float("nan")
        self.assertEqual(str(err.exception), "x must be an integer")
        with self.assertRaises(ValueError) as err:
            sqr.x = -1
        self.assertEqual(str(err.exception), "x must be >= 0")

    def test_y_validation(self):
        """
        test for y validation
        """
        sqr = S.Square(1, 1)
        with self.assertRaises(TypeError) as err:
            sqr.y = True
            sqr.y = "Hola"
            sqr.y = {}
            sqr.y = 1.2
            sqr.y = [1]
            sqr.y = float("inf")
            sqr.y = float("nan")
        self.assertEqual(str(err.exception), "y must be an integer")
        with self.assertRaises(ValueError) as err:
            sqr.y = -1
        self.assertEqual(str(err.exception), "y must be >= 0")

    def test_area(self):
        """
        test for area
        """
        self.assertEqual(S.Square(1).area(), 1)
        self.assertEqual(S.Square(2, 6).area(), 4)
        self.assertEqual(S.Square(5, 6, 6).area(), 25)
        self.assertEqual(S.Square(2, 6, 6, 6).area(), 4)

    def test_display_without_location(self):
        """
        test for display without location
        """
        with patch("sys.stdout", new=StringIO()) as fo:
            S.Square(1).display()
            self.assertEqual(fo.getvalue(), "#\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            S.Square(2).display()
            self.assertEqual(fo.getvalue(), "##\n##\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            S.Square(4).display()
            self.assertEqual(fo.getvalue(), "####\n####\n####\n####\n")

    def test_str(self):
        """
        test for str or print
        """
        with patch("sys.stdout", new=StringIO()) as fo:
            print(S.Square(3))
            self.assertEqual(fo.getvalue(), "[Square] (1) 0/0 - 3\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            print(S.Square(2, 3, 4, 5))
            self.assertEqual(fo.getvalue(), "[Square] (5) 3/4 - 2\n")

    def test_display_with_location(self):
        """
        test for display with location
        """
        with patch("sys.stdout", new=StringIO()) as fo:
            S.Square(3, 1, 1).display()
            self.assertEqual(fo.getvalue(), "\n ###\n ###\n ###\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            S.Square(3, 0, 1).display()
            self.assertEqual(fo.getvalue(), "\n###\n###\n###\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            S.Square(3, 1, 0).display()
            self.assertEqual(fo.getvalue(), " ###\n ###\n ###\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            S.Square(3, 3, 3).display()
            self.assertEqual(fo.getvalue(), "\n\n\n   ###\n   ###\n   ###\n")

    def test_size_setter_and_getter(self):
        """
        test for size setter and getter
        """
        sqr = S.Square(3)
        self.assertEqual(sqr.size, 3)
        self.assertEqual(sqr.width, 3)
        self.assertEqual(sqr.height, 3)
        sqr.size = 18
        self.assertEqual(sqr.size, 18)
        self.assertEqual(sqr.width, 18)
        self.assertEqual(sqr.height, 18)

    def test_update_args(self):
        """
        test for update with *args
        """
        sqr = S.Square(10, 10, 10, 10)
        with patch("sys.stdout", new=StringIO()) as fo:
            sqr.update()
            print(sqr)
            self.assertEqual(fo.getvalue(), "[Square] (10) 10/10 - 10\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            sqr.update(1)
            print(sqr)
            self.assertEqual(fo.getvalue(), "[Square] (1) 10/10 - 10\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            sqr.update(1, 2)
            print(sqr)
            self.assertEqual(fo.getvalue(), "[Square] (1) 10/10 - 2\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            sqr.update(1, 2, 3, 4)
            print(sqr)
            self.assertEqual(fo.getvalue(), "[Square] (1) 3/4 - 2\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            sqr.update(1, 2, 4, 5)
            print(sqr)
            self.assertEqual(fo.getvalue(), "[Square] (1) 4/5 - 2\n")

    def test_update_re_args(self):
        """
        test for reupdate with *args
        """
        sqr = S.Square(10, 10, 10, 10)
        with patch("sys.stdout", new=StringIO()) as fo:
            sqr.update(2, 5, 19, 45)
            print(sqr)
            self.assertEqual(fo.getvalue(), "[Square] (2) 19/45 - 5\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            sqr.update(4, 12, 3, 98)
            print(sqr)
            self.assertEqual(fo.getvalue(), "[Square] (4) 3/98 - 12\n")

    def test_update_kwargs_1(self):
        """
        test for update with **kwargs
        """
        sqr = S.Square(10, 10, 10, 10)
        with patch("sys.stdout", new=StringIO()) as fo:
            sqr.update(x=4)
            print(sqr)
            self.assertEqual(fo.getvalue(), "[Square] (10) 4/10 - 10\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            sqr.update(id=1)
            print(sqr)
            self.assertEqual(fo.getvalue(), "[Square] (1) 4/10 - 10\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            sqr.update(y=5)
            print(sqr)
            self.assertEqual(fo.getvalue(), "[Square] (1) 4/5 - 10\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            sqr.update(width=2)
            print(sqr)
            self.assertEqual(fo.getvalue(), "[Square] (1) 4/5 - 2\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            sqr.update(size=8)
            print(sqr)
            self.assertEqual(fo.getvalue(), "[Square] (1) 4/5 - 8\n")

    def test_update_kwargs_multiple(self):
        """
        test for update with multiple **kwargs
        """
        dictionary = {"x": 30, "y": 40}
        sqr = S.Square(20)
        with patch("sys.stdout", new=StringIO()) as fo:
            sqr.update(**dictionary)
            print(sqr)
            self.assertEqual(fo.getvalue(), "[Square] (1) 30/40 - 20\n")
        dictionary = {"id": 89, "size": 21, "x": 65, "y": 0}
        with patch("sys.stdout", new=StringIO()) as fo:
            sqr.update(**dictionary)
            print(sqr)
            self.assertEqual(fo.getvalue(), "[Square] (89) 65/0 - 21\n")
        dictionary = {"id": 89, "width": 21, "x": 65, "y": 0}
        with patch("sys.stdout", new=StringIO()) as fo:
            sqr.update(**dictionary)
            print(sqr)
            self.assertEqual(fo.getvalue(), "[Square] (89) 65/0 - 21\n")
        dictionary = {"size": 89, "y": 21, "id": 65, "x": 0}
        with patch("sys.stdout", new=StringIO()) as fo:
            sqr.update(**dictionary)
            print(sqr)
            self.assertEqual(fo.getvalue(), "[Square] (65) 0/21 - 89\n")

    def test_update_mix(self):
        """
        test for mix
        """
        sqr = S.Square(10)
        with patch("sys.stdout", new=StringIO()) as fo:
            sqr.update(69, y=30)
            print(sqr)
            self.assertEqual(fo.getvalue(), "[Square] (69) 0/0 - 10\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            sqr.update(69, id=30)
            print(sqr)
            self.assertEqual(fo.getvalue(), "[Square] (69) 0/0 - 10\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            sqr.update(69, 12, 34, 77, y=30)
            print(sqr)
            self.assertEqual(fo.getvalue(), "[Square] (69) 34/77 - 12\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            sqr.update(69, 12, 19, 34, id=30, size=22, x=11, y=13)
            print(sqr)
            self.assertEqual(fo.getvalue(), "[Square] (69) 19/34 - 12\n")
        sqr = S.Square(20)
        with patch("sys.stdout", new=StringIO()) as fo:
            sqr.update(69, id=30, size=22, x=11, y=13)
            print(sqr)
            self.assertEqual(fo.getvalue(), "[Square] (69) 0/0 - 20\n")

    def test_save_to_file_file_exist_square(self):
        """
        save to file with none input square
        """
        S.Square.save_to_file(None)
        self.assertTrue(os.path.exists(os.path.join(".", "Square.json")))
        with open("Square.json", "r") as f:
            file_contents = f.read()
        self.assertEqual(file_contents, "[]")

    def test_save_to_file_file_exist_square_empty(self):
        """
        save to file with [] input square
        """
        S.Square.save_to_file([])
        self.assertTrue(os.path.exists(os.path.join(".", "Square.json")))
        with open("Square.json", "r") as f:
            file_contents = f.read()
        self.assertEqual(file_contents, "[]")

    def test_to_dictionary(self):
        """
        test for to dictionary pt. 1
        """
        test_dict = {"id": 1, "size": 1, "x": 0, "y": 0}
        sqr_dict = S.Square(1).to_dictionary()
        self.assertIsInstance(sqr_dict, dict)
        self.assertCountEqual(test_dict.keys(), sqr_dict.keys())
        self.assertCountEqual(test_dict.values(), sqr_dict.values())

    def test_to_dictionary_2(self):
        """
        test for to dictionary pt. 2
        """
        test_dict = {"id": 1, "size": 1, "x": 3, "y": 0}
        sqr_dict = S.Square(1, 3).to_dictionary()
        self.assertIsInstance(sqr_dict, dict)
        self.assertCountEqual(test_dict.keys(), sqr_dict.keys())
        self.assertCountEqual(test_dict.values(), sqr_dict.values())

    def test_to_dictionary_3(self):
        """
        test for to dictionary pt. 3
        """
        test_dict = {"id": 1, "size": 1, "x": 3, "y": 4}
        sqr_dict = S.Square(1, 3, 4).to_dictionary()
        self.assertIsInstance(sqr_dict, dict)
        self.assertCountEqual(test_dict.keys(), sqr_dict.keys())
        self.assertCountEqual(test_dict.values(), sqr_dict.values())

    def test_to_dictionary_4(self):
        """
        test for to dictionary pt. 4
        """
        test_dict = {"id": 5, "size": 1, "x": 3, "y": 4}
        sqr_dict = S.Square(1, 3, 4, 5).to_dictionary()
        self.assertIsInstance(sqr_dict, dict)
        self.assertCountEqual(test_dict.keys(), sqr_dict.keys())
        self.assertCountEqual(test_dict.values(), sqr_dict.values())


if __name__ == "__main__":
    unittest.main()
