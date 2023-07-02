import io
from operator import mod
import sys

_INPUT = """\
4
1 3
1 3
2 2
1 3


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------

from decimal import Decimal

n = int(input())

probs = []
for i in range(n):
    a, b = map(Decimal, input().split())
    probs.append((i, a / (a + b)))

probs.sort(key=lambda x: (-x[1], x[0]))
for x, _ in probs:
    print(x + 1)
