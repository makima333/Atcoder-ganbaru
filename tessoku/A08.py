import io
from operator import mod
import sys

_INPUT = """\
5 5
2 0 0 5 1
1 0 3 0 0
0 8 5 0 2
4 1 0 0 6
0 9 2 7 0
2
2 2 4 5
1 1 5 5


"""
sys.stdin = io.StringIO(_INPUT)
# --------------------------------
h, w = map(int, input().split())
grid = []
tmp_sum = []

for _ in range(h):
    tmp = []

    for cell in list(map(int, input().split())):
        if tmp:
            tmp.append(tmp[-1] + cell)
        else:
            tmp.append(cell)
    tmp_sum.append(tmp)

import copy

sumhis = []
tmp = [0] * w
for row in tmp_sum:
    tmp = copy.copy(tmp)
    for cell_i, cell in enumerate(row):
        tmp[cell_i] += cell
    sumhis.append(tmp)

q = int(input())
for _ in range(q):
    ans = 0
    x_1, y_1, x_2, y_2 = map(int, input().split())
    x_1, y_1, x_2, y_2 = x_1 - 1, y_1 - 1, x_2 - 1, y_2 - 1
    ans = sumhis[x_2][y_2]
    if y_1 > 0:
        ans -= sumhis[x_2][y_1 - 1]

    if x_1 > 0:
        ans -= sumhis[x_1 - 1][y_2]

    if y_1 > 0 and x_1 > 0:
        ans += sumhis[x_1 - 1][y_1 - 1]

    print(ans)
