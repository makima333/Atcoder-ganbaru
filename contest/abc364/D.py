import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
10 5
-84 -60 -41 -100 8 -8 -52 -62 -61 -76
-52 5
14 4
-2 6
46 2
26 7


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
from bisect import bisect_left, bisect_right


for _ in range(Q):
    b, k = map(int, input().split())
    l, r = -1, 2 * 10**8 + 1
    while r - l > 1:
        m = (r + l) // 2
        lb = bisect_left(A, b - m)
        rb = bisect_right(A, b + m)
        if rb - lb >= k:
            r = m
        else:
            l = m
    print(r)
