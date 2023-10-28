import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
10 9
0 0 0  4 8 8 8 9 9 9 

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
a.append(9000000000000)

res = 0
r = 0
for l in range(0, n):
    while a[r] < a[l] + m:
        r += 1
    res = max(res, r - l)

print(res)
