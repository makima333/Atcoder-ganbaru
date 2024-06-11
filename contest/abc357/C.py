import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
3
"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N = int(input())

if N == 0:
    print("#")
    exit()


one_grid = """###
#.#
###"""


def merge(grid: str, other: str, n: int) -> str:
    grid = grid.split("\n")
    other = other.split("\n")
    ans = ""
    n += 1
    for i in range(3 ** (n - 1)):
        if i != (3 ** (n - 1)) - 1:
            ans += grid[i] + other[i] + "\n"
        else:
            ans += grid[i] + other[i]

    return ans


ans = ""
for i in range(N):
    if i == 0:
        ans = one_grid
    else:
        line_1 = ans
        for j in range(2):
            line_1 = merge(line_1, ans, i)
        line_2 = ans
        white_grid = ""
        for k in range(3 ** ((i + 1) - 1)):
            for t in range(3 ** ((i + 1) - 1)):
                white_grid += "."
            if k != (3 ** ((i + 1) - 1)) - 1:
                white_grid += "\n"

        line_2 = merge(line_2, white_grid, i)
        line_2 = merge(line_2, ans, i)

        ans = line_1 + "\n" + line_2 + "\n" + line_1
    # print(ans)


print(ans)
