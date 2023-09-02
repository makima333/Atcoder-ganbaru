import io
from operator import mod
import sys


_INPUT = """\
4
1 5 4
7 8
6
"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------


N = int(input())
vecs = [list(map(int, input().split())) for _ in range(N - 1)]

dp = [0] * (2**N)

for b in range(2**N):
    l = -1
    for i in range(N - 1):
        if not (b >> i) & 1:
            l = i
            break
    if l >= 0:
        for j in range(l + 1, N):
            if not (b >> j) & 1:
                nb = b | (1 << l) | (1 << j)
                dp[nb] = max(dp[nb], dp[b] + vecs[l][j - l - 1])


print(dp[-1])
