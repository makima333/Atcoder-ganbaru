import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
27

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

B = int(input())
a = 1
while a**a <= B:
    if a**a == B:
        print(a)
        exit()
    a += 1
print(-1)
