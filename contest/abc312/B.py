import io
from operator import mod
import sys

_INPUT = """\
19 18
###......###......
###......###......
###..#...###..#...
..............#...
..................
..................
......###......###
......###......###
......###......###
.###..............
.###......##......
.###..............
............###...
...##.......###...
...##.......###...
.......###........
.......###........
.......###........
........#.........

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
import re

n, m = map(int, input().split())
grids = [input() for _ in range(n)]

target = "###\\."
target_l = "###."
target_r = ".###"
start_cells = []

for i, row in enumerate(grids):
    for match in re.finditer(target, row):
        j = match.start()
        start_cells.append((i, j))

for si, sj in start_cells:
    res = False
    if sj + 4 > m or si + 3 >= n:
        continue
    if (
        grids[si + 1][sj : sj + 4] == target_l
        and grids[si + 2][sj : sj + 4] == target_l
        and grids[si + 3][sj : sj + 4] == "...."
    ):
        res = True

    ei = si + 6
    ej = sj + 5
    if ei + 2 >= n or ej + 4 > m:
        continue
    if (
        grids[ei][ej : ej + 4] == target_r
        and grids[ei + 1][ej : ej + 4] == target_r
        and grids[ei + 2][ej : ej + 4] == target_r
        and grids[ei - 1][ej : ej + 4] == "...."
    ):
        res = True
    else:
        res = False

    if res:
        print(si + 1, sj + 1)
