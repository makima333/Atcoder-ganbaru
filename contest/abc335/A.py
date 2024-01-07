import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
hello2024

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------


S = input()

s = S[:-1]

print(f"{s}4")
