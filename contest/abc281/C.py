import io
from operator import mod
import sys

_INPUT = """\
3 1200
180 240 120


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n, t = map(int, input().split())
an = list(map(int, input().split()))

tmp = sum(an)
if t > tmp:
    t %= tmp

sums = [0]
for i, a in enumerate(an):
    sums.append(sums[-1] + a)
    if sums[-2] < t and sums[-1] > t:
        print(f"{i+1} {abs(sums[-2] - t)}")
