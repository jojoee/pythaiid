import unittest
from pythaiid import random, verify


class TestRandom(unittest.TestCase):

    def test_normal(self):
        for i in range(0, 2000):
            id = random()
            self.assertEqual(verify(id), True)
