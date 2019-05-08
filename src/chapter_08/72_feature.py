#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nltk
from pathlib import Path
from nltk.corpus import stopwords
# from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer

RESOURCE_PATH = './resources/sentiment.txt'


def extract_feature(docs):
    sw = set(stopwords.words('english'))
    # ps = PorterStemmer()
    wl = WordNetLemmatizer()

    def feature(doc):
        words = doc.split()
        words = [wl.lemmatize(w) for w in words]  # ps.stem(w)
        words = [w for w in words if w not in sw]
        return words

    extracted = [' '.join(feature(doc)) for doc in docs]
    return extracted


def main():
    data = Path(RESOURCE_PATH)
    reviews = []

    with data.open() as f:
        for line in f:
            reviews.append(line.strip())

    extracted = extract_feature(reviews)

    extracted_txt = './resources/feature-extracted.txt'
    with open(extracted_txt, mode='w', encoding='utf-8') as f:
        f.write('\n'.join(extracted))


if __name__ == '__main__':
    data = ['wordnet', 'stopwords']
    for d in data:
        try:
            nltk.data.find(d)
        except LookupError:
            nltk.download(d)
    main()
