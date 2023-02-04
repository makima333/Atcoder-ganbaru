import io
from operator import mod
import sys

_INPUT = """\
5 4 2
1 1 3 3
1 1 5 4


"""
sys.stdin = io.StringIO(_INPUT)
# --------------------------------
h, w, n = map(int, input().split())
cells = [[0] * (w + 2) for _ in range(h + 2)]

for _ in range(n):
    a, b, c, d = map(int, input().split())
    cells[a][b] += 1
    cells[a][d + 1] -= 1
    cells[c + 1][b] -= 1
    cells[c + 1][d + 1] += 1

import pprint

# pprint.pprint(cells)


# 横方向に対する累積和
for x in range(1, h + 1):
    for y in range(1, w + 1):
        cells[x][y] += cells[x][y - 1]


# pprint.pprint(cells)

# 縦方向に対する累積和
for y in range(1, w + 1):
    for x in range(1, h + 1):
        cells[x][y] += cells[x - 1][y]


# pprint.pprint(cells)
for x in range(1, h + 1):
    print(*cells[x][1:-1])
