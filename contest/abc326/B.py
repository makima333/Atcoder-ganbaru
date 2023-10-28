import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
320

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------


N = int(input())

while True:
    n_str = str(N)
    if int(n_str[0]) * int(n_str[1]) == int(n_str[2]):
        break
    N += 1


print(N)
