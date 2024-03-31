import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
5 2
2 5 6 7 10

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = []
for i, n in enumerate(A):
    if n % K == 0:
        ans.append(n // K)

print(*ans)
