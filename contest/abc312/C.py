import io
from operator import mod
import sys

_INPUT = """\
5 2
100000 100000 100000 100000 100000
100 200


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n, m = map(int, input().split())

aa = list(map(int, input().split()))
bb = list(map(int, input().split()))

aa.sort()
bb.sort()

left = 0
right = 10**9 + 1

import bisect


def check(mid):
    sellers = bisect.bisect_right(aa, mid)
    buyers = m - bisect.bisect_left(bb, mid)
    return sellers >= buyers


while right - left > 1:
    mid = (left + right) // 2
    if check(mid):
        right = mid
    else:
        left = mid

print(right)
