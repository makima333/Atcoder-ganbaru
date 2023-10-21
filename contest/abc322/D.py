import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
....
..#.
....
....
....
..#.
....
....
....
..#.
....
....

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
# ポリオミノ

import numpy as np

P = [list(input()) for _ in range(12)]
grids = np.array([[1 if cell == "#" else 0 for cell in line] for line in P])
grids = grids.reshape(3, 4, 4)


# 左上に移動
def shift_initial_pos(array_2d):
    min_row = np.min(np.where(array_2d.any(axis=1)))
    min_col = np.min(np.where(array_2d.any(axis=0)))

    shifted_array = np.zeros_like(array_2d)
    rows, cols = array_2d.shape

    for i in range(min_row, rows):
        for j in range(min_col, cols):
            shifted_array[i - min_row, j - min_col] = array_2d[i, j]
    return shifted_array


# 右シフト
def shift_right(array_2d, x):
    if x == 0:
        return array_2d

    if len(array_2d) == 0 or np.any(array_2d[:, -x:]):
        return []
    return np.roll(array_2d, shift=x, axis=1)


# 下シフト
def shift_down(array_2d, y):
    if y == 0:
        return array_2d

    if len(array_2d) == 0 or np.any(array_2d[-y, :]):
        return []
    return np.roll(array_2d, shift=y, axis=0)


# 回転
def rot(array_2d):
    return np.rot90(array_2d, 1)


def check_overlap(board, poly):
    if np.any((board + poly) >= 2):
        return True
    return False


init_grids = np.array([shift_initial_pos(g) for g in grids])
board = np.zeros((4, 4), dtype=int)

if np.sum(init_grids) != 16:
    print("No")
    exit()


def polymino(board, polys):
    if np.all(board):
        return True
    if polys.shape[0] == 0:
        # print(board)
        return False

    poly = polys[0]
    remain_polys = np.delete(polys, 0, axis=0)
    for _ in range(4):
        for x in range(4):
            for y in range(4):
                shifted_poly = shift_right(shift_down(poly, y), x)
                if len(shifted_poly) != 0:
                    if check_overlap(board, shifted_poly) == False:
                        over_poly = shifted_poly + board

                        if polymino(over_poly.copy(), remain_polys.copy()):
                            return True

        poly = shift_initial_pos(rot(poly))


if polymino(board, init_grids):
    print("Yes")
else:
    print("No")
