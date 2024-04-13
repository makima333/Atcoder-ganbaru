import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
6
10 20 30 40 50

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------


N = int(input())
A = list(map(int, input().split()))

suma = sum(A)
print((-1) * suma)
