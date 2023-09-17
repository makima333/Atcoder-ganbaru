import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
5
2 4 1 3
5 3 3



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

ans = [N]
crr = N - 1
while crr > 0:
    if dp[crr] == dp[crr - 2] + bb[crr]:
        ans.append(crr - 2 + 1)
        crr -= 2
    else:
        ans.append(crr - 1 + 1)
        crr -= 1

ans.sort()
print(len(ans))
print(*ans)
