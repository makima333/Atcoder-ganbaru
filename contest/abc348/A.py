import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
9

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N = int(input())

ans = ""

for i in range(N):
    if (i + 1) % 3 == 0:
        ans += "x"
    else:
        ans += "o"

print(ans)
