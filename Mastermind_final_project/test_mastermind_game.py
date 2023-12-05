import unittest
from unittest.mock import patch
from mastermind_game import count_bulls_and_cows
from BullsAndCows import BullsAndCows
from log_error import log_error


class TestMastermindGame(unittest.TestCase):
    """
    Class TestMastermindGame inherit from unittest.Testcase
    Attributes: none
    Methods: test_count_bulls, test_count_cows, test_count_bulls_and_cows
    """

    # use unittest.mock to mock the creation of the graphical bulls and cows
    @patch('mastermind_game.BullsAndCows.create_total_bulls_and_cows')
    def test_count_bulls(self, mock_turtle):
        """
        Method -- test for counting bulls
        Parameters:
            self -- the current object
            mock_turtle -- a mock object for the turtle graphics library
        """
        secret_guess = ["blue", "green", "yellow", "purple"]
        user_guess = ["blue", "red", "yellow", "black"]

        checker = BullsAndCows(10, 4)
        count_bulls_and_cows(checker, user_guess, secret_guess, 0)

        try:
            self.assertEqual(checker.bulls_count, 2)
        except AssertionError as e:
            log_error(f"Assertion failed: {e}")

    @patch('mastermind_game.BullsAndCows.create_total_bulls_and_cows')
    def test_count_cows(self, mock_turtle):
        """
        Method -- test for counting cows
        Parameters:
            self -- the current object
            mock_turtle -- a mock object for the turtle graphics library
        """
        secret_guess = ["blue", "green", "yellow", "purple"]
        user_guess = ["red", "blue", "purple", "black"]

        checker = BullsAndCows(10, 4)
        count_bulls_and_cows(checker, user_guess, secret_guess, 0)

        try:
            self.assertEqual(checker.cows_count, 2)
        except AssertionError as e:
            log_error(f"Assertion failed: {e}")

    @patch('mastermind_game.BullsAndCows.create_total_bulls_and_cows')
    def test_count_bulls_and_cows(self, mock_turtle):
        """
        Method -- test for counting bulls and cows
        Parameters:
            self -- the current object
            mock_turtle -- a mock object for the turtle graphics library
        """
        secret_guess = ["blue", "green", "yellow", "purple"]
        user_guess = ["blue", "purple", "yellow", "green"]

        checker = BullsAndCows(10, 4)
        count_bulls_and_cows(checker, user_guess, secret_guess, 0)

        try:
            self.assertEqual(checker.bulls_count, 2)
            self.assertEqual(checker.cows_count, 2)
        except AssertionError as e:
            log_error(f"Assertion failed: {e}")


def main():
    unittest.main(verbosity=3)


if __name__ == "__main__":
    main()
