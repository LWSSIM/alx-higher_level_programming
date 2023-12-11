#!/usr/bin/python3
"""test unit for base class
"""

import unittest
import models.base as B
import models.rectangle as R
import models.square as S
import os


class TestBase(unittest.TestCase):
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
        self.assertIsNotNone(B.__doc__)
        self.assertGreater(len(B.__doc__), 0)
        self.assertIsNotNone(B.Base.__doc__)
        self.assertGreater(len(B.Base.__doc__), 0)
        self.assertIsNotNone(B.Base.__init__.__doc__)
        self.assertGreater(len(B.Base.__init__.__doc__), 0)

    def setUp(self) -> None:
        '''setup cls attrs
        '''
        B.Base._Base__nb_objects = 0

    def test_attr_privacy(self):
        '''is nb_object private?
        '''
        b1 = B.Base.__nb_objects = 9
        self.assertNotIsInstance(b1, B.Base)

    def test_id(self):
        '''test id setting and incrementing
        '''
        b1 = B.Base()
        b2 = B.Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_id_vals(self):
        '''id values
        '''
        self.assertEqual(B.Base(0).id, 0)
        self.assertEqual(B.Base(20).id, 20)
        self.assertEqual(B.Base(-20).id, -20)

    def test_id_none(self):
        '''id = None use case
        '''
        b1 = B.Base(None)
        b2 = B.Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_more_args(self):
        """test bad args input
        """
        with self.assertRaises(TypeError):
            B.Base(1, 1)

    def test_to_json_string(self):
        """
        Test with 1 dictionary
        """
        dict_val = R.Rectangle(1, 9, 9, 9).to_dictionary()
        str_rep = str(dict_val)
        result = B.Base.to_json_string(dict_val)
        self.assertIsInstance(result, str)
        self.assertEqual(eval(result), eval(str_rep))

    def test_to_json_string_empty_and_none(self):
        """
        Test with 1 dictionary
        """
        res = B.Base.to_json_string([])
        self.assertIsInstance(res, str)
        self.assertEqual(res, "[]")

        res = B.Base.to_json_string(None)
        self.assertIsInstance(res, str)
        self.assertEqual(res, "[]")

    def test_save_to_file_file_exist_rectangle(self):
        """
        save to file with none input rectangle
        """
        R.Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists(os.path.join(".", "Rectangle.json")))
        with open("Rectangle.json", "r") as f:
            file_contents = f.read()
        self.assertEqual(file_contents, "[]")

    def test_save_to_file_file_exist_square(self):
        """
        save to file with none input square
        """
        S.Square.save_to_file(None)
        self.assertTrue(os.path.exists(os.path.join(".", "Square.json")))
        with open("Square.json", "r") as f:
            file_contents = f.read()
        self.assertEqual(file_contents, "[]")

    def test_save_to_file_file_exist_rectangle_empty(self):
        """
        save to file with [] input rectangle
        """
        R.Rectangle.save_to_file([])
        self.assertTrue(os.path.exists(os.path.join(".", "Rectangle.json")))
        with open("Rectangle.json", "r") as f:
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

    def test_save_to_file_values_rectangle(self):
        """
        save to file with obj input rectangle
        """
        r1 = R.Rectangle(1, 1, 1, 1, 1)
        R.Rectangle.save_to_file([r1])
        dict_vals = r1.to_dictionary()

        self.assertTrue(os.path.exists(os.path.join(".", "Rectangle.json")))
        with open("Rectangle.json", "r") as f:
            file_contents = f.read()
        self.assertEqual(file_contents, B.Base.to_json_string([dict_vals]))

    def test_save_to_file_values_square(self):
        """
        save to file with [] input square
        """
        s1 = S.Square(1, 1, 1, 1)
        S.Square.save_to_file([s1])
        dict_vals = s1.to_dictionary()
        self.assertTrue(os.path.exists(os.path.join(".", "Square.json")))
        with open("Square.json", "r") as f:
            file_contents = f.read()
        self.assertEqual(file_contents, B.Base.to_json_string([dict_vals]))

    def test_save_to_file_multiple_rectangle(self):
        """ save to file with multiple instances of rectangle
        """
        d_list = []
        d_list.append(R.Rectangle(2, 1))
        d_list.append(R.Rectangle(5, 9, 1, 1, 8))
        d_list.append(R.Rectangle(2, 6, 3, 4))
        R.Rectangle.save_to_file(d_list)
        self.assertTrue(os.path.exists(os.path.join(".", "Rectangle.json")))
        with open("Rectangle.json", "r") as f:
            file_contents = f.read()
        self.setUp()
        r_list = []
        r_list.append(R.Rectangle(2, 1).to_dictionary())
        r_list.append(R.Rectangle(5, 9, 1, 1, 8).to_dictionary())
        r_list.append(R.Rectangle(2, 6, 3, 4).to_dictionary())
        self.assertEqual(file_contents, B.Base.to_json_string(r_list))

    def test_save_to_file_multiple_square(self):
        """ save to file with multiple instances of square
        """
        d_list = []
        d_list.append(S.Square(8, 1))
        d_list.append(S.Square(1, 2, 2, 9))
        d_list.append(S.Square(3, 5, 3, 4))
        S.Square.save_to_file(d_list)
        self.assertTrue(os.path.exists(os.path.join(".", "Square.json")))
        with open("Square.json", "r") as f:
            file_contents = f.read()
        self.setUp()
        r_list = []
        r_list.append(S.Square(8, 1).to_dictionary())
        r_list.append(S.Square(1, 2, 2, 9).to_dictionary())
        r_list.append(S.Square(3, 5, 3, 4).to_dictionary())
        self.assertEqual(file_contents, B.Base.to_json_string(r_list))


class TestBaseCreate(unittest.TestCase):
    '''test Base: create method
    '''
    def test_create_rectangle(self):
        '''is the rect, dict created valid?
        '''
        r1 = R.Rectangle(3, 5, 4, 4)
        r1_dict = r1.to_dictionary()
        r2 = R.Rectangle.create(**r1_dict)
        self.assertEqual(str(r1), f"[Rectangle] ({r1.id}) 4/4 - 3/5")
        self.assertEqual(str(r2), f"[Rectangle] ({r2.id}) 4/4 - 3/5")
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

    def test_create_square(self):
        '''is the rect, dict created valid?
        '''
        s1 = S.Square(3, 5, 4)
        s1_dict = s1.to_dictionary()
        s2 = S.Square.create(**s1_dict)
        self.assertEqual(str(s1), f"[Square] ({s1.id}) 5/4 - 3")
        self.assertEqual(str(s2), f"[Square] ({s2.id}) 5/4 - 3")
        self.assertIsNot(s1, s2)
        self.assertNotEqual(s1, s2)


class TestBaseFromJSONStr(unittest.TestCase):
    '''tests the from json str base method
    '''
    def test_type_and_IO_rectangle(self):
        '''is the type and file IO values correct
        '''
        l_in = [{'id': 1, 'width': 1, 'height': 1, 'x': 1, 'y': 1}]
        json_in = R.Rectangle.to_json_string(l_in)
        json_out = R.Rectangle.from_json_string(json_in)
        self.assertEqual(list, type(json_out))
        self.assertEqual(l_in, json_out)

    def test_2_IO_rectangle(self):
        '''is the type and file IO values correct
        '''
        l_in = [{'id': 1, 'width': 1, 'height': 1, 'x': 1, 'y': 1},
                {'id': 1, 'width': 1, 'height': 1, 'x': 1, 'y': 1}]
        json_in = R.Rectangle.to_json_string(l_in)
        json_out = R.Rectangle.from_json_string(json_in)
        self.assertEqual(list, type(json_out))
        self.assertEqual(l_in, json_out)

    def test_type_and_IO_square(self):
        '''is the type and file IO values correct
        '''
        l_in = [{'id': 1, 'width': 1, 'height': 1, 'x': 1, 'y': 1},
                {'id': 1, 'width': 1, 'height': 1, 'x': 1, 'y': 1}]
        json_in = S.Square.to_json_string(l_in)
        json_out = S.Square.from_json_string(json_in)
        self.assertEqual(list, type(json_out))
        self.assertEqual(l_in, json_out)

    def test2_IO_square(self):
        '''is the type and file IO values correct
        '''
        l_in = [{'id': 1, 'size': 1, 'x': 1, 'y': 1}]
        json_in = S.Square.to_json_string(l_in)
        json_out = S.Square.from_json_string(json_in)
        self.assertEqual(list, type(json_out))
        self.assertEqual(l_in, json_out)

    def test_None(self):
        self.assertEqual(B.Base.from_json_string(None), [])

    def test_no_args(self):
        with self.assertRaises(TypeError):
            B.Base.from_json_string()

    def test_wrong_input(self):
        with self.assertRaises(TypeError):
            B.Base.from_json_string([], 8)


class TestBaseLoadFromFile(unittest.TestCase):
    '''test base method -> load_from_file
    '''

    def test_load_rectangle(self):
        r1 = R.Rectangle(1, 8, 4)
        r2 = R.Rectangle(2, 2, 3, 4, 5)
        R.Rectangle.save_to_file([r1, r2])
        list_output = R.Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_output[0]))
        self.assertEqual(str(r2), str(list_output[1]))
        self.assertTrue(all(type(obj)) == R.Rectangle for obj in list_output)

    def test_load_square(self):
        r1 = S.Square(1, 8, 4)
        r2 = S.Square(2, 2, 3, 4)
        S.Square.save_to_file([r1, r2])
        list_output = S.Square.load_from_file()
        self.assertEqual(str(r1), str(list_output[0]))
        self.assertEqual(str(r2), str(list_output[1]))
        self.assertTrue(all(type(obj)) == S.Square for obj in list_output)

    def test_bad_args(self):
        '''tests args validity'''
        with self.assertRaises(TypeError):
            B.Base.load_from_file([], 2)

    @classmethod
    def tearDown(cls):
        '''deletes created .json files'''
        files = ["Rectangle.json", "Square.json"]
        for file in files:
            try:
                os.remove(file)
            except FileNotFoundError:
                pass


if __name__ == '__main__':
    unittest.main()
