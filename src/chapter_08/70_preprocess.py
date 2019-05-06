#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import codecs

random.seed(0)


def main():
    neg = './resources/rt-polaritydata/rt-polarity.neg'
    pos = './resources/rt-polaritydata/rt-polarity.pos'
    sentiment = []
    with codecs.open(neg, mode='r', encoding='utf-8', errors='ignore') as f:
        for line in f.readlines():
            sentiment.append(f'-1 {line.strip()}')
    with codecs.open(pos, mode='r', encoding='utf-8', errors='ignore') as f:
        for line in f.readlines():
            sentiment.append(f'+1 {line.strip()}')
    sentiment = random.sample(sentiment, len(sentiment))
    sentiment_txt = './resources/sentiment.txt'
    with open(sentiment_txt, mode='w', encoding='utf-8') as f:
        f.write('\n'.join(sentiment))


if __name__ == '__main__':
    main()
