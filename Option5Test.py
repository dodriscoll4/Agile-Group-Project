import unittest
from unittest.mock import patch
from io import StringIO
from Cl_Code_Base import displaying_race_times_one_competitor


class Option5Test(unittest.TestCase):

    def test_displaying_race_times_one_competitor(self):
        races_location = ['Location1', 'Location2']
        runner = 'Runner Name'
        id = 'ID1'

        # Mocking the race time and finishing positions
        with patch('Cl_Code_Base.reading_race_results_of_relevant_runner',
                   side_effect=[1900, 2000]) as mock_race_results:  # (time in seconds)
            with patch('Cl_Code_Base.sorting_where_runner_came_in_race',
                       side_effect=[(5, 10), (3, 8)]) as mock_race_finishing_positions:  # (finished position, total runners)
                with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                    displaying_race_times_one_competitor(races_location, runner, id)

        expected_output_lines = [
            f"Runner Name (ID1)",
            "-" * 35,
            f"Location1 [31] mins [40] secs (5 of 10)",
            f"Location2 [33] mins [20] secs (3 of 8)"
        ]

        actual_output_lines = mock_stdout.getvalue().strip().split('\n')

        # Assert that the output matches the expected output line by line
        for expected_line, actual_line in zip(expected_output_lines, actual_output_lines):
            self.assertEqual(actual_line.strip(), expected_line.strip())


if __name__ == '__main__':
    unittest.main()
