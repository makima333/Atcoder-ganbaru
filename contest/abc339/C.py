import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
4
-1 1000000000 1000000000 1000000000


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N = int(input())
A = list(map(int, input().split()))

ans = 0
now_p = 0

for a in A:
    now_p += a
    if now_p < 0:
        ans += abs(now_p)
        now_p = 0

print(ans + sum(A))
