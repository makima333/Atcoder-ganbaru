import io
from operator import mod
import sys

_INPUT = """\
2
0 0 3 3
2 2 4 4


"""
sys.stdin = io.StringIO(_INPUT)
# --------------------------------
n = int(input())
max_xy = 1501

cells = [[0] * max_xy for _ in range(max_xy)]

for _ in range(n):
    a, b, c, d = map(int, input().split())
    cells[a][b] += 1
    cells[a][d] -= 1
    cells[c][b] -= 1
    cells[c][d] += 1

for x in range(max_xy):
    for y in range(max_xy):
        if y > 0:
            cells[x][y] += cells[x][y - 1]


for y in range(max_xy):
    for x in range(max_xy):
        if x > 0:
            cells[x][y] += cells[x - 1][y]


ans = 0
for row in cells:
    for cell in row:
        if cell > 0:
            ans += 1

# import pprint

# pprint.pprint(cells)
print(ans)
