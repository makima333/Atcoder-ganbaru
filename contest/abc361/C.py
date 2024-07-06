import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
8 3
31 43 26 6 18 36 22 13

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
ans = (10**9) + 1

for i in range(K + 1):
    # print(i, i + (N - K) - 1)
    ans = min(ans, A[i + (N - K) - 1] - A[i])
print(ans)
