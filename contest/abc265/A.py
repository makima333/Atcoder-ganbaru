import io
from operator import mod
import sys

_INPUT = """\
100 100 100

"""
sys.stdin = io.StringIO(_INPUT)

#---------------------------------
x, y, n= map(int, input().split())

res = 0

if x*3 <= y:
    res = x * n
else:
    res = (y*(n//3)) +(x*(n % 3))

print(res)