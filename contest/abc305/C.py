import io
from operator import mod
import sys

_INPUT = """\
6 6
..####
..##.#
..####
..####
..####
......


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------

h, w = map(int, input().split())

grid = [list(input()) for _ in range(h)]
cnt_list = [1000 for _ in range(h)]
start_list = [1000 for _ in range(h)]
end_list = [0 for _ in range(h)]
min_cnt = 1000

for row_i, row in enumerate(grid):
    ctype = set(row)
    if len(ctype) == 1 and ctype == set(["."]):
        continue

    start = -1
    end = -1
    cnt = 0
    for c_i, c in enumerate(row):
        if start == -1 and c == "#":
            start = c_i

        if c == "#":
            cnt += 1
            end = c_i

    cnt_list[row_i] = cnt
    if min_cnt > min(cnt_list):
        target_row = row_i
        min_cnt = min(cnt_list)
    start_list[row_i] = start
    end_list[row_i] = end

for i in range(min(start_list), max(end_list) + 1):
    if grid[target_row][i] == ".":
        target_col = i
        break


print(target_row + 1, target_col + 1)
