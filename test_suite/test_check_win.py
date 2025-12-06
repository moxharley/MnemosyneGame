from unittest import TestCase
from logic import check_win


class Test(TestCase):
    def test_win(self):
        example_character = {'X-coordinate': 0, 'Y-coordinate': 0}
        example_board = {'goal': (0, 0)}
        expected = True
        actual = check_win(example_board, example_character)
        self.assertEqual(expected, actual)

    def test_x_and_y_incorrect(self):
        example_character = {'X-coordinate': 1, 'Y-coordinate': 1}
        example_board = {'goal': (0, 0)}
        expected = False
        actual = check_win(example_board, example_character)
        self.assertEqual(expected, actual)

    def test_x_incorrect(self):
        example_character = {'X-coordinate': 1, 'Y-coordinate': 0}
        example_board = {'goal': (0, 0)}
        expected = False
        actual = check_win(example_board, example_character)
        self.assertEqual(expected, actual)

    def test_y_incorrect(self):
        example_character = {'X-coordinate': 0, 'Y-coordinate': 1}
        example_board = {'goal': (0, 0)}
        expected = False
        actual = check_win(example_board, example_character)
        self.assertEqual(expected, actual)
