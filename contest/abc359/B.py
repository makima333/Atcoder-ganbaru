import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
3
1 2 1 3 2 3


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N = int(input())
A = list(map(int, input().split()))

ans = 0
for a_i, a in enumerate(A):
    if a_i < (2 * N) - 1:
        # print(a_i, a, A[a_i - 1], A[a_i + 1])
        if A[a_i - 1] == A[a_i + 1]:
            ans += 1
print(ans)
