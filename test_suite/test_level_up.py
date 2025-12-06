from unittest import TestCase
from unittest.mock import patch
from logic import level_up
import pygame


pygame.mixer.pre_init(frequency=44100, size=-16, channels=4, buffer=512)
pygame.mixer.init()
pygame.mixer.set_num_channels(4)


class Test(TestCase):
    def test_one_exp(self):
        example_character = {'exp': 0}
        expected = {'exp': 1}
        actual = level_up(example_character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['1'])
    def test_level_up_endure(self, _):
        example_character = {'exp': 2, 'end': 0}
        expected = {'exp': 0, 'end': 1}
        actual = level_up(example_character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['2'])
    def test_level_up_engage(self, _):
        example_character = {'exp': 2, 'eng': 0}
        expected = {'exp': 0, 'eng': 1}
        actual = level_up(example_character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['3'])
    def test_level_up_interface(self, _):
        example_character = {'exp': 2, 'inf': 0}
        expected = {'exp': 0, 'inf': 1}
        actual = level_up(example_character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['4'])
    def test_level_up_intuit(self, _):
        example_character = {'exp': 2, 'int': 0}
        expected = {'exp': 0, 'int': 1}
        actual = level_up(example_character)
        self.assertEqual(expected, actual)
