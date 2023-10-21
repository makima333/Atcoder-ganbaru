import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
8 5
1 3 4 7 8


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N, M = map(int, input().split())
AA = list(map(int, input().split()))
from bisect import bisect_left

for i in range(1, N + 1):
    # print(bisect(AA, i))
    print(AA[bisect_left(AA, i)] - i)
