import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
5
1 3 99999999 99999994 1000000

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
import decimal

N = int(input())
A = list(map(int, input().split()))

mod = 10 ** 8

A.sort()

r = N
cnt = 0
for i in range(N):
    r = max(i+1, r)
    while r-1 > i and A[r-1] + A[i] >= mod:
        r -= 1
    cnt += N - r
    

total = sum([(N-1) * a for a in A])
total -= cnt * mod
print(total)