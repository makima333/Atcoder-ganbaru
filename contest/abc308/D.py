import io
from operator import mod
import sys

_INPUT = """\
5 7
skunsek
nukesnu
ukeseku
nsnnesn
uekukku


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
h, w = map(int, input().split())

grid = [list(input()) for _ in range(h)]

if grid[0][0] != "s" or grid[h - 1][w - 1] not in ["s", "n", "u", "k", "e"]:
    print("No")
    exit()

from collections import deque

history = set([])
cand = deque([])

# first time
if grid[0][1] == "n":
    cand.append((0, 1))

if grid[1][0] == "n":
    cand.append((1, 0))
x = 0
y = 0

if len(cand) == 0:
    print("No")
    exit()


def next_snuke(c):
    if c == "s":
        return "n"
    if c == "n":
        return "u"
    if c == "u":
        return "k"
    if c == "k":
        return "e"
    if c == "e":
        return "s"


# bfs, grid, cells, mass
while True:
    if len(cand) == 0:
        print("No")
        exit()

    y, x = cand.popleft()
    if y == h - 1 and x == w - 1:
        print("Yes")
        exit()

    if (y, x) not in history:
        history.add((y, x))
    else:
        continue

    next_c = next_snuke(grid[y][x])

    if x + 1 < w:
        if grid[y][x + 1] == next_c:
            cand.append((y, x + 1))

    if y + 1 < h:
        if grid[y + 1][x] == next_c:
            cand.append((y + 1, x))

    if x - 1 >= 0:
        if grid[y][x - 1] == next_c:
            cand.append((y, x - 1))

    if y - 1 >= 0:
        if grid[y - 1][x] == next_c:
            cand.append((y - 1, x))
