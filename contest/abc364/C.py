import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
8 30 30
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
B = list(map(int, input().split()))
B.sort(reverse=True)

a_sum = 0
b_sum = 0

for i in range(N):
    a = A[i]
    b = B[i]

    a_sum += a
    b_sum += b

    if a_sum > X or b_sum > Y:
        print(i + 1)
        exit()

print(N)
