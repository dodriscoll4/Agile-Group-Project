import unittest
from unittest.mock import patch, mock_open
from io import StringIO
from Cl_Code_Base import main


class TestQuitOption(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['8'])
    @patch('builtins.open', new_callable=mock_open())
    def test_quit_option(self, mock_open, mock_input, mock_stdout):
        main()
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '')


if __name__ == '__main__':
    unittest.main()
