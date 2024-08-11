import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
6 30
1 1 1 10 10 10

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
from bisect import bisect_left

N, M = map(int, input().split())
A = list(map(int, input().split()))

if sum(A) <= M:
    print("infinite")
    exit()

if N > M:
    print(0)
    exit()

A.sort()
A_ruisekisum = [0] * (N + 1)
for i in range(N):
    A_ruisekisum[i + 1] = A_ruisekisum[i] + A[i]

tmp_const = M // N
while True:
    idx = bisect_left(A, tmp_const)
    if idx == N:
        idx = N - 1
    if tmp_const != A[idx]:
        idx -= 1

    right_sum = (N - (idx + 1)) * tmp_const
    left_sum = A_ruisekisum[idx + 1]
    total = right_sum + left_sum
    if total <= M:
        ans = tmp_const
        # print(ans)
    else:
        break

    tmp = (M - total) // (N - (idx + 1))
    if tmp == 0:
        break
    tmp_const += tmp

    # tmp_const += 1

print(ans)
