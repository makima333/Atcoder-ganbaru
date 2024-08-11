import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
3
abc
de
fghi


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
N = int(input())
chars = []
max_len = 0
for _ in range(N):
    s = input()
    max_len = max(max_len, len(s))
    chars.append(list(s))

moji = ["" for _ in range(max_len)]

for s in chars:
    for i in range(max_len):
        if i < len(s):
            moji[i] += s[i]
        else:
            moji[i] += "*"

# print(moji)
for m in moji:
    tmp = m.lstrip("*")
    print(tmp[::-1])
