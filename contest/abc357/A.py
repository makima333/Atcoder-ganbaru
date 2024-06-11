import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
5 10
12 3 2 3 3

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N, M = map(int, input().split())
H = list(map(int, input().split()))

ans = 0
for i in range(N):

    if H[i] <= M:
        ans += 1
        M -= H[i]
    else:
        break


print(ans)
