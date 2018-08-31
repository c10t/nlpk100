#!/usr/bin/env python
# -*- coding: utf-8 -*-

def patatcaxi(text1, text2):
    return "".join([i + j for i, j in zip(text1, text2)])


def main():
    print(patatcaxi(u"パトカー", u"タクシー"))


if __name__ == '__main__':
    main()
