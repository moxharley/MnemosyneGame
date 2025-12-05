from unittest import TestCase
from logic import check_alive


class Test(TestCase):
    def test_is_alive(self):
        example_character = {'current-HP': 10, 'current-EP': 10}
        example_hull = 90
        expected = True
        actual = check_alive(example_character, example_hull)
        self.assertEqual(expected, actual)

    def test_no_hp(self):
        example_character = {'current-HP': 0, 'current-EP': 10}
        example_hull = 90
        expected = False
        actual = check_alive(example_character, example_hull)
        self.assertEqual(expected, actual)

    def test_no_ep(self):
        example_character = {'current-HP': 10, 'current-EP': 0}
        example_hull = 90
        expected = False
        actual = check_alive(example_character, example_hull)
        self.assertEqual(expected, actual)

    def test_no_hull(self):
        example_character = {'current-HP': 10, 'current-EP': 10}
        example_hull = 0
        expected = False
        actual = check_alive(example_character, example_hull)
        self.assertEqual(expected, actual)

