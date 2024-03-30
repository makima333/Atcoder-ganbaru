import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
||xyz


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------


S = input()

ss = S.split("|")
print(ss[0] + ss[2])
