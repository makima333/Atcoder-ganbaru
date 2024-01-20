import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
4
10 2
10 1
10 2
3 2

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------


N = int(input())

score_t = 0
score_a = 0

for _ in range(N):
    t, a = map(int, input().split())
    score_t += t
    score_a += a

if score_t > score_a:
    print("Takahashi")
elif score_t < score_a:
    print("Aoki")
else:
    print("Draw")
