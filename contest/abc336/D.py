import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
5
2 2 3 1 1

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N = int(input())
A = [0] + list(map(int, input().split()))

l, r = [0] * (N + 2), [0] * (N + 2)
for i in range(1, N + 1):
    l[i] = min(A[i], l[i - 1] + 1)
for i in range(N, 0, -1):
    r[i] = min(A[i], r[i + 1] + 1)

print(max(min(l[i], r[i]) for i in range(1, N + 1)))
