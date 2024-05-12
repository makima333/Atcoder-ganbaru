import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
10
eixfumagit
vtophbepfe
pxbfgsqcug
ugpugtsxzq
bvfhxyehfk
uqyfwtmglr
jaitenfqiq
acwvufpfvv
jhaddglpva
aacxsyqvoj
eixfumagit
vtophbepfe
pxbfgsqcug
ugpugtsxzq
bvfhxyehok
uqyfwtmglr
jaitenfqiq
acwvufpfvv
jhaddglpva
aacxsyqvoj


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N = int(input())

grid_a = [list(input()) for _ in range(N)]
grid_b = [list(input()) for _ in range(N)]

for row_i, row in enumerate(grid_a):
    for col_i, cell in enumerate(row):
        if grid_a[row_i][col_i] != grid_b[row_i][col_i]:
            print(row_i + 1, col_i + 1)
