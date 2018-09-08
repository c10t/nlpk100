#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def main():
    file_path = './resource/uk.txt'

    # intend to extract == Section == or ==Section==
    pattern = re.compile(r'^(=+)(.*?)(=+)$')

    with open(file_path, encoding='utf-8') as uk:
         for line in uk.readlines():
             matched = pattern.search(line.rstrip())
             if matched:
                 print(f"{matched.group(2).rstrip()} - {len(matched.group(1)) - 1}")

if __name__ == '__main__':
    main()
