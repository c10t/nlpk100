import re
from typing import List

def q00(s: str) -> str:
    return s[::-1]

def q01(s: str) -> str:
    return "".join(s[::2])

def q02(s1: str, s2: str) -> str:
    return "".join([i + j for i, j in zip(s1, s2)])

def q03(s: str) -> List[int]:
    a_to_z = re.compile(r"[^a-zA-Z]")
    return [len(a_to_z.sub("", word)) for word in s.split()]

def q04():
    pass

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
