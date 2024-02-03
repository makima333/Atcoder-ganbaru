import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
10 10 10


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

H, W, N = map(int, input().split())

# 0: 上, 1: 左, 2: 下, 3: 右
# 上右下左
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

import numpy as np

cells = np.array([["." for _ in range(W)] for _ in range(H)])

now_d = 0
pos = (0, 0)

for _ in range(N):
    # print(pos, now_d)
    v = cells[pos[0], pos[1]]

    if v == ".":
        cells[pos[0]][pos[1]] = "#"
        now_d = (now_d + 1) % 4

        h = pos[0] + directions[now_d][0]
        if h == H:
            h = 0
        elif h == -1:
            h = H - 1

        w = pos[1] + directions[now_d][1]
        if w == W:
            w = 0
        elif w == -1:
            w = W - 1

        pos = (h, w)

    elif v == "#":
        cells[pos[0]][pos[1]] = "."
        now_d = (now_d - 1) % 4

        h = pos[0] + directions[now_d][0]
        if h == H:
            h = 0
        elif h == -1:
            h = H - 1

        w = pos[1] + directions[now_d][1]
        if w == W:
            w = 0
        elif w == -1:
            w = W - 1

        pos = (h, w)


for row in cells:
    print("".join(row))
