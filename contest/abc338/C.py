import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
2
800 300
100 0
0 10


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N = int(input())

Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
INF = 10**18

ans = 0

for a in range(max(Q) + 1):
    b = INF
    for i in range(N):
        if Q[i] < A[i] * a:
            b = -INF
        elif B[i] > 0:
            b = min(b, (Q[i] - A[i] * a) // B[i])
    ans = max(ans, a + b)

print(ans)
