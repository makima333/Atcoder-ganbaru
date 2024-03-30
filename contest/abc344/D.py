import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
aaabbbbcccc
6
2 aa aaa
2 dd ddd
2 ab aabb
4 bbaa bbbc bbb bbcc
2 cc bcc
3 ccc cccc ccccc

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------


def min_cost_to_match(T, bags):
    N = len(bags)
    M = len(T)
    INF = float("inf")

    # DPテーブルを無限大で初期化
    dp = [[INF] * (M + 1) for _ in range(N + 1)]

    # 初期状態
    dp[0][0] = 0

    for i in range(1, N + 1):
        for j in range(M + 1):
            # 袋から文字列を選ばない場合
            dp[i][j] = min(dp[i][j], dp[i - 1][j])

            # 袋から文字列を選ぶ場合
            for string in bags[i - 1]:
                next_j = j + len(string) if T.startswith(string, j) else j
                if next_j <= M:
                    dp[i][next_j] = min(dp[i][next_j], dp[i - 1][j] + 1)

    # 最終的な結果
    return dp[N][M] if dp[N][M] != INF else -1


T = input()
N = int(input())
bags = []
for _ in range(N):
    bag = list(map(str, input().split()))
    bags.append(bag[1:])


print(min_cost_to_match(T, bags))
