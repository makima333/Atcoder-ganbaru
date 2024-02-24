import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
zzzzzwz



"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------


S = input()

from collections import Counter

c = Counter(S)
for k, v in c.items():
    if v == 1:
        s = k


print(S.find(s) + 1)
