import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
6 200
100 675 201 200 199 328


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

n, x = map(int, input().split())

ss = list(map(int, input().split()))
ans = 0
for s in ss:
    ans += s if s <= x else 0

print(ans)
