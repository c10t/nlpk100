#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    file_path = '../resource/hightemp.txt'

    with open(file_path, encoding='utf-8') as f:
        temp = f.readlines()
        print({line.split()[0] for line in temp})

if __name__ == '__main__':
    main()
