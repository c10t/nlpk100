#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    file_path = '../resource/hightemp.txt'

    with open(file_path, encoding='utf-8') as f:
        temp = f.readlines()
        for line in sorted(temp, key=lambda x: x.split()[2], reverse=True):
            print(line.rstrip())

if __name__ == '__main__':
    main()
