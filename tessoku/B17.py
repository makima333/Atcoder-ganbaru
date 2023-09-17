import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
4
10 30 40 20

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
N = int(input())
hh = list(map(int, input().split()))

dp = [0 for _ in range(N)]


for i in range(1, N):
    if i == 1:
        dp[i] = abs(hh[i - 1] - hh[i])
        # print(abs(hh[i - 1] - hh[i]))
        continue
    dp[i] = min(
        abs(hh[i - 2] - hh[i]) + dp[i - 2],
        abs(hh[i - 1] - hh[i]) + dp[i - 1],
    )

ans = [N]
crr = N - 1

while crr > 0:
    if ans[-1] == 2:
        ans.append(1)
        break

    elif dp[crr] == abs(hh[crr - 2] - hh[crr]) + dp[crr - 2]:
        crr -= 2
        ans.append(crr + 1)
    else:
        crr -= 1
        ans.append(crr + 1)

ans.sort()
print(len(ans))
print(*ans)
