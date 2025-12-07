from unittest import TestCase
from player_turn import make_bar


class Test(TestCase):
    def test_make_full_bar(self):
        expected = '[\033[32m██████████\033[0m]'
        actual = make_bar(10)
        self.assertEqual(expected, actual)

    def test_make_half_bar(self):
        expected = '[\033[33m█████░░░░░\033[0m]'
        actual = make_bar(5)
        self.assertEqual(expected, actual)

    def test_make_low_bar(self):
        expected = '[\033[31m█░░░░░░░░░\033[0m]'
        actual = make_bar(1)
        self.assertEqual(expected, actual)

    def test_make_empty_bar(self):
        expected = '[\033[31m░░░░░░░░░░\033[0m]'
        actual = make_bar(0)
        self.assertEqual(expected, actual)