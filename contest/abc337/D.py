import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
3 3 3
x..
..x
.x.



"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

import numpy as np

H, W, K = map(int, input().split())
grid = np.array([list(input()) for _ in range(H)])

ans = 2 * (10**5) + 1
x = [0 for _ in range(W + 1)]
d = [0 for _ in range(W + 1)]

for h in range(H):
    for w in range(1, W + 1):
        x[w], d[w] = x[w - 1], d[w - 1]
        if grid[h, w - 1] == ".":
            d[w] += 1
        elif grid[h, w - 1] == "x":
            x[w] += 1
    for w in range(1, W - K + 2):
        if x[w + K - 1] - x[w - 1] == 0:
            ans = min(ans, d[w + K - 1] - d[w - 1])

x = [0 for _ in range(H + 1)]
d = [0 for _ in range(H + 1)]
for w in range(W):
    for h in range(1, H + 1):
        x[h], d[h] = x[h - 1], d[h - 1]
        if grid[h - 1, w] == ".":
            d[h] += 1
        elif grid[h - 1, w] == "x":
            x[h] += 1

    for h in range(1, H - K + 2):
        if x[h + K - 1] - x[h - 1] == 0:
            ans = min(ans, d[h + K - 1] - d[h - 1])

if ans == 2 * (10**5) + 1:
    print(-1)
else:
    print(ans)
