#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    input_path = '../resource/hightemp.txt'
    output_path = '../results/'

    with open(input_path, encoding='utf-8') as f:
        lines = [[cell for cell in line.split('\t')] for line in f.readlines()]
        transposed = list(zip(*lines))

    with open(output_path + 'col1.txt', mode='w', encoding='utf-8') as col1:
        col1.write("\n".join(transposed[0]))

    with open(output_path + 'col2.txt', mode='w', encoding='utf-8') as col2:
        col2.write("\n".join(transposed[1]))

if __name__ == '__main__':
    main()
