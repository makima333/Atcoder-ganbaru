import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
3
bc

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------


_ = input()

S = input()

if "ab" in S or "ba" in S:
    print("Yes")
else:
    print("No")
