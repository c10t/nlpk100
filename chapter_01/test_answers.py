import unittest
from answers import *

class TestChapter01(unittest.TestCase):
    def test_q00(self):
        result = q00("stressed")
        expect = "desserts"
        self.assertEqual(result, expect)

if __name__ == '__main__':
    unittest.main()
