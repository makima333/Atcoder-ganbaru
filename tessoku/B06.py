import io
from operator import mod
import sys

_INPUT = """\
7
0 1 1 0 1 0 0
3
2 5
2 7
5 7

"""
sys.stdin = io.StringIO(_INPUT)
# --------------------------------
n = int(input())
an = list(map(int, input().split()))

q = int(input())

sums = [0]
tmp = 0
for a in an:

    tmp += a if a != 0 else -1
    sums.append(tmp)

for _ in range(q):
    l, r = map(int, input().split())
    tmp_sum = sums[r] - sums[l - 1]
    if tmp_sum > 0:
        print("win")
    elif tmp_sum < 0:
        print("lose")
    elif tmp_sum == 0:
        print("draw")
