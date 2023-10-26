import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
5 47
.#..#..#####..#...#..#####..#...#...###...#####
.#.#...#.......#.#...#......##..#..#...#..#....
.##....#####....#....#####..#.#.#..#......#####
.#.#...#........#....#......#..##..#...#..#....
.#..#..#####....#....#####..#...#...###...#####



"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

H, W = map(int, input().split())

cells = []

for _ in range(H):
    cells.append(list(input()))

history = set()
from collections import deque

ans = 0
for y in range(H):
    for x in range(W):
        if (y, x) not in history:
            history.add((y, x))
            if cells[y][x] == "#":
                ans += 1
                q = deque()
                # 下
                if y + 1 < H:
                    q.append((y + 1, x))
                # 上
                if y - 1 >= 0:
                    q.append((y - 1, x))
                # 右
                if x + 1 < W:
                    q.append((y, x + 1))
                # 左
                if x - 1 >= 0:
                    q.append((y, x - 1))
                # 右下
                if x + 1 < W and y + 1 < H:
                    q.append((y + 1, x + 1))
                # 左下
                if x - 1 >= 0 and y + 1 < H:
                    q.append((y + 1, x - 1))
                # 右上
                if x + 1 < W and y - 1 >= 0:
                    q.append((y - 1, x + 1))
                # 左上
                if x - 1 >= 0 and y - 1 >= 0:
                    q.append((y - 1, x - 1))
                while len(q) > 0:
                    y_tmp, x_tmp = q.popleft()
                    if cells[y_tmp][x_tmp] == "#" and (y_tmp, x_tmp) not in history:
                        history.add((y_tmp, x_tmp))
                        # 下
                        if y_tmp + 1 < H:
                            q.append((y_tmp + 1, x_tmp))
                        # 上
                        if y_tmp - 1 >= 0:
                            q.append((y_tmp - 1, x_tmp))
                        # 右
                        if x_tmp + 1 < W:
                            q.append((y_tmp, x_tmp + 1))
                        # 左
                        if x_tmp - 1 >= 0:
                            q.append((y_tmp, x_tmp - 1))
                        # 右下
                        if x_tmp + 1 < W and y_tmp + 1 < H:
                            q.append((y_tmp + 1, x_tmp + 1))
                        # 左下
                        if x_tmp - 1 >= 0 and y_tmp + 1 < H:
                            q.append((y_tmp + 1, x_tmp - 1))
                        # 右上
                        if x_tmp + 1 < W and y_tmp - 1 >= 0:
                            q.append((y_tmp - 1, x_tmp + 1))
                        # 左上
                        if x_tmp - 1 >= 0 and y_tmp - 1 >= 0:
                            q.append((y_tmp - 1, x_tmp - 1))

print(ans)
