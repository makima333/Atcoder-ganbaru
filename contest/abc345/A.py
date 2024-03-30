import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
==>


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

S = input()
s = S[1:-1]
s = set(s)

if S[0] == "<" and S[-1] == ">" and s == {"="}:
    print("Yes")
else:
    print("No")
