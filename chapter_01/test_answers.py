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

    def test_q04(self):
        result = q04(
            "Hi He Lied Because Boron Could Not Oxidize Fluorine. "
            "New Nations Might Also Sign Peace Security Clause. "
            "Arthur King Can."
        )

        expect = {
            "H": 1, "He": 2, "Li": 3, "Be": 4, "B": 5, "C": 6,
            "N": 7, "O": 8, "F": 9, "Ne": 10, "Na": 11, "Mi": 12,
            "Al": 13, "Si": 14, "P": 15, "S": 16, "Cl": 17,
            "Ar": 18, "K": 19, "Ca": 20
        }

        for (k, v) in expect.items():
            self.assertTrue((k, v) in result.items(), f"{k}:{v} is not found")

    def test_q05(self):
        result_word_bigram = q05("I am an NLPer", True)
        expect_word_bigram = [("I", "am"), ("am", "an"), ("an", "NLPer")]
        self.assertEqual(result_word_bigram, expect_word_bigram)

        result_char_bigram = q05("I am an NLPer")
        expect_char_bigram = [
            ('I', ' '), (' ', 'a'), ('a', 'm'), ('m', ' '), (' ', 'a'),
            ('a', 'n'), ('n', ' '), (' ', 'N'), ('N', 'L'), ('L', 'P'),
            ('P', 'e'), ('e', 'r')
        ]
        self.assertEqual(result_char_bigram, expect_char_bigram)


if __name__ == '__main__':
    unittest.main()
