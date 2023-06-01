import io
from operator import mod
import sys

_INPUT = """\
1 2 4
aaAaAaaAAAAaAaaAaAAaaaAAAAA



"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
X, Y, Z = map(int, input().split())
S = input()
dp = [[float("inf")] * 2 for _ in range(len(S) + 1)]
dp[0][0] = 0

# AAaA
# X Y Z = 1,3,3
# [0, 0]
# [1][0]=3 [1][1]=1+3
# [2][0]=6 or 1 + 3 + 4 [2][1]=  5 or 7

for s_i, s in enumerate(list(S)):
    if s == "A":
        dp[s_i + 1][0] = min(dp[s_i][0] + Y, dp[s_i][1] + Y + Z)
        dp[s_i + 1][1] = min(dp[s_i][0] + Z + X, dp[s_i][1] + X)
    else:
        dp[s_i + 1][0] = min(dp[s_i][0] + X, dp[s_i][1] + X + Z)
        dp[s_i + 1][1] = min(dp[s_i][0] + Z + Y, dp[s_i][1] + Y)

print(min(dp[len(S)]))
