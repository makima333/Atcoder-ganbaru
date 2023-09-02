import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
2
0 100 0 100
0 100 0 100


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
N = int(input())

grid = []

for _ in range(100):
    tmp = [0 for _ in range(100)]
    grid.append(tmp.copy())


for _ in range(N):
    a, b, c, d = map(int, input().split())

    for x in range(a, b):
        for y in range(c, d):
            grid[x][y] = 1

ans = 0
for row in grid:
    ans += sum(row)
print(ans)
