import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
3 9 2

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
A, B, D = map(int, input().split())
ans = [A]


while ans[-1] < B:
    ans.append(ans[-1] + D)


print(*ans)
