import unittest
from pythaiid import get_last_digit


class TestGetLastDigit(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(get_last_digit(0), 1)
        self.assertEqual(get_last_digit(2), 9)
        self.assertEqual(get_last_digit(3), 8)
        self.assertEqual(get_last_digit(5), 6)
        self.assertEqual(get_last_digit(7), 4)
        self.assertEqual(get_last_digit(11), 1)
        self.assertEqual(get_last_digit(13), 9)
        self.assertEqual(get_last_digit(17), 5)
        self.assertEqual(get_last_digit(19), 3)
        self.assertEqual(get_last_digit(23), 0)
        self.assertEqual(get_last_digit(29), 4)
        self.assertEqual(get_last_digit(31), 2)
        self.assertEqual(get_last_digit(37), 7)
        self.assertEqual(get_last_digit(41), 3)
        self.assertEqual(get_last_digit(43), 1)
        self.assertEqual(get_last_digit(47), 8)
        self.assertEqual(get_last_digit(53), 2)
        self.assertEqual(get_last_digit(59), 7)
        self.assertEqual(get_last_digit(61), 5)
        self.assertEqual(get_last_digit(67), 0)
        self.assertEqual(get_last_digit(71), 6)
        self.assertEqual(get_last_digit(73), 4)
        self.assertEqual(get_last_digit(79), 9)
        self.assertEqual(get_last_digit(83), 5)
        self.assertEqual(get_last_digit(89), 0)
        self.assertEqual(get_last_digit(97), 2)
        self.assertEqual(get_last_digit(100), 0)
