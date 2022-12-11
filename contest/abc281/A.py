import io
from operator import mod
import sys

_INPUT = """\
Q142857Z



"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n = int(input())
for i in range(n + 1):
    print(n - i)
