import io
import sys
from tokenize import Double

_INPUT = """\
#.........
..........
..........
..........
..........
..........
..........
..........
..........
..........

 
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------

rows = [input() for _ in range(10)]

a, b, c, d = -1, -1, -1, -1
for i, row in enumerate(rows):
    row_lis = list(row)
    # すべて....
    if len(set(row_lis)) == 1 and row != "##########":
        if a != -1 and b == -1:
            b = i
        continue

    if a == -1:
        a = i + 1

    if c == -1 and d == -1:
        for col_i, cell in enumerate(row_lis):
            if c == -1 and cell == "#":
                c = col_i + 1
            if c != -1 and d == -1 and cell == ".":
                d = col_i

if b == -1:
    b = 10
if d == -1:
    d = 10

print(a, b)
print(c, d)
