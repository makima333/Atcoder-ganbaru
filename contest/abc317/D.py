import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
1
3 8 1



"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N = int(input())
xx = []
yy = []
zz = []

for _ in range(N):
    x, y, z = map(int, input().split())
    xx.append(x)
    yy.append(y)
    zz.append(z)

z_sum = sum(zz)

dp = [float("inf") for _ in range(z_sum + 1)]
dp[0] = 0

for i in range(N):
    x, y, z = (xx[i], yy[i], zz[i])
    w = max(0, (x + y) // 2 + 1 - x)
    for j in range(z_sum, z - 1, -1):
        dp[j] = min(dp[j], dp[j - z] + w)
        # print(dp)

print(min(dp[(z_sum // 2) + 1 :]))
