import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
2 8


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

a, b = map(int, input().split())

print(a**b + b**a)
