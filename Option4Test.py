import unittest
from unittest.mock import patch
from io import StringIO
from Cl_Code_Base import displaying_winners_of_each_race


class Option4Test(unittest.TestCase):

    def test_displaying_winners_of_each_race(self):
        races_location = ['Kinsale', 'Blarney', 'Newmarket', 'Youghal', 'Castletownbere']

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            displaying_winners_of_each_race(races_location)

        expected_output = """Race                  1st Place    2nd Place    3rd Place
=========================================================
Kinsale               LK-73        WD-32        TP-02
Blarney               KY-43        WD-19        WD-32
Newmarket             WD-32        WD-19        TP-02
Youghal               TP-02        WD-19        WD-32
Castletownbere        KY-12        WD-32        TP-02"""

        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)


if __name__ == '__main__':
    unittest.main()


