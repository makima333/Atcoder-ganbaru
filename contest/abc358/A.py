import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
AtCoder Land

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
S, T = input().split()
ans = False
if S == "AtCoder":
    if T == "Land":
        ans = True

print("Yes" if ans else "No")
