import io
from operator import mod
import sys

_INPUT = """\
0


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
a = int(input())

if a:
    sum = 1
    for i in range(a):
        sum *= i + 1
    print(sum)
else:
    print(1)
