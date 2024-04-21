import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
9 20
9 5 1 2 2 2 8 9 2 1 6 2 6 5 8 7 8 5 9 8

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N, Q = map(int, input().split())
T = list(map(int, input().split()))
tooth = [1 for _ in range(N)]


for t in T:
    if tooth[t - 1] == 1:
        tooth[t - 1] = 0
    else:
        tooth[t - 1] = 1


print(sum(tooth))
