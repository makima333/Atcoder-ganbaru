import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
3
1 2
1 2
1 2

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N = int(input())

L = []
R = []

for _ in range(N):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

if sum(L) > 0 or sum(R) < 0:
    print("No")
    exit()

import copy

dl = copy.deepcopy(L)
sum_dl = sum(dl)

for i in range(N):
    tmp = min(-sum_dl, R[i] - L[i])
    sum_dl += tmp
    dl[i] += tmp

print("Yes")
print(*dl)
# print(sum(dl))
