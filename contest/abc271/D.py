import io
from operator import mod
import sys

_INPUT = """\
3 11
1 4
2 3
5 7



"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
(n, sum) = map(int, input().split())

ab_t = [tuple(map(int, input().split())) for _ in range(n)]

dp = [[0] * (sum + 1)]
dp[0][0] = 1

for a, b in ab_t:
    new_dp = [0] * (sum + 1)
    for i in range(sum):
        if dp[-1][i]:
            if i + a <= sum:
                new_dp[i + a] = 1
            if i + b <= sum:
                new_dp[i + b] = 2
    dp.append(new_dp)

if dp[n][sum]:
    print("Yes")
    res = ["T"] * n
    for i in reversed(range(1, n + 1)):
        if dp[i][sum] == 1:
            res[i - 1] = "H"
            sum -= ab_t[i - 1][0]
        else:
            sum -= ab_t[i - 1][1]
    print(*res, sep="")
else:
    print("No")
