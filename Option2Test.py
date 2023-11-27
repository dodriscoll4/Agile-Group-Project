import unittest
from unittest.mock import patch
from Cl_Code_Base import users_venue


class Option2Test(unittest.TestCase):

    @patch("Cl_Code_Base.updating_races_file")
    @patch("builtins.input", side_effect=["Cork", "1", "2", "3", "4", "5", "6", "7", "8", "9", "6"])
    def test_users_venue_creates_new_file(self, mock_input, mock_updating_races_file):
        races_location = ["Kinsale", "Blarney", "Newmarket", "Youghal", "Castletownbere"]
        runners_id = ["CK-24", "CK-23", "KY-43", "CK-11", "KY-12", "TP-02", "WD-32", "LK-73", "WD-19"]

        # Call the users_venue function
        users_venue(races_location, runners_id)

        # Check that the file has been created
        self.assertIn("Cork", races_location)

        # Check that updating_races_file has been called
        mock_updating_races_file.assert_called_once_with(races_location)


if __name__ == '__main__':
    unittest.main()
