import unittest
import os
from unittest import mock
from unittest.mock import patch
from io import StringIO


from peopledatalabs.helper import helper


class TestHelper(unittest.TestCase):

    def test_print_menu(self):

        with patch('sys.stdout', new = StringIO()) as fake_out:
            myhelper = helper()
            myhelper.print_menu()

            self.assertIn('Phone number', fake_out.getvalue())
            self.assertIn('Email', fake_out.getvalue())
            self.assertIn('Exit', fake_out.getvalue())


if __name__ == '__main__':
    unittest.main()
