import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
1

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------


N = int(input())

o = "o"

for _ in range(N - 1):
    o += "o"


print(f"L{o}ng")
