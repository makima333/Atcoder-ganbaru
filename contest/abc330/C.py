import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
264428617



"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
import math
from bisect import bisect_left

# 与えられたDの値を取得
D = int(input())

# 予め2乗の値を計算しておく
squares = []
for x in range(int(math.sqrt(2 * (10**12))) + 1):  # 上限をsqrt(2 * (10**6))に変更
    squares.append(x * x)

# 最小値を見つけるための変数
ans = float("inf")

# 各xに対して、yの値を探す
for x2 in squares:  # xの2乗に対してループ
    target = D - x2
    if target < 0:  # ターゲットが負の場合、次のxに進む
        continue

    binidx = bisect_left(squares, target)
    if binidx < len(squares):
        y2 = squares[binidx]
        ans = min(ans, abs(x2 + y2 - D))
    if binidx - 1 < len(squares):
        y2 = squares[binidx - 1]
        ans = min(ans, abs(x2 + y2 - D))

print(ans)
