import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
4 3
5 3 11 8
16
7
1000

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
N, Q = map(int, input().split())

RR = list(map(int, input().split()))

RR.sort()

RR_sums = [0]
for r in RR:
    RR_sums.append(RR_sums[-1] + r)

RR_sums = RR_sums[1:]

from bisect import bisect_right

for _ in range(Q):
    t = int(input())
    ridx = bisect_right(RR_sums, t)
    if ridx > len(RR_sums) - 1:
        ans = N
    else:
        ans = ridx
    print(ans)
