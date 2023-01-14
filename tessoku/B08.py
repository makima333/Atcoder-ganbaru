# import io
# from operator import mod
# import sys

# _INPUT = """\
# 5
# 1 3
# 2 5
# 3 4
# 2 6
# 3 3
# 4
# 1 3 3 6
# 1 5 2 6
# 1 3 3 5
# 1 1 6 6

# """
# sys.stdin = io.StringIO(_INPUT)
# --------------------------------

max_n = 1501
n = int(input())
grid = [[0] * max_n for _ in range(max_n)]


for _ in range(n):
    x, y = map(int, input().split())
    grid[x][y] += 1


grid_sum = [[0] * max_n for _ in range(max_n)]

for x in range(1, max_n):
    for y in range(1, max_n):
        grid_sum[x][y] = grid_sum[x][y - 1] + grid[x][y]


for y in range(1, max_n):
    for x in range(1, max_n):
        grid_sum[x][y] += grid_sum[x - 1][y]


q = int(input())
for _ in range(q):
    x_1, y_1, x_2, y_2 = map(int, input().split())
    ans = (
        grid_sum[x_2][y_2]
        - grid_sum[x_1 - 1][y_2]
        - grid_sum[x_2][y_1 - 1]
        + grid_sum[x_1 - 1][y_1 - 1]
    )
    print(ans)
