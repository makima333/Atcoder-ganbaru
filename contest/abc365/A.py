import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
1992

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N = int(input())

if N % 4 != 0:
    print(365)
elif N % 100 != 0 and N % 4 == 0:
    print(366)
elif N % 400 != 0 and N % 100 == 0:
    print(365)
elif N % 400 == 0:
    print(366)
