#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def main():
    last_n = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    file_path = '../resource/hightemp.txt'

    with open(file_path, encoding='utf-8') as f:
        last = f.readlines()[-last_n:]
        for line in last:
            print(line.rstrip())

if __name__ == '__main__':
    main()
