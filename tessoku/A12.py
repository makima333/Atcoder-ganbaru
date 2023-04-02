import io
from operator import mod
import sys

_INPUT = """\
4 10
1 2 3 4


"""
sys.stdin = io.StringIO(_INPUT)
# --------------------------------
n, k = map(int, input().split())
aa = list(map(int, input().split()))

left = 1
right = 10**9

while left < right:
    mid = (left + right) // 2
    tmp_sum = 0
    for a in aa:
        tmp_sum += mid // a

    if tmp_sum < k:
        left = mid + 1
    else:
        right = mid

print(left)
