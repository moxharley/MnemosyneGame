from unittest import TestCase
from logic import update


class Test(TestCase):
    def test_increase_hp(self):
        example_key = 'current-HP'
        example_character = {'current-HP': 5, 'current-EP': 5}
        example_amount = 5
        expected = {'current-HP': 10, 'current-EP': 5}
        actual = update(example_key, example_character, example_amount)
        self.assertEqual(expected, actual)

    def test_decrease_hp(self):
        example_key = 'current-HP'
        example_character = {'current-HP': 5, 'current-EP': 5}
        example_amount = -3
        expected = {'current-HP': 2, 'current-EP': 5}
        actual = update(example_key, example_character, example_amount)
        self.assertEqual(expected, actual)

    def test_increase_ep(self):
        example_key = 'current-EP'
        example_character = {'current-HP': 5, 'current-EP': 5}
        example_amount = 5
        expected = {'current-HP': 5, 'current-EP': 10}
        actual = update(example_key, example_character, example_amount)
        self.assertEqual(expected, actual)

    def test_decrease_ep(self):
        example_key = 'current-EP'
        example_character = {'current-HP': 5, 'current-EP': 5}
        example_amount = -3
        expected = {'current-HP': 5, 'current-EP': 2}
        actual = update(example_key, example_character, example_amount)
        self.assertEqual(expected, actual)