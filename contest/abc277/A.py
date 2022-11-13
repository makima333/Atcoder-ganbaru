import io
from operator import mod
import sys

_INPUT = """\
4 3
2 3 1 4

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n, x = map(int, input().split())
ns = list(map(int, input().split()))

for i, num in enumerate(ns):
    if num == x:
        print(i + 1)
        exit()
