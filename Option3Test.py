import unittest
from unittest.mock import patch
from io import StringIO
from Cl_Code_Base import competitors_by_county


class Option3Test(unittest.TestCase):

    def test_competitors_by_county(self):
        runners_name = ["Anna Fox", "Des Kelly", "Ann Cahill", "Joe Flynn", "Sally Fox", "Joe Shine", "Lisa Collins", "Sil Murphy", "Des Kelly"]
        runners_id = ["CK-24", "CK-23", "KY-43", "CK-11", "KY-12", "TP-02", "WD-32", "LK-73", "WD-19"]

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            competitors_by_county(runners_name, runners_id)

        expected_output = """Cork runners
====================
Anna Fox (CK-24)
Des Kelly (CK-23)
Joe Flynn (CK-11)

Kerry runners
====================
Ann Cahill (KY-43)
Sally Fox (KY-12)

Limerick runners
====================
Sil Murphy (LK-73)

Tipperary runners
====================
Joe Shine (TP-02)

Waterford runners
====================
Des Kelly (WD-19)
Lisa Collins (WD-32)"""

        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)


if __name__ == '__main__':
    unittest.main()
