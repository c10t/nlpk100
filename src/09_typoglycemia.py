#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def typoglycemia(phrase, seed=0):
    random.seed(seed)
    result = list()
    for word in phrase.split():
        if len(word) < 5:
            result.append(word)
        else:
            randompart = list(word[1:-1])
            random.shuffle(randompart)
            result.append(word[0] + "".join(randompart) + word[-1])

    return " ".join(result)


def main():
    print(typoglycemia("Test helloworld"))
    print(typoglycemia("I couldn't believe that I could actually understand what I was reading : \
    the phenomenal power of the human mind ."))

if __name__ == '__main__':
    main()
