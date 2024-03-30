import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
3 7
2 2 3

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
# 2次元DP、部分和問題、DP復元
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

if not dp[N][S]:
    print(-1)
    exit()


# DP復元
ans = []
i = N
s = S

while i > 0:
    if dp[i][s] and not dp[i - 1][s]:
        ans.append(i)
        s -= A[i]
    i -= 1

print(len(ans))
print(*reversed(ans))
