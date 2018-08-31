#!/usr/bin/env python
# -*- coding: utf-8 -*-


def set_to_template(x, y, z):
    return f"{x}時の{y}は{z}"


def main():
    print(set_to_template(12, u"気温", 22.4))


if __name__ == '__main__':
    main()
