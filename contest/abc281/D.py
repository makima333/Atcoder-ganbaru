import io
from operator import mod

_INPUT = """\
4 2 2
1 2 3 4


"""
import sys

sys.stdin = io.StringIO(_INPUT)

# ---------------------------------

# dp[nまで見た][k個][余り]

sys.setrecursionlimit(10**7)

N, K, D = map(int, input().split())
an = list(map(int, input().split()))

dp = [[[-1] * D for _ in range(K + 1)] for _ in range(N + 1)]
dp[0][0][0] = 0

for i in range(N):
    for j in range(K + 1):
        for k in range(D):
            if dp[i][j][k] == -1:
                continue

            # a_iを選ばない遷移
            dp[i + 1][j][k] = max(dp[i + 1][j][k], dp[i][j][k])

            # a_iを選ぶ遷移
            if j != K:
                dp[i + 1][j + 1][(k + an[i]) % D] = max(
                    dp[i + 1][j + 1][(k + an[i]) % D], dp[i][j][k] + an[i]
                )

print(dp[N][K][0])
