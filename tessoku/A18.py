import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
4 11
3 1 4 5

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
# 2次元DP、部分和問題
N, S = map(int, input().split())
A = [0] + list(map(int, input().split()))

dp = [[False] * (S + 1) for _ in range(N + 1)]
dp[0][0] = True


for i in range(1, N + 1):
    for j in range(S + 1):
        if j < A[i]:
            if dp[i - 1][j]:
                dp[i][j] = True
            else:
                dp[i][j] = False
        else:
            if dp[i - 1][j - A[i]] or dp[i - 1][j]:
                dp[i][j] = True
            else:
                dp[i][j] = False

if dp[N][S]:
    print("Yes")
else:
    print("No")
