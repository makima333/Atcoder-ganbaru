import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
20 815 60
2066 3193 2325 4030 3725 1669 1969 763 1653 159 5311 5341 4671 2374 4513 285 810 742 2981 202


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N, K, X = map(int, input().split())
A = list(map(int, input().split()))

A.sort(reverse=True)
ans = 0

for i in range(N):
    if A[i] < X:
        break
    else:
        tmp = A[i]
        if K >= tmp // X:
            K -= tmp // X
            A[i] = tmp % X
        else:
            A[i] = tmp - X * K
            K = 0
            break

if K > 0:
    A.sort(reverse=True)
    for i in range(N):
        if K > 0:
            tmp = A[i]
            tmp = tmp - X * K
            A[i] = tmp if tmp > 0 else 0
            K -= 1
        else:
            break

print(sum(A))
