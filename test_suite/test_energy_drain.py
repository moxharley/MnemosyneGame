from unittest import TestCase
from logic import energy_drain
from unittest.mock import patch
import pygame


class Test(TestCase):
    @patch('random.random', return_value=1)
    def test_no_drain(self, _):
        example_character = {'current-EP': 10}
        expected = {'current-EP': 10}
        actual = energy_drain(example_character)
        self.assertEqual(expected, actual)

    @patch('random.random', return_value=0)
    def test_drain(self, _):
        pygame.mixer.pre_init(frequency=44100, size=-16, channels=4, buffer=512)
        pygame.mixer.init()
        pygame.mixer.set_num_channels(4)
        example_character = {'current-EP': 10}
        expected = {'current-EP': 9}
        actual = energy_drain(example_character)
        self.assertEqual(expected, actual)

    @patch('random.random', return_value=0.20)
    def test_bound(self, _):
        example_character = {'current-EP': 10}
        expected = {'current-EP': 10}
        actual = energy_drain(example_character)
        self.assertEqual(expected, actual)
