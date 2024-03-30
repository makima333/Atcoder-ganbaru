import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
10 10
7 2620
9 2620
8 3375
1 3375
6 1395
5 1395
6 2923
10 3375
9 5929
5 1225


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N, T = map(int, input().split())

points = [0 for _ in range(N)]

from collections import defaultdict

nums = defaultdict(int)
nums[0] = N

for _ in range(T):
    a, b = map(int, input().split())

    nums[points[a - 1]] -= 1
    if nums[points[a - 1]] == 0:
        del nums[points[a - 1]]
    points[a - 1] += b
    nums[points[a - 1]] += 1
    print(len(nums))
