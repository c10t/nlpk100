#!/usr/bin/env python
# -*- coding: utf-8 -*-


def char_bigram_as_set(word):
    return {(word[i], word[i + 1]) for i in range(len(word)) if i < len(word) - 1}


def main():
    x = char_bigram_as_set("paraparaparadise")
    y = char_bigram_as_set("paragraph")
    print("X := {}".format(x))
    print("Y := {}".format(y))
    print("X | Y = {}".format(x | y))
    print("X & Y = {}".format(x & y))
    print("X - Y = {}".format(x ^ y))
    print("Is 'se' in X? - {}".format(("s", "e") in x))
    print("Is 'se' in Y? - {}".format(("s", "e") in y))


if __name__ == '__main__':
    main()
