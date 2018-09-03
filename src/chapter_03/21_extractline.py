#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gzip
import json

def main():
    file_path = './resource/uk.txt'

    with open(file_path, encoding='utf-8') as uk:
         for line in uk.readlines():
             if "[[Category:" in line:
                 print(line.rstrip())

if __name__ == '__main__':
    main()
