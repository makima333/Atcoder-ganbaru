import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
20
BBAAABBACAACABCBABAB


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

_ = input()
S = input()
print(S.find("ABC") + 1 if S.find("ABC") != -1 else -1)
