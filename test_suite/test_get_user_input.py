from unittest import TestCase
from unittest.mock import patch
from logic import get_user_input
import pygame


pygame.mixer.pre_init(frequency=44100, size=-16, channels=4, buffer=512)
pygame.mixer.init()
pygame.mixer.set_num_channels(4)


class Test(TestCase):
    @patch('builtins.input', side_effect=['n'])
    def test_n(self, _):
        expected = 'n'
        actual = get_user_input()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['e'])
    def test_e(self, _):
        expected = 'e'
        actual = get_user_input()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['s'])
    def test_s(self, _):
        expected = 's'
        actual = get_user_input()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['w'])
    def test_w(self, _):
        expected = 'w'
        actual = get_user_input()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['status'])
    def test_status(self, _):
        expected = 'status'
        actual = get_user_input()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['look'])
    def test_look(self, _):
        expected = 'look'
        actual = get_user_input()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['interact'])
    def test_interact(self, _):
        expected = 'interact'
        actual = get_user_input()
        self.assertEqual(expected, actual)