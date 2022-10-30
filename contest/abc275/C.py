import io
from operator import mod
import sys

_INPUT = """\
.#.......
#.#......
.#.......
.........
....#.#.#
.........
....#.#.#
........#
.........


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------

sharps = []

for x, _ in enumerate(range(9)):
    row = list(input())
    for y, c in enumerate(row):
        if c == "#":
            sharps.append([x + 1, y + 1])

import copy
import numpy as np

cnt = 0
tmp_sharps = copy.copy(sharps)
for xy in sharps:
    sharps_copy = copy.copy(tmp_sharps)
    cands = {}
    for xy_copy in sharps_copy:
        d = ((xy[0] - xy_copy[0]) ** 2 + (xy[1] - xy_copy[1]) ** 2) ** 0.5
        if d not in cands.keys():
            cands[d] = [xy_copy]
        else:
            for ca in cands[d]:
                vec_1 = [ca[0] - xy[0], ca[1] - xy[1]]
                vec_2 = [xy_copy[0] - xy[0], xy_copy[1] - xy[1]]
                if (
                    np.dot(
                        vec_1,
                        vec_2,
                    )
                    == 0
                ):
                    four_point = [
                        xy[0] + vec_1[0] + vec_2[0],
                        xy[1] + vec_1[1] + vec_2[1],
                    ]
                    if four_point in sharps:
                        cnt += 1
            cands[d].append(xy_copy)

    tmp_sharps.pop(0)


print(cnt)
