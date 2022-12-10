import io
from operator import mod
import sys

_INPUT = """\
10 5
8 6 9 1 2 1 10 100 1000 10000
2 3
1 4
3 9
6 8
1 10

"""
sys.stdin = io.StringIO(_INPUT)
# --------------------------------
n, q = map(int, input().split())
ans = []

sums = [0]
an = list(map(int, input().split()))
lr = [list(map(int, input().split())) for _ in range(q)]

tmp = 0

for a in an:
    tmp += a
    sums.append(tmp)

for row in lr:
    l = row[0]
    r = row[1]
    print(sums[r] - sums[l - 1])
