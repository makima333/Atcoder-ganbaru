import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
200000 314 318

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------


N, M, P = map(int, input().split())

if N < M:
    print(0)
    exit()

ans = ((N - M) // P) + 1
print(ans)
