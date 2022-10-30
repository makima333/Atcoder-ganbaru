import io
from operator import mod
import sys

_INPUT = """\
1000000000000000000 1000000000000000000 1000000000000000000 1000000000000000000 1000000000000000000 1000000000000000000



"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
a, b, c, d, e, f = map(int, input().split())

print(((a * b * c) - (d * e * f)) % 998244353)
