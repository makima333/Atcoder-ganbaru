import io
from operator import mod
import sys

_INPUT = """\
1
0 0 0 0 0






"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n = int(input())
xx = list(map(int, input().split()))

xx.sort()

xx = xx[n : (-1) * n]


print(sum(xx) / len(xx))
