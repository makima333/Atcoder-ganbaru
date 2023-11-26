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

_, L, R = map(int, input().split())
AA = list(map(int, input().split()))

ans = []

for a in AA:
    if a < L:
        ans.append(L)
    elif a > R:
        ans.append(R)
    else:
        ans.append(a)

print(*ans)
