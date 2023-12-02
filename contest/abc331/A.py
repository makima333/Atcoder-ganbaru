import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
12 30
2012 6 30



"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
M, D = map(int, input().split())
y, m, d = map(int, input().split())


if d == D:
    d = 1
    m += 1 if M != m else 0
    if M == m:
        m = 1
        y += 1

    print(y, m, d)
else:
    print(y, m, d + 1)
