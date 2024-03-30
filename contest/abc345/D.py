import io
from operator import mod
import sys

# 再帰用
sys.setrecursionlimit(10**9)


_INPUT = """\
5 3 3
1 1
2 2
2 2
2 2
2 2


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
# テトロミノ

import sys

# 再帰用
sys.setrecursionlimit(10**9)


N, H, W = map(int, input().split())
board = [[0] * W for _ in range(H)]
tiles = [None] * (2 * N)
used = [False] * (N)

for i in range(N):
    r, c = map(int, input().split())
    tiles[i] = (r, c)
    tiles[i + N] = (c, r)


def can_place_tile(board, tile, x, y):
    h, w = tile
    for i in range(h):
        for j in range(w):
            if (
                x + i >= len(board)
                or y + j >= len(board[0])
                or board[x + i][y + j] != 0
            ):
                return False
    return True


def place_tile(board, tile, x, y):
    h, w = tile
    for i in range(h):
        for j in range(w):
            board[x + i][y + j] = 1


def remove_tile(board, tile, x, y):
    h, w = tile
    for i in range(h):
        for j in range(w):
            board[x + i][y + j] = 0


def solve(board, tiles, x, y, used):
    if y >= len(board[0]):
        x += 1
        y = 0
    if x >= len(board):
        return True

    if board[x][y] != 0:
        return solve(board, tiles, x, y + 1, used)

    for i, tile in enumerate(tiles):
        if i >= N:
            i = i - N
        if used[i]:
            continue
        if can_place_tile(board, tile, x, y):
            place_tile(board, tile, x, y)
            used[i] = True
            if solve(board, tiles, x, y + 1, used):
                return True
            used[i] = False
            remove_tile(board, tile, x, y)
    return False


result = solve(board, tiles, 0, 0, used)
print("Yes" if result else "No")
