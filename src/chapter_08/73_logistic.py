#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
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


def write_list(filepath, l):
    with open(filepath, mode='w', encoding='utf-8') as f:
        f.write('\n'.join(l))


def process(x, y):
    model = LogisticRegression()
    vectorizer = CountVectorizer()
    x_train, x_test, y_train, y_test = train_test_split(
        vectorizer.fit_transform(x), y, test_size=0.2, random_state=0)
    model.fit(x_train, y_train)
    print('train: ', model.score(x_train, y_train))
    print('test : ', model.score(x_test, y_test))

    # Q. 75
    features = vectorizer.get_feature_names()
    indices = np.argsort(model.coef_)[0]
    print('--- [top 10] ---')
    for idx in indices[-1:-11:-1]:
        print(features[idx])
    print('--- [bottom 10] ---')
    for idx in indices[:10]:
        print(features[idx])

    # Q. 76
    def label(p): return '+1' if p > 0.5 else '-1'
    predict_all = model.predict(vectorizer.transform(x))
    proba = model.predict_proba(vectorizer.transform(x))

    q75 = []
    for ans, prd, prb in zip(y, predict_all, proba):
        belong = prb[0] if prd == 0 else prb[1]
        q75.append(f'{label(ans)}\t{label(prd)}\t{belong}')

    # write_list('./resources/q75.txt', q75)


def main():
    with open(DATA, encoding='utf-8') as f:
        corpus = [line.strip() for line in f]

    x, y = preprocess(corpus)
    process(x, y)


if __name__ == '__main__':
    main()
