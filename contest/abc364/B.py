import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
6 6
1 1
.#####
######
######
######
######
######
RURLDLULLRULRDL

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
H, W = map(int, input().split())
sy, sx = map(int, input().split())

grid = [list(input()) for _ in range(H)]
operations = list(input())

operations_dict = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}


for ope in operations:
    dy, dx = operations_dict[ope]
    ny = sy + dy
    nx = sx + dx

    if 0 <= ny - 1 < H and 0 <= nx - 1 < W and grid[ny - 1][nx - 1] == ".":
        sy = ny
        sx = nx
    # print(sy, sx, ope)

print(sy, sx)
