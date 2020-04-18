import re
from typing import Dict, List

def q00(s: str) -> str:
    return s[::-1]

def q01(s: str) -> str:
    return "".join(s[::2])

def q02(s1: str, s2: str) -> str:
    return "".join([i + j for i, j in zip(s1, s2)])

def q03(s: str) -> List[int]:
    a_to_z = re.compile(r"[^a-zA-Z]")
    return [len(a_to_z.sub("", word)) for word in s.split()]

def q04(text: str) -> Dict[str, int]:
    pick_only_first_char = (1, 5, 6, 7, 8, 9, 15, 16, 19)
    char_to_position = {}

    for i, word in enumerate(text.split()):
        if i + 1 in pick_only_first_char:
            char_to_position[word[0:1]] = i + 1
        else:
            char_to_position[word[0:2]] = i + 1

    return char_to_position


def q05():
    pass

def q06():
    pass

def q07():
    pass

def q08():
    pass

def q09():
    pass
