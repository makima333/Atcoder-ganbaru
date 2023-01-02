import io
from operator import mod
import sys

_INPUT = """\
10
7
0 3
2 4
1 3
0 3
5 6
5 6
5 6


"""
sys.stdin = io.StringIO(_INPUT)
# --------------------------------
T = int(input())
N = int(input())
B = [0, 0] + [0] * T

for _ in range(N):
    l, r = map(int, input().split())
    B[l] += 1
    B[r] -= 1

total = 0
for i in range(T):
    total += B[i]
    print(total)
