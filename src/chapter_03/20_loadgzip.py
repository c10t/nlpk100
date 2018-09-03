#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gzip
import json

def main():
    file_path = './resource/jawiki-country.json.gz'

    with gzip.open(file_path) as gz:
        for line in gz:
            data = json.loads(line)
            if data['title'] == u'イギリス':
                # with open('./resource/uk.txt', mode='w', encoding='utf-8') as uk:
                #    uk.write(data['text'])
                print(data)
                break

if __name__ == '__main__':
    main()
