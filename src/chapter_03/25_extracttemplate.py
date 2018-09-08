#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def main():
    file_path = './resource/uk.txt'

    pattern_basic_info_block = re.compile(r'\{\{基礎情報.*?$')
    pattern_end_block = re.compile(r'^\}\}$')
    pattern_template = re.compile(r'^\|(.*?)\s=\s(.*)')
    pattern_end_with_br = re.compile(".*<br/>$")
    pattern_template_multi_line = re.compile(r'^\*.*')

    with open(file_path, encoding='utf-8') as uk:
        basic_info_block_started = False
        in_multi_line = False
        hold_key_for_multi_line = ""

        basic_info = dict()

        for line in uk.readlines():
            basic_info_block_is_found = pattern_basic_info_block.search(line.rstrip())
            if pattern_end_block.search(line.rstrip()):
                basic_info_block_started = False

            if basic_info_block_started:
                if in_multi_line and pattern_template_multi_line.match(line.rstrip()):
                    basic_info[hold_key_for_multi_line] += line.rstrip()
                else:
                    in_multi_line = False

                matched_template = pattern_template.search(line.rstrip())
                if matched_template:
                    basic_info[matched_template.group(1)] = matched_template.group(2)
                    if pattern_end_with_br.match((line.rstrip())):
                        hold_key_for_multi_line = matched_template.group(1)
                        in_multi_line = True

            if basic_info_block_is_found:
                basic_info_block_started = True


    for k in basic_info.keys():
        print(f"'{k}': '{basic_info[k]}'")

if __name__ == '__main__':
    main()
