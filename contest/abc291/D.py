import io
from operator import mod
import sys

_INPUT = """\
3
1 2
4 2
3 4

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------


mod = 998244353

N = int(input())

data = [tuple(map(int, input().split())) for _ in range(N)]
dp = [[0, 0] for _ in range(N)]
dp[0] = [1, 1]

for i in range(1, N):
    for pre in range(2):
        for nxt in range(2):
            if data[i - 1][pre] != data[i][nxt]:
                dp[i][nxt] += dp[i - 1][pre]
    dp[i][0] %= mod
    dp[i][1] %= mod


print((dp[N - 1][0] + dp[N - 1][1]) % mod)
