import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
6
3 2
1 6
4 5
1 3
5 5
9 8


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N = int(input())
xy = [tuple(map(int, input().split())) for _ in range(N)]


def distance(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


for i in range(N):
    max_d_idx = -1
    max_d = 0
    for j in range(N):
        d = distance(xy[i], xy[j])
        if d > max_d:
            max_d = d
            max_d_idx = j
    print(max_d_idx + 1)
