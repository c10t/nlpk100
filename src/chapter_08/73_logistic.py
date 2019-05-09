#!/usr/bin/env python
# -*- coding: utf-8 -*-
from nltk.tokenize import RegexpTokenizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

DATA = './resources/feature-extracted.txt'


def preprocess(corpus):
    tk = RegexpTokenizer(r'\w+')

    x = []
    y = []
    for document in corpus:
        pol, review = document.split(' ', 1)
        x.append(' '.join(tk.tokenize(review)))
        y.append(1.0 if pol == '+1' else 0.0)

    return x, y


def process(x, y):
    model = LogisticRegression()
    vectorizer = CountVectorizer()
    x_train, x_test, y_train, y_test = train_test_split(
        vectorizer.fit_transform(x), y, test_size=0.2, random_state=0)
    model.fit(x_train, y_train)
    print('train: ', model.score(x_train, y_train))
    print('test : ', model.score(x_test, y_test))


def main():
    with open(DATA, encoding='utf-8') as f:
        corpus = [line.strip() for line in f]

    x, y = preprocess(corpus)
    process(x, y)


if __name__ == '__main__':
    main()
