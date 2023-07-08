import io
from operator import mod
import sys

_INPUT = """\
3 4




"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
a, b = map(int, input().split())

aa = set([(1, 2), (2, 3), (4, 5), (5, 6), (7, 8), (8, 9)])


if (a, b) in aa:
    print("Yes")
else:
    print("No")
