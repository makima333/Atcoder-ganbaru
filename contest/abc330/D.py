import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
15
xooxxooooxxxoox
oxxoxoxxxoxoxxo
oxxoxoxxxoxoxxx
ooooxooooxxoxxx
oxxoxoxxxoxoxxx
oxxoxoxxxoxoxxo
oxxoxooooxxxoox
xxxxxxxxxxxxxxx
xooxxxooxxxooox
oxxoxoxxoxoxxxo
xxxoxxxxoxoxxoo
xooxxxooxxoxoxo
xxxoxxxxoxooxxo
oxxoxoxxoxoxxxo
xooxxxooxxxooox


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N = int(input())

cells = []

for _ in range(N):
    cells.append(list(input()))

col_cnts = [0 for _ in range(N)]
for row in cells:
    for i, cell in enumerate(row):
        if cell == "o":
            col_cnts[i] += 1

ans = 0

for row in cells:
    col_cnt = 0
    row_cnt = -1
    for i, cell in enumerate(row):
        if cell == "o":
            row_cnt += 1
            tmp_col_cnt = -1
            tmp_col_cnt += col_cnts[i]
            # for j in range(N):
            #     if cells[j][i] == "o":
            #         tmp_col_cnt += 1
            if tmp_col_cnt > 0:
                col_cnt += tmp_col_cnt

    if row_cnt > 0:
        # print(row_cnt, col_cnt)
        ans += row_cnt * col_cnt
print(ans)
