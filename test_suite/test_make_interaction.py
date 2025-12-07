from unittest import TestCase
from room import make_interaction
from unittest.mock import patch
import pygame


pygame.mixer.pre_init(frequency=44100, size=-16, channels=4, buffer=512)
pygame.mixer.init()
pygame.mixer.set_num_channels(4)


class Test(TestCase):
    @patch('random.random', return_value=0)
    @patch('logic.roll', return_value=6)
    @patch('builtins.input', side_effect=['1'])
    def test_interface_success(self, _, __, ___):
        example_interactions = make_interaction()
        example_character = {'current-HP': 5, 'current-EP': 5, 'inf': 0}
        expected = {'current-HP': 5, 'current-EP': 6, 'inf': 0}
        actual = example_interactions[(2, 0)](example_character)
        self.assertEqual(expected, actual)

    @patch('random.random', return_value=0)
    @patch('logic.roll', return_value=0)
    @patch('builtins.input', side_effect=['1'])
    def test_interface_failure(self, _, __, ___):
        example_interactions = make_interaction()
        example_character = {'current-HP': 5, 'current-EP': 5, 'inf': 0}
        expected = {'current-HP': 5, 'current-EP': 4, 'inf': 0}
        actual = example_interactions[(2, 0)](example_character)
        self.assertEqual(expected, actual)

    @patch('random.random', return_value=0.25)
    @patch('logic.roll', return_value=6)
    @patch('builtins.input', side_effect=['1'])
    def test_engage_success(self, _, __, ___):
        example_interactions = make_interaction()
        example_character = {'current-HP': 5, 'current-EP': 5, 'eng': 0}
        expected = {'current-HP': 5, 'current-EP': 6, 'eng': 0}
        actual = example_interactions[(2, 0)](example_character)
        self.assertEqual(expected, actual)

    @patch('random.random', return_value=0.25)
    @patch('logic.roll', return_value=0)
    @patch('builtins.input', side_effect=['1'])
    def test_engage_failure(self, _, __, ___):
        example_interactions = make_interaction()
        example_character = {'current-HP': 5, 'current-EP': 5, 'eng': 0}
        expected = {'current-HP': 4, 'current-EP': 5, 'eng': 0}
        actual = example_interactions[(2, 0)](example_character)
        self.assertEqual(expected, actual)

    @patch('random.random', return_value=0.5)
    @patch('logic.roll', return_value=6)
    @patch('builtins.input', side_effect=['1'])
    def test_endure_success(self, _, __, ___):
        example_interactions = make_interaction()
        example_character = {'current-HP': 5, 'current-EP': 5, 'end': 0}
        expected = {'current-HP': 6, 'current-EP': 5, 'end': 0}
        actual = example_interactions[(2, 0)](example_character)
        self.assertEqual(expected, actual)

    @patch('random.random', return_value=0.5)
    @patch('logic.roll', return_value=0)
    @patch('builtins.input', side_effect=['1'])
    def test_endure_failure(self, _, __, ___):
        example_interactions = make_interaction()
        example_character = {'current-HP': 5, 'current-EP': 5, 'end': 0}
        expected = {'current-HP': 4, 'current-EP': 5, 'end': 0}
        actual = example_interactions[(2, 0)](example_character)
        self.assertEqual(expected, actual)

    @patch('random.random', return_value=0.75)
    @patch('logic.roll', return_value=6)
    @patch('builtins.input', side_effect=['1'])
    def test_intuit_success(self, _, __, ___):
        example_interactions = make_interaction()
        example_character = {'current-HP': 5, 'current-EP': 5, 'int': 0}
        expected = {'current-HP': 6, 'current-EP': 5, 'int': 0}
        actual = example_interactions[(2, 0)](example_character)
        self.assertEqual(expected, actual)

    @patch('random.random', return_value=0.75)
    @patch('logic.roll', return_value=0)
    @patch('builtins.input', side_effect=['1'])
    def test_intuit_failure(self, _, __, ___):
        example_interactions = make_interaction()
        example_character = {'current-HP': 5, 'current-EP': 5, 'int': 0}
        expected = {'current-HP': 5, 'current-EP': 4, 'int': 0}
        actual = example_interactions[(2, 0)](example_character)
        self.assertEqual(expected, actual)