import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
3 2 5
1 2 9


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
from collections import deque

# 入力
n, a, b = map(int, input().split())
d = list(map(int, input().split()))

week_length = a + b

# 予定のある日を1週間の何日目かに変換し、重複を排除する
days = [d_i % week_length for d_i in d]
distinct_days = list(set(days))
distinct_days.sort()
distinct_days_deque = deque(distinct_days)

# 予定のある日の範囲がaを超えないかどうかをチェック
for _ in range(n):
    if distinct_days_deque[-1] - distinct_days_deque[0] < a:
        print("Yes")  # 予定のある日の範囲がa以内の場合、Yesを出力して終了
        exit()

    distinct_days_deque.rotate(-1)
    distinct_days_deque[-1] += week_length

print("No")  # 予定のある日の範囲がaを超える場合、Noを出力
