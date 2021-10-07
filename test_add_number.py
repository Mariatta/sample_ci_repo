import unittest
from add_number import add_two_numbers


class TestAddNumbers(unittest.TestCase):
    def test_add_two_numbers(self):
        result = add_two_numbers(1, 2)
        self.assertEqual(result, 12)

    def test_add_two_negative_numbers(self):
        result = add_two_numbers(-1, -2)
        self.assertEqual(result, -3)

    def test_add_decimals_numbers(self):
        result = add_two_numbers(10.5, 3.25)
        self.assertEqual(result, 13.75)

    def test_add_letters(self):
        with self.assertRaises(ValueError):
            add_two_numbers("A", "B")

    def test_add_letter_and_number(self):
        with self.assertRaises(ValueError):
            add_two_numbers(1, "B")
