import unittest
from unittest.mock import patch
from io import StringIO
from Cl_Code_Base import race_results, race_venues, winner_of_race, podium_position, display_races


class Option1Test(unittest.TestCase):

    def test_race_options(self):
        races_location = ["Kinsale", "Blarney", "Newmarket", "Youghal", "Castletownbere"]
        with patch("builtins.input", side_effect=["1"]):
            with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
                race_results(races_location)

        expected_output = """1: Kinsale
2: Blarney
3: Newmarket
4: Youghal
5: Castletownbere"""
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_race_venues(self):
        with patch("builtins.open", create=True) as mock_open:
            mock_open.return_value.__enter__.return_value.readlines.return_value = ["Kinsale, 30", "Blarney, 32"]
            venues = race_venues()

        self.assertEqual(venues, ["Kinsale", "Blarney"])

    def test_winner_of_race(self):
        id = ["runner1", "runner2", "runner3"]
        time_taken = [30, 32, 28]
        winner = winner_of_race(id, time_taken)

        self.assertEqual(winner, "runner3")

    def test_podium_position(self):
        id = ["runner1", "runner2", "runner3"]
        time_taken = [30, 32, 28]
        podium = podium_position(id, time_taken)

        self.assertEqual(podium, ("runner3", "runner1", "runner2"))

    def test_display_results(self):
        id = ["runner1", "runner2", "runner3"]
        time_taken = [30, 32, 28]
        venue = "Kinsale"
        fastest_runner = "runner3"
        podium_places = ("runner3", "runner1", "runner2")

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            display_races(id, time_taken, venue, fastest_runner, podium_places)

        expected_output = """Results for Kinsale
=====================================
runner1    0 minutes and 30 seconds
runner2    0 minutes and 32 seconds
runner3    0 minutes and 28 seconds

runner3 won the race.

1st Place: runner3
2nd Place: runner1
3rd Place: runner2"""
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)


if __name__ == '__main__':
    unittest.main()
