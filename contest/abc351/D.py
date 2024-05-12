import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
3 5
.#...
.....
.#..#


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]
from collections import deque

q = deque()
ans = -1

stop_cells = [[0] * W for _ in range(H)]
for h in range(H):
    for w in range(W):
        if grid[h][w] == "#":
            continue
        for dh, dw in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nh, nw = h + dh, w + dw
            if 0 <= nh < H and 0 <= nw < W and grid[nh][nw] == "#":
                stop_cells[h][w] = 1
                break

history = [[0] * W for _ in range(H)]
for th in range(H):
    for tw in range(W):
        if history[th][tw] == 1 or grid[th][tw] == "#":
            continue

        if stop_cells[th][tw] == 1:
            ans = max(ans, 1)
            continue

        tmp_history = [[0] * W for _ in range(H)]
        q.append((th, tw))
        area = 0
        tmp_history[th][tw] = 1
        while q:
            h, w = q.popleft()
            area += 1

            if stop_cells[h][w] == 1:
                continue
            history[h][w] = 1

            for dh, dw in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nh, nw = h + dh, w + dw
                if 0 <= nh < H and 0 <= nw < W:
                    if grid[nh][nw] == "#" or tmp_history[nh][nw] == 1:
                        continue
                    tmp_history[nh][nw] = 1
                    q.append((nh, nw))

        ans = max(ans, area)

print(ans)
