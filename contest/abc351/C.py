import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
5
0 0 0 1 2

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
N = int(input())
balls = list(map(int, input().split()))

from collections import deque

q = deque()

for i in range(N):

    q.append(balls[i])

    while True:
        if len(q) == 1:
            break

        if q[-1] == q[-2]:
            tmp = q.pop()
            q.pop()
            q.append(tmp + 1)
        else:
            break
    # print(i + 1, q)

print(len(q))
