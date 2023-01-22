import io
from operator import mod

_INPUT = """\
2 14
2 3
5 6

"""
import sys

sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
N, X = map(int, input().split(" "))
coins = {}
kinds = [0]
for i in range(N):
    A, B = map(int, input().split(" "))
    coins[A] = B
    kinds.append(A)
dp = [[False] * (X + 1) for i in range(N + 1)]
dp[0][0] = True
for i in range(1, N + 1):
    price = kinds[i]
    for j in range(X + 1):
        for k in range(coins[price] + 1):
            print(i, j, k)

            [print(row) for row in dp]
            if price * k > j:
                print("break1")
                break
            if dp[i - 1][j - price * k] == True:
                dp[i][j] = True
                print("break2")
                break


if dp[N][X]:
    print("Yes")
else:
    print("No")
