import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
1 1 100
100


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------\
n, k, x = map(int, input().split())
A = list(map(int, input().split()))

ans = []
for a_i, a in enumerate(A):
    ans.append(a)
    if a_i + 1 == k:
        ans.append(x)
print(*ans)
