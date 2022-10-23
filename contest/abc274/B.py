import io
from operator import mod
import sys

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
h, w = map(int, input().split())

grids = [list(input()) for _ in range(h)]

cnts = [0] * w
for r in grids:
    for i, c in enumerate(r):
        if c == "#":
            cnts[i] += 1

print(*cnts)
