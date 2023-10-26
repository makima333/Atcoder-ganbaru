import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
Takahashi Chokudai

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

name = input().split()[0]

print(f"{name} san")
