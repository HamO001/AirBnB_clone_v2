import os
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.engine.file_storage import FileStorage


class TestHBNBCommand(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        cls.HBNB = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        del cls.HBNB

    def setUp(self):
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_create_for_errors(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create")
            self.assertEqual("** class name missing **\n", f.getvalue())

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create asdfsfsd")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

    def test_create_command_validity(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create BaseModel")
            bm = f.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create User")
            us = f.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create State")
            st = f.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create Place")
            pl = f.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create City")
            ct = f.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create Review")
            rv = f.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create Amenity")
            am = f.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all BaseModel")
            self.assertIn(bm, f.getvalue())

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all User")
            self.assertIn(us, f.getvalue())

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all State")
            self.assertIn(st, f.getvalue())

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all Place")
            self.assertIn(pl, f.getvalue())

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all City")
            self.assertIn(ct, f.getvalue())

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all Review")
            self.assertIn(rv, f.getvalue())

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all Amenity")
            self.assertIn(am, f.getvalue())

    def test_create_command_with_kwargs(self):
        with patch("sys.stdout", new=StringIO()) as f:
            call = ('create Place city_id="0001" name="My_house" number_rooms=4 latitude=37.77 longitude=43.434')
            self.HBNB.onecmd(call)
            pl = f.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all Place")
            output = f.getvalue()
            self.assertIn(pl, output)
            self.assertIn("'city_id': '0001'", output)
            self.assertIn("'name': 'My house'", output)
            self.assertIn("'number_rooms': 4", output)
            self.assertIn("'latitude': 37.77", output)
            self.assertIn("'longitude': 43.434", output)


if __name__ == "__main__":
    unittest.main()