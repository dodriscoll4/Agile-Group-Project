import unittest
from unittest.mock import patch
from io import StringIO
from Cl_Code_Base import displaying_runners_who_have_not_gotten_podium


class Option7Test(unittest.TestCase):
    
    def test_displaying_runners_who_have_not_gotten_podium(self):
        races_location = ["Kinsale", "Blarney", "Newmarket", "Youghal", "Castletownbere"]
        runners_name = ["Runner1", "Runner2", "Runner3", "Runner4", "Runner5"]
        runners_id = ["ID1", "ID2", "ID3", "ID4", "ID5"]
        expected_output = """Competitors who have not achieved a podium position in any race:
=================================================================
Runner1 (ID1)
Runner2 (ID2)
Runner3 (ID3)
Runner4 (ID4)
Runner5 (ID5)"""

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            displaying_runners_who_have_not_gotten_podium(races_location, runners_name, runners_id)

        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)


if __name__ == '__main__':
    unittest.main()
