from unittest import TestCase
from player_turn import move
import pygame


pygame.mixer.pre_init(frequency=44100, size=-16, channels=4, buffer=512)
pygame.mixer.init()
pygame.mixer.set_num_channels(4)


class Test(TestCase):
    def test_move_north(self):
        example_character = {'X-coordinate': 0, 'Y-coordinate': 0}
        north = 'n'
        expected = {'X-coordinate': 0, 'Y-coordinate': 1}
        actual = move(example_character, north)
        self.assertEqual(expected, actual)

    def test_move_east(self):
        example_character = {'X-coordinate': 0, 'Y-coordinate': 0}
        east = 'e'
        expected = {'X-coordinate': 1, 'Y-coordinate': 0}
        actual = move(example_character, east)
        self.assertEqual(expected, actual)

    def test_move_south(self):
        example_character = {'X-coordinate': 0, 'Y-coordinate': 0}
        south = 's'
        expected = {'X-coordinate': 0, 'Y-coordinate': -1}
        actual = move(example_character, south)
        self.assertEqual(expected, actual)

    def test_move_west(self):
        example_character = {'X-coordinate': 0, 'Y-coordinate': 0}
        west = 'w'
        expected = {'X-coordinate': -1, 'Y-coordinate': 0}
        actual = move(example_character, west)
        self.assertEqual(expected, actual)