import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
4 3 5
5 3 0 2
3 1 2 3
3 2 4 0
1 0 1 4

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
N, K, P = map(int, input().split())

dp = [[-1 for _ in range(K**10 + 1)] for _ in range(N + 1)]
dp[0][0] = 0


def dest(num, digits):
    num_str = str(num)

    while len(num_str) < len(digits):
        num_str = "0" + num_str

    result_str = ""
    for n, d in zip(num_str, digits):
        temp = int(n) - d
        if temp < 0:
            return -1
        if temp > 9:
            temp = 9
        result_str += str(temp)

    return int(result_str)


for i in range(1, N + 1):
    tmp = list(map(int, input().split()))
    cost = tmp[0]

    for j in range(K**10 + 1):
        # 選ぶばない
        if dp[i - 1][j] > -1 and dp[i][j] == -1:
            dp[i][j] = dp[i - 1][j]
        elif dp[i - 1][j] > -1:
            dp[i][j] = min(dp[i - 1][j], dp[i][j])

        # 選ぶ
        tmp_j = dest(j, tmp[1:])
        if tmp_j != -1:
            if dp[i - 1][tmp_j] > -1 and dp[i][j] == -1:
                dp[i][j] = dp[i - 1][tmp_j] + cost
            elif dp[i - 1][tmp_j] > -1:
                dp[i][j] = min(dp[i - 1][tmp_j] + cost, dp[i][j])


def check_digits_above_n(num, N):
    num_str = str(num)

    for digit in num_str:
        if int(digit) < N:
            return False

    return True


res = dp[-1]
ans = float("inf")
for e, k in enumerate(res):
    if e > int(str(P) * K):
        if check_digits_above_n(e, P):
            if k != -1:
                ans = min(k, ans)
                # print(e, k)

if ans == float("inf"):
    print(-1)
else:
    print(ans)
