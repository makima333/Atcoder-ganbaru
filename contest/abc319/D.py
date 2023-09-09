import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
13 3
9 5 2 7 1 8 8 2 1 5 2 3 6

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N, M = map(int, input().split())
ll = list(map(int, input().split()))

left = max(ll)
right = sum(ll) + N - 1


def logic(mid):
    cnt = 1
    width = 0

    for l in ll:
        if width == 0:
            width += l
        else:
            width += l + 1
        if width > mid:
            cnt += 1
            width = l

    return cnt <= M


while left < right:
    mid = (left + right) // 2
    cal_res = logic(mid)
    if cal_res:
        right = mid
    else:
        left = mid + 1

print(left)
