from unittest import TestCase
from unittest.mock import patch
from logic import roll


class Test(TestCase):
    @patch('random.randint', return_value=6)
    def test_roll_success(self, _):
        expected = True
        actual = roll(0, 3)
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=1)
    def test_roll_failure(self, _):
        expected = False
        actual = roll(0, 3)
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=3)
    def test_roll_bound(self, _):
        expected = True
        actual = roll(0, 3)
        self.assertEqual(expected, actual)