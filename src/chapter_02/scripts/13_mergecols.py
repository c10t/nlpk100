#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    col1_path = '../resource/col1.txt'
    col2_path = '../resource/col2.txt'
    output_path = '../results/'

    with open(col1_path, encoding='utf-8') as col1, open(col2_path, encoding='utf-8') as col2, \
          open(output_path + 'merged.txt', mode='w', encoding='utf-8') as merged:
        for line1, line2 in zip(col1, col2):
            merged.write("\t".join((line1.rstrip(), line2.rstrip() + "\n"))) # unnecessary to rstrip line2

if __name__ == '__main__':
    main()
