import io
from operator import mod
import sys

_INPUT = """\
10 2



"""
sys.stdin = io.StringIO(_INPUT)
# --------------------------------
a, b = map(int, input().split())

print(a + b)
