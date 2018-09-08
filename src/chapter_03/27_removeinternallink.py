#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


def extract_basic_info(file_path):
    pattern_basic_info_block = re.compile(r'{{基礎情報.*?$')
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

    return basic_info


def main():
    file_path = './resource/uk.txt'
    info = extract_basic_info(file_path)

    pattern_emphasis = re.compile(r"'{2,5}")
    pattern_internal_link = re.compile(r"\[{2}([^\[\]]*)\]{2}")
    pattern_has_represent = re.compile(r"(.*)\|(.*)")

    for key in info.keys():
        info[key] = pattern_emphasis.sub(r"", info[key])

        link = pattern_internal_link.finditer(info[key])
        for li in link:
            info[key] = info[key].replace(li.group(0), li.group(1))
            # print(f"...has internal link: {li.group(0)} -> {li.group(1)}")
            has_repr = pattern_has_represent.search(li.group(1))
            if has_repr:
                # print(f"...use article name: {has_repr.group(0)} -> {has_repr.group(1)}")
                info[key] = info[key].replace(has_repr.group(0), has_repr.group(1))

        print(f"{key}: {info[key]}")


if __name__ == '__main__':
    main()
