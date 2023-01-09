import io
from operator import mod

_INPUT = """\
3
2023
50
1059872604593911


"""
import sys

sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
import math

n = int(input())

for _ in range(n):
    k = int(input())
    for p in range(2, int(k ** (1 / 2)) + 1):
        if k % p == 0:
            break

    if k % (p**2) == 0:
        q = k // p**2
    else:
        q = p
        p = math.sqrt(k // p)

    print(int(p), int(q))
