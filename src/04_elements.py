#!/usr/bin/env python
# -*- coding: utf-8 -*-

FIRST_CHAR_ONLY = (1, 5, 6, 7, 8, 9, 15, 16, 19)

def elementize(sentence):
    resultmap = dict()

    for i, word in enumerate(sentence.split()):
        if i + 1 in FIRST_CHAR_ONLY:
            resultmap[word[0:1]] = i + 1
        else:
            resultmap[word[0:2]] = i + 1

    return resultmap


def main():
    print(elementize("Hi He Lied Because Boron Could Not Oxidize Fluorine. \
    New Nations Might Also Sign Peace Security Clause. Arthur King Can."))


if __name__ == '__main__':
    main()
