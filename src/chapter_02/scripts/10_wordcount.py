#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    file_path = '../resource/hightemp.txt'
    with open(file_path, encoding='utf-8') as f:
        text = f.readlines()
        print(len(text))

if __name__ == '__main__':
    main()
