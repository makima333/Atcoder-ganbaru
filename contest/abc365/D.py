import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
24
SPRPSRRRRRPPRPRPSSRSPRSS


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
N = int(input())
S = input()
# R, S, P = グー、チョキ、パー

# DP, 動的計画法
# グー、チョキ、パー
dp = [0, 0, 0]

for s in S:
    new_dp = [0, 0, 0]
    # グー
    if s == "R":
        new_dp[0] = max(dp[1], dp[2])
        new_dp[1] = 0
        new_dp[2] = max(dp[0], dp[1]) + 1
    # チョキ
    elif s == "S":
        new_dp[0] = max(dp[1], dp[2]) + 1
        new_dp[1] = max(dp[0], dp[2])
        new_dp[2] = 0
    # パー
    else:
        new_dp[0] = 0
        new_dp[1] = max(dp[0], dp[2]) + 1
        new_dp[2] = max(dp[0], dp[1])
    dp = new_dp
    # print(dp)

print(max(dp))
