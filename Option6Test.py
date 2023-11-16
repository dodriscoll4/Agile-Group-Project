import unittest
from unittest.mock import patch
from io import StringIO
from Cl_Code_Base import displaying_runners_who_have_won_at_least_one_race, reading_race_results


class Option6Test(unittest.TestCase):

    def test_displaying_runners_who_have_won_at_least_one_race(self):
        races_location = ["Kinsale", "Blarney", "Newmarket", "Youghal", "Castletownbere"]
        runners_name = ["Runner1", "Runner2", "Runner3", "Runner4", "Runner5"]
        runners_id = ["ID1", "ID2", "ID3", "ID4", "ID5"]

        # Mocking the race results for the races
        with patch('Cl_Code_Base.reading_race_results',
                   return_value=(['ID1', 'ID2', 'ID3', 'ID4', 'ID5'], [10, 14, 12, 11, 11])) as mock_race_results:
            with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
                displaying_runners_who_have_won_at_least_one_race(races_location, runners_name, runners_id)

        expected_output_lines = [
            "The following runners have all won at least one race:",
            "-" * 55,
            "Runner1 (ID1)",
            "Runner2 (ID2)",
            "Runner3 (ID3)",
            "Runner4 (ID4)",
            "Runner5 (ID5)"
        ]

        actual_output_lines = mock_stdout.getvalue().strip().split("\n")

        for expected_line, actual_line in zip(expected_output_lines, actual_output_lines):
            self.assertEqual(actual_line.strip(), expected_line.strip())


if __name__ == '__main__':
    unittest.main()
