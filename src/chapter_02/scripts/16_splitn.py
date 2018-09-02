#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import math

def split_list(list_, n):
    q = math.ceil(len(list_) / n)
    return [list_[i * q : (i + 1) * q] for i in range(n)]


def main():
    n_split = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    file_path = '../resource/hightemp.txt'

    with open(file_path, encoding='utf-8') as f:
        temp = f.readlines()
        for i, sub_list in enumerate(split_list(temp, n_split)):
            print(f"---------- split {i+1} / {n_split} ----------")
            for line in sub_list:
                print(line.rstrip())

if __name__ == '__main__':
    main()
