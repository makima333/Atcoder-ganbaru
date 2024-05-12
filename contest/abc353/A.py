import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
7
10 5 10 2 10 13 15

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N = int(input())
A = list(map(int, input().split()))
a1 = A[0]
a_max = A[0]
ans = -1
for i, a in enumerate(A[1:]):
    if max(a_max, a) != a_max:
        a_max = a
        # print(a)
        ans = i + 2
        break

print(ans)
