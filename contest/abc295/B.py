import io
from operator import mod
import sys

_INPUT = """\
4 6
#.#3#.
###.#.
##.###
#1..#.


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
r, c = map(int, input().split())

grid = [list(input()) for _ in range(r)]


def check(src, dst):
    if dst in [".", "#"]:
        return src

    dst_int = int(dst)
    return max(src, dst_int)


for _ in range(10):
    # print("##")
    # for row in grid:
    #     print(row)

    x = 0
    while x != r:
        y = 0
        while y != c:

            if grid[x][y] in [".", "#", "0"]:
                # x += 1
                y += 1
                continue

            cell = int(grid[x][y])

            tmp = cell - 1

            if x + 1 != r:
                grid[x + 1][y] = str(check(tmp, grid[x + 1][y]))
            if x - 1 != -1:
                grid[x - 1][y] = str(check(tmp, grid[x - 1][y]))
            if y + 1 != c:
                grid[x][y + 1] = str(check(tmp, grid[x][y + 1]))
            if y - 1 != -1:
                grid[x][y - 1] = str(check(tmp, grid[x][y - 1]))
            y += 1
        x += 1


for row in grid:
    for c in row:
        if c != "#":
            print(".", end="")
        else:
            print("#", end="")
    print("")
