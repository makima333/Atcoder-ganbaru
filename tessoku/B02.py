import io
from operator import mod
import sys

_INPUT = """\
5 70



"""
sys.stdin = io.StringIO(_INPUT)
# --------------------------------
a, b = map(int, input().split())

for i in range(a, b + 1):
    if 100 % i == 0:
        print("Yes")
        exit(0)
print("No")
