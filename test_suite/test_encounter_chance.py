from unittest import TestCase
from unittest.mock import patch
from room import encounter_chance
import pygame


pygame.mixer.pre_init(frequency=44100, size=-16, channels=4, buffer=512)
pygame.mixer.init()
pygame.mixer.set_num_channels(4)


class Test(TestCase):
    @patch('random.random', return_value=0)
    @patch('logic.roll', return_value=6)
    @patch('builtins.input', side_effect=['1'])
    def test_encounter_intuit_success(self, _, __, ___):
        example_character = {'current-HP': 5, 'current-EP': 5, 'int': 0, 'eng': 0, 'end': 0, 'inf': 0, 'inventory': ['Empty', 'Empty', 'Empty', 'Empty'], 'first-name': 'Test'}
        example_passed = [False, False]
        expected = {'current-HP': 5, 'current-EP': 5, 'int': 0, 'eng': 0, 'end': 0, 'inf': 0, 'inventory': ['Empty', 'Empty', 'Empty', 'Empty'], 'first-name': 'Test'}
        actual = encounter_chance(example_character, example_passed)
        self.assertEqual(expected, actual)

    @patch('random.random', return_value=0)
    @patch('logic.roll', return_value=6)
    @patch('builtins.input', side_effect=['2'])
    def test_encounter_engage_success(self, _, __, ___):
        example_character = {'current-HP': 5, 'current-EP': 5, 'int': 0, 'eng': 0, 'end': 0, 'inf': 0, 'inventory': ['Empty', 'Empty', 'Empty', 'Empty'], 'first-name': 'Test'}
        example_passed = [False, False]
        expected = {'current-HP': 5, 'current-EP': 5, 'int': 0, 'eng': 0, 'end': 0, 'inf': 0, 'inventory': ['Empty', 'Empty', 'Empty', 'Empty'], 'first-name': 'Test'}
        actual = encounter_chance(example_character, example_passed)
        self.assertEqual(expected, actual)

    @patch('random.random', return_value=0)
    @patch('logic.roll', return_value=6)
    @patch('builtins.input', side_effect=['3'])
    def test_encounter_engage_success(self, _, __, ___):
        example_character = {'current-HP': 5, 'current-EP': 5, 'int': 0, 'eng': 0, 'end': 0, 'inf': 0, 'inventory': ['Data-Knife', 'Empty', 'Empty', 'Empty'], 'first-name': 'Test'}
        example_passed = [False, False]
        expected = {'current-HP': 5, 'current-EP': 5, 'int': 0, 'eng': 0, 'end': 0, 'inf': 0, 'inventory': ['Data-Knife', 'Empty', 'Empty', 'Empty'], 'first-name': 'Test'}
        actual = encounter_chance(example_character, example_passed)
        self.assertEqual(expected, actual)

    @patch('random.random', return_value=0)
    @patch('logic.roll', side_effect=[0, 6])
    @patch('builtins.input', side_effect=['1', '1'])
    def test_encounter_any_choice_failure_then_success(self, _, __, ___):
        example_character = {'current-HP': 10, 'exp': 0, 'current-EP': 10, 'int': 0, 'eng': 0, 'end': 0, 'inf': 0, 'inventory': ['Empty', 'Empty', 'Empty', 'Empty'], 'first-name': 'Test'}
        example_passed = [False, False]
        expected = {'current-HP': 5, 'current-EP': 10, 'exp': 1, 'int': 0, 'eng': 0, 'end': 0, 'inf': 0, 'inventory': ['Empty', 'Empty', 'Empty', 'Empty'], 'first-name': 'Test'}
        actual = encounter_chance(example_character, example_passed)
        self.assertEqual(expected, actual)

    @patch('random.random', return_value=0)
    @patch('logic.roll', side_effect=[0, 0])
    @patch('builtins.input', side_effect=['1', '1'])
    def test_encounter_any_choice_failure_then_failure(self, _, __, ___):
        example_character = {'current-HP': 10, 'current-EP': 10, 'int': 0, 'eng': 0, 'end': 0, 'inf': 0, 'inventory': ['Empty', 'Empty', 'Empty', 'Empty'], 'first-name': 'Test'}
        example_passed = [False, False]
        expected = {'current-HP': 0, 'current-EP': 10, 'int': 0, 'eng': 0, 'end': 0, 'inf': 0, 'inventory': ['Empty', 'Empty', 'Empty', 'Empty'], 'first-name': 'Test'}
        actual = encounter_chance(example_character, example_passed)
        self.assertEqual(expected, actual)


