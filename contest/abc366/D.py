import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
3
733 857 714
956 208 257
123 719 648
840 881 245
245 112 746
306 942 694
58 870 849
13 208 789
687 906 783
8
3 3 3 3 1 1
1 3 2 3 3 3
2 2 2 3 1 1
1 3 1 1 1 1
2 3 2 3 2 3
1 2 1 1 1 2
3 3 2 2 1 3
1 2 2 3 2 3

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
# 累積和、二次元累積和
N = int(input())

grids = []

for _ in range(N):
    grid = []
    for _ in range(N):
        row = list(map(int, input().split()))
        grid.append(row)
    grids.append(grid)

ruiseki_grids = []
for grid in grids:
    ruiseki_grid = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(N):
            ruiseki_grid[i + 1][j + 1] = (
                ruiseki_grid[i + 1][j]
                + ruiseki_grid[i][j + 1]
                - ruiseki_grid[i][j]
                + grid[i][j]
            )
    ruiseki_grids.append(ruiseki_grid)


qN = int(input())
for _ in range(qN):
    lx, rx, ly, ry, lz, rz = map(int, input().split())
    ans = 0
    for i in range(lx, rx + 1):
        grid = ruiseki_grids[i - 1]
        ans += grid[ry][rz] - grid[ly - 1][rz] - grid[ry][lz - 1] + grid[ly - 1][lz - 1]
    print(ans)
