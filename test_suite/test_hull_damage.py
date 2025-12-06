from unittest import TestCase
from unittest.mock import patch
from logic import hull_damage
import pygame


pygame.mixer.pre_init(frequency=44100, size=-16, channels=4, buffer=512)
pygame.mixer.init()
pygame.mixer.set_num_channels(4)


class Test(TestCase):
    @patch('random.random', return_value=1)
    @patch('random.randint', return_value=1)
    def test_hull_damage(self, _, __):
        example_hull = 90
        expected = 90
        actual = hull_damage(example_hull)
        self.assertEqual(expected, actual)

    @patch('random.random', return_value=0)
    @patch('random.randint', return_value=1)
    def test_no_hull_damage(self, _, __):
        example_hull = 90
        expected = 89
        actual = hull_damage(example_hull)
        self.assertEqual(expected, actual)
