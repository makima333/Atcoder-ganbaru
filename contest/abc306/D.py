import io
from operator import mod
import sys

_INPUT = """\
5
1 100
1 300
0 -200
1 500
1 300



"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n = int(input())
dp = [[0, 0] for _ in range(n + 1)]

for i in range(n):
    poison, r = map(int, input().split())

    if poison == 0:
        dp[i + 1][0] = max(dp[i][0] + r, dp[i][0], dp[i][1] + r)
        dp[i + 1][1] = dp[i][1]
    elif poison == 1:
        dp[i + 1][0] = dp[i][0]
        dp[i + 1][1] = max(dp[i][1], dp[i][0] + r)

print(max(dp[n]))
