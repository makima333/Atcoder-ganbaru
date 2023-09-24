import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
5 180
40 60 80 50


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
N, X = map(int, input().split())
aa = list(map(int, input().split()))

import copy

for i in range(101):
    tmp = copy.copy(aa)
    tmp.append(i)
    tmp.sort()
    if X <= sum(tmp[1:-1]):
        print(i)
        exit()

print(-1)
