import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
6 2
1 2 1 2 1 2

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N, K = map(int, input().split())
A = list(map(int, input().split()))
A = A[(-1) * K :] + A[: (-1) * K]
print(*A)
