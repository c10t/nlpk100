#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

A_TO_Z = re.compile(r"[^a-zA-Z]")

def words_length(phrase):
    return [len(A_TO_Z.sub("", word)) for word in phrase.split()]


def main():
    print(words_length("Now I need a drink, alcoholic of course, \
    after the heavy lectures involving quantum mechanics."))


if __name__ == '__main__':
    main()
