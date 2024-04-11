import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
10
68 3
17 2
99 2
92 4
82 4
10 3
100 2
78 1
3 1
35 4

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
from collections import defaultdict

N = int(input())
AC = [tuple(map(int, input().split())) for _ in range(N)]

colors = defaultdict(lambda: 10**9 + 1)

for a, c in AC:
    colors[c] = min(colors[c], a)

colors = sorted(colors.items(), key=lambda x: x[1], reverse=True)

print(colors[0][1])
