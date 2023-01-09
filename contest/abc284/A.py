import io
from operator import mod
import sys

_INPUT = """\
4
2023
Year
New
Happy


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n = int(input())
tmp = [input() for _ in range(n)]

for i in range(n):
    print(tmp[n - 1 - i])
