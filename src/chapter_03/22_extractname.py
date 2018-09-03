#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def main():
    file_path = './resource/uk.txt'
    pattern = re.compile(r'^\[\[Category:(.*?)(\|.*)?\]\]$')

    with open(file_path, encoding='utf-8') as uk:
         for line in uk.readlines():
             matched = pattern.search(line.rstrip())
             if matched:
                 print(matched.group(1))

if __name__ == '__main__':
    main()
