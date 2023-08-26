import io
from operator import mod
import sys

_INPUT = """\
10
1 19 75 37 17 16 33 18 22
41 28 89 74 98 43 42 31


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
N = int(input())

aa = [0]
aa += list(map(int, input().split()))

bb = [0, 0]
bb += list(map(int, input().split()))

dp = [0]

for i in range(1, N):
    if i == 1:
        time = dp[0] + aa[1]
    else:
        time = min(dp[i - 1] + aa[i], dp[i - 2] + bb[i])

    dp.append(time)


print(dp[-1])
