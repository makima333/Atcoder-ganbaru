import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
1 2 3 4 5 6 7 8 9
4 5 6 7 8 9 1 2 3
7 8 9 1 2 3 4 5 6
1 2 3 4 5 6 7 8 9
4 5 6 7 8 9 1 2 3
7 8 9 1 2 3 4 5 6
1 2 3 4 5 6 7 8 9
4 5 6 7 8 9 1 2 3
7 8 9 1 2 3 4 5 6



"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

sudoku = []
res = True
sudoku_33 = [[] for _ in range(9)]

for _ in range(9):
    sudoku.append(list(map(int, input().split())))

for row in sudoku:
    if len(set(row)) != 9:
        res = False

# print(res)
import numpy as np

sudoku_90 = np.rot90(np.array(sudoku), k=-1).tolist()

for col in sudoku_90:
    if len(set(col)) != 9:
        res = False

# print(res)

blocks = np.array(sudoku_90).reshape(3, 3, 3, 3).swapaxes(1, 2).reshape(-1, 3, 3)
for block in blocks:
    tmp = []
    for row in block.tolist():
        tmp += row
    if len(set(tmp)) != 9:
        res = False

# print(res)

if res:
    print("Yes")
else:
    print("No")
