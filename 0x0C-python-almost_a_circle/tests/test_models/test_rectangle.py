#!/usr/bin/python3
"""test unit for base class
"""

import unittest
import models.base as B
import models.rectangle as R
from io import StringIO
from unittest.mock import patch


class TestRectangle(unittest.TestCase):
    """

    Note:
        this class has no class attributes

    Args:
        arg1 (type):

    Methods:
        __init__: init the class attributes
    """
    def test_docs(self):
        '''Test docstrings for
            module, class, method'''
        self.assertIsNotNone(R.__doc__)
        self.assertGreater(len(R.__doc__), 0)
        self.assertIsNotNone(R.Rectangle.__doc__)
        self.assertGreater(len(R.Rectangle.__doc__), 0)
        self.assertIsNotNone(R.Rectangle.__init__.__doc__)
        self.assertGreater(len(R.Rectangle.__init__.__doc__), 0)

    def setUp(self) -> None:
        '''setup cls attrs
        '''
        B.Base._Base__nb_objects = 0

    def test_attr_privacy(self):
        '''is nb_object private?
        '''
        rec = R.Rectangle(1, 1, 1)
        self.assertIn("id", rec.__dict__)
        self.assertIn("_Rectangle__width", rec.__dict__)
        self.assertNotIn("width", rec.__dict__)
        self.assertIn("_Rectangle__height", rec.__dict__)
        self.assertNotIn("height", rec.__dict__)
        self.assertIn("_Rectangle__x", rec.__dict__)
        self.assertNotIn("x", rec.__dict__)
        self.assertIn("_Rectangle__y", rec.__dict__)
        self.assertNotIn("y", rec.__dict__)

    def test_attr_value(self):
        """
        Tests for default values
        """
        rec = R.Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rec.width, 1)
        self.assertEqual(rec.height, 2)
        self.assertEqual(rec.x, 3)
        self.assertEqual(rec.y, 4)
        self.assertEqual(rec.id, 5)

    def test_attr_value_empty(self):
        """
        Tests for default values
        """
        rec = R.Rectangle(1, 2)
        self.assertEqual(rec.width, 1)
        self.assertEqual(rec.height, 2)
        self.assertEqual(rec.x, 0)
        self.assertEqual(rec.y, 0)
        self.assertIsNotNone(rec.id)

    def test_setter(self):
        """
        Tests for setter
        """
        rec = R.Rectangle(1, 2)
        rec.width = 11
        self.assertEqual(rec.width, 11)
        rec.height = 12
        self.assertEqual(rec.height, 12)
        rec.x = 13
        self.assertEqual(rec.x, 13)
        rec.y = 14
        self.assertEqual(rec.y, 14)
        rec.id = 15
        self.assertEqual(rec.id, 15)

    def test_no_args(self):
        """
        Tests for no arguments
        """
        with self.assertRaises(TypeError) as err:
            R.Rectangle()
        self.assertEqual(
            str(err.exception),
            "Rectangle.__init__() missing 2 required positional" +
            " arguments: 'width' and 'height'",
        )
        with self.assertRaises(TypeError) as err:
            R.Rectangle(1)
        self.assertEqual(
            str(err.exception),
            "Rectangle.__init__() missing 1 required positional" +
            " argument: 'height'",
        )

    def test_too_many_args(self):
        """
        Tests for too many arguments
        """
        with self.assertRaises(TypeError) as err:
            R.Rectangle(1, 2, 3, 4, 5, 6)
        self.assertEqual(
            str(err.exception),
            "Rectangle.__init__() takes from 3 to 6 positional" +
            " arguments but 7 were given",
        )

    def test_width_validation(self):
        """
        Tests for width validation
        """
        with self.assertRaises(TypeError) as err:
            R.Rectangle(True, 1)
            R.Rectangle("miw", 1)
            R.Rectangle([1, 2], 1)
            R.Rectangle(1.2, 1)
            R.Rectangle(float("inf"), 1)
            R.Rectangle(float("nan"), 1)
        self.assertEqual(str(err.exception), "width must be an integer")
        with self.assertRaises(ValueError) as err:
            R.Rectangle(0, 1)
            R.Rectangle(-1, 1)
        self.assertEqual(str(err.exception), "width must be > 0")

    def test_height_validation(self):
        """
        Tests for heigth validation
        """
        with self.assertRaises(TypeError) as err:
            R.Rectangle(1, True)
            R.Rectangle(1, "miw")
            R.Rectangle(1, [1, 2])
            R.Rectangle(1, 1.2)
            R.Rectangle(1, float("inf"))
            R.Rectangle(1, float("nan"))
        self.assertEqual(str(err.exception), "height must be an integer")
        with self.assertRaises(ValueError) as err:
            R.Rectangle(1, 0)
            R.Rectangle(1, -1)
        self.assertEqual(str(err.exception), "height must be > 0")

    def test_x_validation(self):
        """
        Tests for x validation
        """
        rec = R.Rectangle(1, 1)
        with self.assertRaises(TypeError) as err:
            rec.x = True
            rec.x = "miw"
            rec.x = {}
            rec.x = 1.9
            rec.x = [1]
            rec.x = float("inf")
            rec.x = float("nan")
        self.assertEqual(str(err.exception), "x must be an integer")
        with self.assertRaises(ValueError) as err:
            rec.x = -1
        self.assertEqual(str(err.exception), "x must be >= 0")

    def test_y_validation(self):
        """
        Tests for y validation
        """
        rec = R.Rectangle(1, 1)
        with self.assertRaises(TypeError) as err:
            rec.y = True
            rec.y = "miw"
            rec.y = {}
            rec.y = 1.9
            rec.y = [1]
            rec.y = float("inf")
            rec.y = float("nan")
        self.assertEqual(str(err.exception), "y must be an integer")
        with self.assertRaises(ValueError) as err:
            rec.y = -1
        self.assertEqual(str(err.exception), "y must be >= 0")

    def test_area(self):
        """
        Tests for area
        """
        self.assertEqual(R.Rectangle(1, 1).area(), 1)
        self.assertEqual(R.Rectangle(2, 5).area(), 10)
        self.assertEqual(R.Rectangle(5, 4, 3).area(), 20)
        self.assertEqual(R.Rectangle(5, 5, 4, 3).area(), 25)
        self.assertEqual(R.Rectangle(1, 2, 3, 4, 5).area(), 2)

    def test_display_without_location(self):
        """
        Tests for display without location
        """
        with patch("sys.stdout", new=StringIO()) as fo:
            R.Rectangle(1, 1).display()
            self.assertEqual(fo.getvalue(), "#\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            R.Rectangle(1, 2).display()
            self.assertEqual(fo.getvalue(), "#\n#\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            R.Rectangle(2, 2).display()
            self.assertEqual(fo.getvalue(), "##\n##\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            R.Rectangle(4, 6).display()
            self.assertEqual(fo.getvalue(),
                             "####\n####\n####\n####\n####\n####\n")

    def test_str(self):
        """
        Tests for str and print
        """
        with patch("sys.stdout", new=StringIO()) as fo:
            print(R.Rectangle(3, 2))
            self.assertEqual(fo.getvalue(), "[Rectangle] (1) 0/0 - 3/2\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            print(R.Rectangle(1, 2, 3, 4, 5))
            self.assertEqual(fo.getvalue(), "[Rectangle] (5) 3/4 - 1/2\n")

    def test_display_with_location(self):
        """
        Tests for display with location
        """
        with patch("sys.stdout", new=StringIO()) as fo:
            R.Rectangle(3, 3, 1, 1).display()
            self.assertEqual(fo.getvalue(), "\n ###\n ###\n ###\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            R.Rectangle(3, 3, 0, 1).display()
            self.assertEqual(fo.getvalue(), "\n###\n###\n###\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            R.Rectangle(3, 3, 1, 0).display()
            self.assertEqual(fo.getvalue(), " ###\n ###\n ###\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            R.Rectangle(3, 3, 3, 3).display()
            self.assertEqual(fo.getvalue(), "\n\n\n   ###\n   ###\n   ###\n")

    def test_update_args(self):
        """
        Tests for update with *args
        """
        rec = R.Rectangle(10, 10, 10, 10, 10)
        with patch("sys.stdout", new=StringIO()) as fo:
            rec.update()
            print(rec)
            self.assertEqual(fo.getvalue(), "[Rectangle] (10) 10/10 - 10/10\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            rec.update(1)
            print(rec)
            self.assertEqual(fo.getvalue(), "[Rectangle] (1) 10/10 - 10/10\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            rec.update(1, 2)
            print(rec)
            self.assertEqual(fo.getvalue(), "[Rectangle] (1) 10/10 - 2/10\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            rec.update(1, 2, 3)
            print(rec)
            self.assertEqual(fo.getvalue(), "[Rectangle] (1) 10/10 - 2/3\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            rec.update(1, 2, 3, 4)
            print(rec)
            self.assertEqual(fo.getvalue(), "[Rectangle] (1) 4/10 - 2/3\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            rec.update(1, 2, 3, 4, 5)
            print(rec)
            self.assertEqual(fo.getvalue(), "[Rectangle] (1) 4/5 - 2/3\n")

    def test_update_re_args(self):
        """
        Tests for reupdate with *args
        """
        rec = R.Rectangle(10, 10, 10, 10, 10)
        with patch("sys.stdout", new=StringIO()) as fo:
            rec.update(2, 5, 30, 19, 45)
            print(rec)
            self.assertEqual(fo.getvalue(), "[Rectangle] (2) 19/45 - 5/30\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            rec.update(4, 28, 12, 3, 98)
            print(rec)
            self.assertEqual(fo.getvalue(), "[Rectangle] (4) 3/98 - 28/12\n")

    def test_update_kwargs_1(self):
        """
        Tests for update with **kwargs pt. 1
        """
        rec = R.Rectangle(10, 10, 10, 10, 10)
        with patch("sys.stdout", new=StringIO()) as fo:
            rec.update(x=4)
            print(rec)
            self.assertEqual(fo.getvalue(), "[Rectangle] (10) 4/10 - 10/10\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            rec.update(height=3)
            print(rec)
            self.assertEqual(fo.getvalue(), "[Rectangle] (10) 4/10 - 10/3\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            rec.update(id=1)
            print(rec)
            self.assertEqual(fo.getvalue(), "[Rectangle] (1) 4/10 - 10/3\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            rec.update(y=5)
            print(rec)
            self.assertEqual(fo.getvalue(), "[Rectangle] (1) 4/5 - 10/3\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            rec.update(width=2)
            print(rec)
            self.assertEqual(fo.getvalue(), "[Rectangle] (1) 4/5 - 2/3\n")

    def test_update_kwargs_multiple(self):
        """
        Tests for update with **kwargs pt. 2
        """
        dictionary = {"x": 30, "y": 40}
        rec = R.Rectangle(10, 20)
        with patch("sys.stdout", new=StringIO()) as fo:
            rec.update(**dictionary)
            print(rec)
            self.assertEqual(fo.getvalue(), "[Rectangle] (1) 30/40 - 10/20\n")
        dictionary = {"id": 89, "width": 97, "height": 21, "x": 65, "y": 0}
        with patch("sys.stdout", new=StringIO()) as fo:
            rec.update(**dictionary)
            print(rec)
            self.assertEqual(fo.getvalue(), "[Rectangle] (89) 65/0 - 97/21\n")
        dictionary = {"width": 89, "height": 97, "y": 21, "id": 65, "x": 0}
        with patch("sys.stdout", new=StringIO()) as fo:
            rec.update(**dictionary)
            print(rec)
            self.assertEqual(fo.getvalue(), "[Rectangle] (65) 0/21 - 89/97\n")

    def test_update_mix(self):
        """
        Tests for update with mix
        """
        rec = R.Rectangle(10, 20)
        with patch("sys.stdout", new=StringIO()) as fo:
            rec.update(69, y=30)
            print(rec)
            self.assertEqual(fo.getvalue(), "[Rectangle] (69) 0/0 - 10/20\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            rec.update(69, id=30)
            print(rec)
            self.assertEqual(fo.getvalue(), "[Rectangle] (69) 0/0 - 10/20\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            rec.update(69, 12, 19, 34, 77, y=30)
            print(rec)
            self.assertEqual(fo.getvalue(), "[Rectangle] (69) 34/77 - 12/19\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            rec.update(69, 12, 19, 34, 77, id=30, width=22,
                       height=21, x=11, y=13)
            print(rec)
            self.assertEqual(fo.getvalue(), "[Rectangle] (69) 34/77 - 12/19\n")
        rec = R.Rectangle(10, 20)
        with patch("sys.stdout", new=StringIO()) as fo:
            rec.update(69, id=30, width=22, height=21, x=11, y=13)
            print(rec)
            self.assertEqual(fo.getvalue(), "[Rectangle] (69) 0/0 - 10/20\n")

    def test_to_dictionary(self):
        """
        Tests for to dictionary pt.1
        """
        test_dict = {"id": 1, "width": 1, "height": 2, "x": 0, "y": 0}
        obj_dict = R.Rectangle(1, 2).to_dictionary()
        self.assertIsInstance(obj_dict, dict)
        self.assertCountEqual(test_dict.keys(), obj_dict.keys())
        self.assertCountEqual(test_dict.values(), obj_dict.values())

    def test_to_dictionary_2(self):
        """
        Tests for to dictionary pt. 2
        """
        test_dict = {"id": 1, "width": 1, "height": 2, "x": 3, "y": 0}
        obj_dict = R.Rectangle(1, 2, 3).to_dictionary()
        self.assertIsInstance(obj_dict, dict)
        self.assertCountEqual(test_dict.keys(), obj_dict.keys())
        self.assertCountEqual(test_dict.values(), obj_dict.values())

    def test_to_dictionary_3(self):
        """
        Tests for to dictionary pt. 3
        """
        test_dict = {"id": 1, "width": 1, "height": 2, "x": 3, "y": 4}
        obj_dict = R.Rectangle(1, 2, 3, 4).to_dictionary()
        self.assertIsInstance(obj_dict, dict)
        self.assertCountEqual(test_dict.keys(), obj_dict.keys())
        self.assertCountEqual(test_dict.values(), obj_dict.values())

    def test_to_dictionary_4(self):
        """
        Tests for to dictionary pt. 4
        """
        test_dict = {"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}
        obj_dict = R.Rectangle(1, 2, 3, 4, 5).to_dictionary()
        self.assertIsInstance(obj_dict, dict)
        self.assertCountEqual(test_dict.keys(), obj_dict.keys())
        self.assertCountEqual(test_dict.values(), obj_dict.values())


if __name__ == '__main__':
    unittest.main()
