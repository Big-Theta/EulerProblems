import unittest
from pan_fib import *

class TestPanFib(unittest.TestCase):
    def test_is_pandigital(self):
        val1 = "1234567890"
        self.assertFalse(is_pandigital(val1))
        val2 = "123456789"
        self.assertTrue(is_pandigital(val2))
        val3 = "567894321"
        self.assertTrue(is_pandigital(val3))

    def test_first_pandigital(self):
        self.assertEqual(2749, find_first_pandigital())
        self.assertTrue(first_is_pandigital(5678943219999))
        self.assertTrue(first_is_pandigital(5679438219999))

    def test_last_pandigital(self):
        self.assertEqual(541, find_last_pandigital())
        self.assertTrue(last_is_pandigital(8888567894321))
        self.assertTrue(last_is_pandigital(9999567943821))

