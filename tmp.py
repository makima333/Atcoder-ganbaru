import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
17

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N = int(input())

ans = 1

for i in range(1, 12):
    ans *= N - i

from math import factorial

print(ans // factorial(11))
