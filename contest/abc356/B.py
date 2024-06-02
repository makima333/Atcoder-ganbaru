import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
2 4
10 20 30 40
20 0 10 30
0 100 100 0


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N, M = map(int, input().split())
A = list(map(int, input().split()))
x = [0 for _ in range(M)]
for _ in range(N):
    X = list(map(int, input().split()))
    for i, x_ in enumerate(X):
        x[i] += x_


ans = True
for a_, x_ in zip(A, x):
    if a_ > x_:
        ans = False
        break

print("Yes" if ans else "No")
