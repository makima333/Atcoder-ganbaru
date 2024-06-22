import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
4 2
3 4 5 4
1 4


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()

ans = 0
a_i = 0
b_i = 0
while a_i < len(A) and b_i < len(B):
    a = A[a_i]
    if B[b_i] <= a:
        b_i += 1
        ans += a
    a_i += 1

if b_i < len(B):
    ans = -1

print(ans)
