#!/usr/bin/env python
# -*- coding: utf-8 -*-

def patrol(text):
    return text[::2]


def main():
    print(patrol(u"パタトクカシーー"))


if __name__ == '__main__':
    main()
