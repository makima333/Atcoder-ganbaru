import io
from operator import mod
import sys

_INPUT = """\
10 10



"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
a, b = map(int, input().split())

tmp = float(0)
tmp = b / a

print("{:.3f}".format(round(tmp, 3)))
