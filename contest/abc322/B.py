import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
3 3
aaa
aaa

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N, M = map(int, input().split())

T = input()
S = input()

if S.startswith(T) and S.endswith(T):
    print(0)
elif S.startswith(T):
    print(1)
elif S.endswith(T):
    print(2)
else:
    print(3)
