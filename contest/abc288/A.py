import io
from operator import mod
import sys

_INPUT = """\
3 1
abc
arc
agc

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n, k = map(int, input().split())
ss = []


for i in range(n):
    if i + 1 > k:
        break
    ss.append(input())

ss.sort()

[print(s) for s in ss]
