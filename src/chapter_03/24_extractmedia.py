#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def main():
    file_path = './resource/uk.txt'

    # intend to extract File:hoge| or ファイル:piyo|
    pattern = re.compile(r'(File|ファイル):(.*?)\|')

    with open(file_path, encoding='utf-8') as uk:
         for line in uk.readlines():
             matched = pattern.search(line.rstrip())
             if matched:
                 print(f"{matched.group(2).rstrip()}")

if __name__ == '__main__':
    main()
