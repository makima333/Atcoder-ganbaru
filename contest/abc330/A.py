import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
5 4 7
3 1 4 9 7

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

n, X = map(int, input().split())
SS = list(map(int, input().split()))

ans = 0

for s in SS:
    if s >= X:
        ans += 1

print(ans)
