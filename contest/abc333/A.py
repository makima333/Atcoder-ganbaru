import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
3

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------


N = int(input())
n = str(N)

ans = ""
for _ in range(N):
    ans = f"{ans}{n}"

print(ans)
