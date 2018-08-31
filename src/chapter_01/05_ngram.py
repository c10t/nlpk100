#!/usr/bin/env python
# -*- coding: utf-8 -*-


def word_bigram(text):
    target = text.split()
    return [(target[i], target[i + 1]) for i in range(len(target)) if i < len(target) - 1]


def char_bigram(word):
    return [(word[i], word[i + 1]) for i in range(len(word)) if i < len(word) - 1]


def main():
    print(word_bigram("I am an NLPer"))
    print(char_bigram("I am an NLPer"))


if __name__ == '__main__':
    main()
