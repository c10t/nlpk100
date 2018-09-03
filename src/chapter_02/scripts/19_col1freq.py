#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter

def main():
    file_path = '../resource/hightemp.txt'

    with open(file_path, encoding='utf-8') as f:
        c = Counter()
        for line in f.readlines():
            c[line.split()[0]] += 1

        for key, value in c.most_common():
            print(f"{key}: {value}")

if __name__ == '__main__':
    main()
