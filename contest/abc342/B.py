import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
7
3 7 2 1 6 5 4
13
2 3
1 2
1 3
3 6
3 7
2 4
3 7
1 3
4 7
1 6
2 4
1 3
1 3


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N = int(input())
P = list(map(int, input().split()))
Q = int(input())

orderp = [0] * N
for pi, p in enumerate(P):
    orderp[p - 1] = pi

for _ in range(Q):
    a, b = map(int, input().split())
    if orderp[a - 1] < orderp[b - 1]:
        print(a)
    else:
        print(b)
