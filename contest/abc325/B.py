import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
6
31 3
20 8
11 5
4 3
47 14
1 18



"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N = int(input())

wx = []
for _ in range(N):
    w, x = map(int, input().split())
    wx.append((w, x))

ans = 0
for t in range(24):
    tmp = 0
    for w, x in wx:
        time = (t + x) % 24

        if time >= 9 and time <= 17:
            tmp += w

    ans = max(tmp, ans)
print(ans)
