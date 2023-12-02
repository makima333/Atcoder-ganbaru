import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
16 120 150 200



"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
N, S, M, L = map(int, input().split())
nap = [100000 for _ in range(120)]
nap[0] = 0

for i in range(120):
    if i == 0:
        continue

    size = 6
    if nap[i - size] != 100000:
        nap[i] = min(nap[i - size] + S, nap[i])

    size = 8
    if nap[i - size] != 100000:
        nap[i] = min(nap[i - size] + M, nap[i])
    size = 12
    if nap[i - size] != 100000:
        nap[i] = min(nap[i - size] + L, nap[i])

print(min(nap[N:]))
