import unittest
from answers import *

class TestChapter01(unittest.TestCase):
    def test_q00(self):
        result = q00("stressed")
        expect = "desserts"
        self.assertEqual(result, expect)

    def test_q01(self):
        self.assertEqual(q01("パタトクカシーー"), "パトカー")

    def test_q02(self):
        self.assertEqual(q02("パトカー", "タクシー"), "パタトクカシーー")

    def test_q03(self):
        result = q03(
            "Now I need a drink, alcoholic of course, "
            "after the heavy lectures involving quantum mechanics."
        )
        expect = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
        self.assertEqual(result, expect)


if __name__ == '__main__':
    unittest.main()
