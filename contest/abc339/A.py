import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
atcoder.jp


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

S = input()

print(S.split(".")[-1])
