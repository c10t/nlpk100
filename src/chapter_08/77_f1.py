#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

RESOURCE = './resources/q75.txt'


def main():
    with Path(RESOURCE).open(encoding='utf-8') as f:
        tp, fp, tn, fn = 0, 0, 0, 0
        for line in f:
            predict, answer, _ = line.strip().split('\t')
            if predict == '+1' and predict == answer:
                tp += 1
            if predict == '+1' and predict != answer:
                fp += 1
            if predict == '-1' and predict == answer:
                tn += 1
            if predict == '-1' and predict != answer:
                fn += 1

        precision = tp / (tp + fp)
        recall = tp / (tp + fn)
        print('accuracy:', (tp + tn) / (tp + fp + fn + tn))
        print('precision:', precision)
        print('recall:', recall)
        print('f1:', 2 * recall * precision / (recall + precision))


if __name__ == '__main__':
    main()
