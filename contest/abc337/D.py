import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
10 12 6
......xo.o..
x...x.....o.
x...........
..o...x.....
.....oo.....
o.........x.
ox.oox.xx..x
....o...oox.
..o.....x.x.
...o........


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

import numpy as np

H, W, K = map(int, input().split())
grid = np.zeros((H, W), dtype=int)
grid_mirror = np.zeros((H, W), dtype=int)
for h in range(H):
    S = input()
    for w in range(W):
        if S[w] == "o":
            grid[h, w] = 1
            grid_mirror[h, w] = 1
        elif S[w] == "x":
            grid[h, w] = 0
            grid_mirror[h, w] = 0
        elif S[w] == ".":
            grid[h, w] = 0
            grid_mirror[h, w] = 1

ans_index = []
for h in range(H):
    for w in range(W):
        if grid_mirror[h, w] == 0:
            continue
        if w + K <= W:
            tmp = grid_mirror[h, w : K + w]
            if sum(tmp) == K:
                ans_index.append([h, w, "R"])
        if h + K <= H:
            tmp = grid_mirror[h : K + h, w]
            if sum(tmp) == K:
                ans_index.append([h, w, "D"])


diff = grid_mirror - grid
ans = (2 * (10**5)) + 1
for a in ans_index:
    h, w, direction = a
    if direction == "R":
        ans = min(sum(diff[h, w : K + w]), ans)
    elif direction == "D":
        ans = min(sum(diff[h : K + h, w]), ans)


if ans == (2 * (10**5)) + 1:
    print(-1)
else:
    print(ans)
