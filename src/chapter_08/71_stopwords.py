#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from copy import deepcopy
from collections import Counter
from pathlib import Path


class StopWords():
    def __init__(self, texts=[], file_path='', from_file=False):
        if from_file:
            self.words = self._load(file_path)
        else:
            self.words = Counter()
            for text in texts:
                self.words += Counter(text.split())

    def clone(self):
        return deepcopy(self.words)

    def is_stopword(self, word, threshold=100):
        return self.words[word] > threshold

    def _load(self, file_path):
        data = Path(file_path)
        words = Counter()
        # no need to use readlines()
        # https://docs.python.org/3/howto/functional.html
        with data.open() as f:
            for line in f:
                words += Counter(line.strip().split())

        return words


class Test(unittest.TestCase):
    source = [
        'a movie with a real anarchic flair',
        'russian ark is a new treasure of the hermitage',
        'like a poor man\'s you can count on me'
    ]
    word_cases = [
        ('a', 3, True), ('hermitage', 3, False), ('diffeomorphism', 3, False)
    ]

    def test_is_stopwords(self):
        stopwords = StopWords(self.source)
        for word, threshold, expect in self.word_cases:
            actual = stopwords.is_stopword(word, threshold)
            self.assertEqual(actual, expect, '{}'.format(word))


if __name__ == '__main__':
    unittest.main()
