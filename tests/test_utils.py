from src.utils.calc import add, sub, div, mul
import unittest


class TestFunc(unittest.TestCase):
    def test_utils(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(sub(1, 2), -1)
        self.assertEqual(div(1, 2), 0.5)
        self.assertEqual(mul(1, 2), 2)
