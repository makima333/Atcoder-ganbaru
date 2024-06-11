import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
SunTORY

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
S = input()

# count big letters
b = 0
small = 0
for s in S:
    if s.isupper():
        b += 1
    else:
        small += 1


if b > small:
    print(S.upper())
else:
    print(S.lower())
