import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
3

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N = int(input())

for i in range(N + 1):
    for j in range(N + 1):
        for k in range(N + 1):
            if i + j + k <= N:
                print(f"{i} {j} {k}")
