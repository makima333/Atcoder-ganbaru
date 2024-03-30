import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
0 0

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------


a, b = map(int, input().split())
ab = a + b

for i in range(10):
    if i != ab:
        print(i)
        exit()
