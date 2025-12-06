from unittest import TestCase
from logic import validate_move


class Test(TestCase):
    def test_valid_move(self):
        example_board = {(0, 0): "Empty Room", (0, 1): "Empty Room"}
        example_character = {"X-coordinate": 0, "Y-coordinate": 0}
        example_movement = 'n'
        self.assertTrue(validate_move(example_board, example_character, example_movement))

    def test_invalid_move(self):
        example_board = {(0, 0): "Empty Room", (0, 1): "Empty Room"}
        example_character = {"X-coordinate": 0, "Y-coordinate": 0}
        example_movement = 'e'
        self.assertFalse(validate_move(example_board, example_character, example_movement))
