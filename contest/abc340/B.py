import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
5
1 20
1 30
2 1
1 40
2 3

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

Q = int(input())

A = []

for _ in range(Q):
    q, k = map(int, input().split())
    if q == 1:
        A.append(k)
    else:
        print(A[-k])
