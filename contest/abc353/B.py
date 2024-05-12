import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
15 100
73 8 55 26 97 48 37 47 35 55 5 17 62 2 60



"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N, K = map(int, input().split())
A = list(map(int, input().split()))

from collections import deque

q = deque(A)

ans = 0
k = 0
while q:
    if k == 0:
        ans += 1
        k = K
    
    a = q.popleft()
    if a <= k:
        k -= a
    else:
        ans += 1
        k = K
        k -= a


print(ans)

