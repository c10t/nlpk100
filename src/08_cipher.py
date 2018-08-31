#!/usr/bin/env python
# -*- coding: utf-8 -*-


def cipher(text):
    return "".join([chr(219-ord(char)) if char.islower() else char for char in text])


def main():
    encrypted = cipher("I couldn't be1i3v3 that I could actually understand wh4t I was reading : \
    the phenomenal power of the human mind .")
    decrypted = cipher(encrypted)
    print(encrypted)
    print(decrypted)


if __name__ == '__main__':
    main()
