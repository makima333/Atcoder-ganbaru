import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
4
8 2 5 1

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
import copy

N = int(input())
A = list(map(int, input().split()))


tmpA = sorted(A, reverse=True)
tmp = tmpA[1]

for i, a in enumerate(A):
    if a == tmp:
        ans = i + 1
        break


print(ans)
