import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
3
Aoki
Takahashi
Takahashi

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------


N = int(input())
ans = 0
for _ in range(N):
    s = input()
    if s == "Takahashi":
        ans += 1
print(ans)
