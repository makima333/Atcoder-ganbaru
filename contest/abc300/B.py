import io
from operator import mod
import sys

_INPUT = """\
10 30
..........##########..........
..........####....###.....##..
.....##....##......##...#####.
....####...##..#####...##...##
...##..##..##......##..##....#
#.##....##....##...##..##.....
..##....##.##..#####...##...##
..###..###..............##.##.
.#..####..#..............###..
#..........##.................
................#..........##.
######....................####
....###.....##............####
.....##...#####......##....##.
.#####...##...##....####...##.
.....##..##....#...##..##..##.
##...##..##.....#.##....##....
.#####...##...##..##....##.##.
..........##.##...###..###....
...........###...#..####..#...


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------

h, w = map(int, input().split())
acells = [list(input()) for _ in range(h)]
bcells = [list(input()) for _ in range(h)]
import copy


def vec_shift(cells):
    tmp = []
    for i, c in enumerate(cells):
        # print((i + 1) % (len(cells)))s
        tmp.append(cells[(i + 1) % (len(cells))])

    return tmp


def hor_shift(cells):
    tmp = []
    for row in cells:
        tmp_array = []
        for i, cell in enumerate(row):

            tmp_array.append(row[(i + 1) % (len(row))])
        tmp.append(tmp_array)

    return tmp


def check(ss, dd):
    for i, s in enumerate(ss):
        if "".join(s) != "".join(dd[i]):
            return False

    return True


tmpcells = acells
for _ in range(h):
    tmpcells = vec_shift(tmpcells)
    if check(tmpcells, bcells):
        print("Yes")
        exit()

    for _ in range(w):
        tmpcells = hor_shift(tmpcells)
        if check(tmpcells, bcells):
            print("Yes")
            exit()


print("No")
