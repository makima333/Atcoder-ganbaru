import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
5 2 3

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
N, L, R = map(int, input().split())

ans = [i for i in range(1, N + 1)]

tmp = reversed(ans[L - 1 : R])
ans = ans[: L - 1] + list(tmp) + ans[R:]

print(*ans)
