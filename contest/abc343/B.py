import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
5
0 1 0 1 1
1 0 0 1 0
0 0 0 0 1
1 1 0 0 1
1 0 1 1 0

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N = int(input())

for _ in range(N):
    ans = []
    row = list(map(int, input().split()))
    for i, r in enumerate(row):
        if r == 1:
            ans.append(i + 1)
    if ans:
        print(*ans)
